from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from time import sleep

from src.driver import configuraDriver
from src.csv_ import escreveCSV


# Cabeçalho terminal 
print('\n')
print('=' * 50)
print('Scraper de Notícias do GE'.center(50))
print('=' * 50)
print('\n')

# Define a URL
url = 'https://ge.globo.com/'

# Pergunta ao usuário o que deseja pesquisar no site  
print('-' * 50)
pesquisa = input(' - O que deseja pesquisar no site? ')
print()

# Inicia o driver 
driver = configuraDriver()
driver.get(url)

# Preenchendo o campo de pesquisa
btn_busca = driver.find_element(By.XPATH, '//*[@id="busca-campo"]')
btn_busca.send_keys(pesquisa.upper())
sleep(1)
btn_busca.send_keys(Keys.ENTER)

# Pega a tabela com as noticias 
tabela_noticias = driver.find_element(By.CLASS_NAME, 'results__list')
# Guarda os objetos de noticia em uma lista 
noticias = tabela_noticias.find_elements(By.TAG_NAME, 'li')
print('-' * 50)

# Verifica se teve algum resultado na pesquisa 
if len(noticias) == 1 and 'Nenhum resultado encontrado' in noticias[0].text:
    print(f' - A pesquisa {pesquisa} teve nenhum resultado!'.center(50))
    # Fecha e torna false o driver
    driver.quit()
    driver = False

if driver:
    # Mostra ao usuário quantas notícias retornaram da pesquisa
    print(f' - {len(noticias)} notícias encontradas'.center(50))

    # Pergunta ao usuário quantas notícias
    while True:
        try:
            print()
            qnt_noticias = int(input(' - Quantas noticias deseja ver? ')) 
            if qnt_noticias > len(noticias):
                raise Exception()
            break
        except:
            print('Digite uma quantidade válida!')
    print()

    # Trata as informações das notícias retornadas
    resultados = []
    for i, noticia in enumerate(noticias[1:qnt_noticias+1]):
        print(f'   {i+1}: ', end='')

        texto_noticia = noticia.find_element(By.CLASS_NAME, 'widget--info__text-container')
        info_noticia = texto_noticia.find_element(By.TAG_NAME, 'a')

        # Informações para o usuário
        url_noticia = info_noticia.get_attribute('href')
        titulo_noticia = info_noticia.find_element(By.TAG_NAME, 'div').text

        # Adiciona os resultados a lista 
        resultados.append([titulo_noticia, url_noticia])

        # Printar Título da notícia
        print(titulo_noticia)

    # Cria a pasta "Data" caso não exista
    if not os.path.exists(r'.\data'):
        os.mkdir(r'.\data')

    # Escreve o resultado da pesquisa em um arquivo .txt em formato CSV
    arquivo = 'resultados.csv'
    caminho_base = os.getcwd()
    caminho_relativo_arquivo_csv = fr'data\{arquivo}'
    caminho_arquivo_csv = fr'{caminho_base}\data\{arquivo}'
    escreveCSV(resultados, caminho_relativo_arquivo_csv)
    print()
    print(f' >>> Notícias escolhidas foram salvas em: {caminho_arquivo_csv}')

print()
sleep(3)
print(' - Finalizando o programa...')
sleep(3)
print()
