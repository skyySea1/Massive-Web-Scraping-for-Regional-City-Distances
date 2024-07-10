

# Web Scraping de Distâncias entre Cidades - Google Maps

Este projeto em Python automatiza a obtenção de distâncias entre cidades na Bahia utilizando o Google Maps como fonte de dados.

-criar um executável
-criar um gui selecionável, com conversor de dados, que permite também sua inserção

## Funcionalidades

- **Automatização**: Utiliza Selenium para interagir automaticamente com o Google Maps.
- **Organização por Regiões**: Cidades estão agrupadas por regiões específicas do estado da Bahia.
- **Exportação de Dados**: Resultados são salvos em um arquivo Excel para análise posterior.

## Pré-requisitos

Antes de executar o script, certifique-se de ter o Python instalado em seu sistema. Você também precisa instalar as seguintes bibliotecas Python:

```bash
pip install selenium pandas openpyxl
```

Além disso, é necessário ter o WebDriver adequado para o seu navegador configurado no seu PATH. Este script foi configurado para usar o Microsoft Edge.

## Configuração do Ambiente Virtual (Opcional)

Se preferir, você pode utilizar o ambiente virtual já configurado no projeto. Siga estas etapas para ativá-lo:

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Ative o ambiente virtual. Dependendo do seu sistema operacional:

   Para Windows:
   ```bash
   venv\Scripts\activate
   ```

   Para macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

3. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```

## Executando o Script

Para executar o projeto:

```bash
python calculo_distancias.py
```

O script irá iterar sobre todas as combinações de origem e destino definidas em `regions.py`, coletará as distâncias via Google Maps e salvará os resultados em um arquivo Excel (`distancias_rotas.xlsx`) na pasta raiz do projeto.

## Estrutura do Projeto

- **`calculo_distancias.py`**: Script principal para iniciar o web scraping.
- **`regions.py`**: Módulo contendo as definições das regiões e suas respectivas cidades.
- **`Info/`**: Pasta contendo arquivos de suporte, como o módulo `regions.py`.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir um pull request com melhorias ou correções.

## Autor

Este projeto foi desenvolvido por [SkyySea1]. Você pode entrar em contato comigo pelo LinkedIn, Discord, e-mail ou Instagram para qualquer dúvida, sugestão ou correção.
