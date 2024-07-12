# Scraper de Notícias do GE

Este projeto é um scraper desenvolvido em Python para extrair notícias do site GE (Globo Esporte). O usuário pode pesquisar por termos específicos e obter os títulos e URLs das reportagens correspondentes.

## Funcionalidades

- Pesquisa de notícias no site GE com base em um termo fornecido pelo usuário.
- Retorna os títulos e URLs das reportagens encontradas.
- Exporta os resultados para um arquivo CSV.

## Requisitos

- Python 3.7 ou superior
- Selenium 3.141.0
- TensorFlow 2.7.0

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/pbrazf/scraper-noticias-ge.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd scraper-noticias-ge
    ```
3. Crie um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    source venv/bin/activate # No Windows use `venv\Scripts\activate`
    ```
4. Instale os pacotes necessários:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Execute o script `main.py`:
    ```bash
    python main.py
    ```
2. Siga as instruções no terminal para inserir o termo de pesquisa.
3. Veja os resultados no terminal e no arquivo `resultados.csv`.

## Estrutura do Projeto

- `src/`: Contém os módulos do scraper.
  - `csv_.py`: Funções para gerar o arquivo .csv.
  - `driver.py`: Funções para configurar o webdriver.
- `main.py`: Script principal para executar o scraper.
- `requirements.txt`: Arquivo de dependências do projeto.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## Autor

- Pedro Ferreira Braz - [pbraz.pedrof@gmail.com](mailto:pbraz.pedrof@gmail.com)
- GitHub: [pbrazf](https://github.com/pbrazf)
- Linkedin: [pbrazf](https://www.linkedin.com/in/pbrazf/)
