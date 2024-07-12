import csv
import os

# Caminho atual
caminho_base = os.getcwd()

def escreveCSV(dados, filename='resultados.csv'):
    '''
    ------------------------------------------------------------------------------------------------
    Exporta os resultados das notícias para um arquivo CSV.
    
    Args:
        dados (list): Lista de tuplas contendo títulos e URLs das notícias.
        filename (str): Nome do arquivo CSV de saída. Padrão é 'resultados.csv'.
    ------------------------------------------------------------------------------------------------
    '''

    # Define o caminho para o arquivo
    caminho = fr'{caminho_base}\{filename}'

    # Abre o arquivo CSV para escrita
    with open(caminho, mode='w', newline='', encoding='utf-8') as file:
        # Define os nomes das colunas
        fieldnames = ['Título', 'URL']
        
        # Cria um writer de dicionários
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        # Escreve o cabeçalho
        writer.writeheader()
        
        # Escreve os dados
        for titulo, url in dados:
            writer.writerow({'Título': titulo, 'URL': url})
            writer.writerow({})  # Adiciona uma linha em branco entre registros
