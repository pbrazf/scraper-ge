import os
import logging
import sys
from selenium import webdriver
from time import sleep

class SuppressOutput:
    '''
    ------------------------------------------------------------------------------------------------
    Classe para suprimir a saída padrão e os erros durante a execução do WebDriver.
    ------------------------------------------------------------------------------------------------
    '''

    def __enter__(self):
        self._original_stdout = sys.stdout
        self._original_stderr = sys.stderr
        sys.stdout = open(os.devnull, 'w')
        sys.stderr = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stderr.close()
        sys.stdout = self._original_stdout
        sys.stderr = self._original_stderr


def configuraDriver():
    '''
    ------------------------------------------------------------------------------------------------
    Configura o WebDriver do Selenium com várias opções para evitar avisos e melhorar a performance.
    
    Retorna:
        WebDriver: Instância configurada do WebDriver do Chrome.
    ------------------------------------------------------------------------------------------------
    '''
    
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-software-rasterizer')
    options.add_argument('--disable-extensions')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--disable-webgl')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-logging')
    options.add_argument('--log-level=3')
    
    logging.getLogger('selenium').setLevel(logging.ERROR)
    
    with SuppressOutput():
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
    
    sleep(3)
    return driver
