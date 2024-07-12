<a href="#english-version" style="background-color: #4CAF50; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 12px;">English Version</a>

[![Switch to English Version](https://img.shields.io/badge/Switch%20to-English%20Version-blue?style=flat-square)](#english-version)


# 🌟 Web Scraping de Distâncias entre Cidades por Regiões na Bahia
Projeto de Web Scraping de Distâncias entre Cidades, uma solução inovadora desenvolvida para atender demandas reais de meu ambiente de trabalho, proporcionando automação e eficiência na coleta de dados geográficos customizáveis

## 🚀 Visão Geral
Este projeto em Python automatiza a obtenção de distâncias entre cidades na Bahia utilizando o Google Maps como fonte de dados.
---
💡 Ideias Adicionais
Além das principais implementações, estamos considerando outras melhorias e recursos para o futuro:

Integração com APIs: Para obter dados mais precisos e em tempo real.
Suporte Multiplataforma: Garantir que o executável funcione perfeitamente em diferentes sistemas operacionais.
Melhorias na Performance: Otimizações no código para reduzir o tempo de execução e aumentar a eficiência.
criar um executável
criar um gui selecionável, com conversor de dados, que permite também sua inserção



## 🔧 Funcionalidades

- **Automatização**: Utiliza Selenium para interagir automaticamente com o Google Maps.
- **Organização por Regiões**: Cidades estão agrupadas por regiões específicas do estado da Bahia.
- **Exportação de Dados**: Resultados são salvos em um arquivo Excel para análise posterior.

## 🎯 Objetivo
O principal objetivo deste projeto é automatizar a coleta de dados de distâncias entre cidades na Bahia, agrupadas por regiões, para uso em diversas aplicações, desde planejamento logístico até estudos geográficos sem utilizar nenhuma API externa ou consultar banco de dados.

## 💡 Destaques Técnicos
Selenium WebDriver: Utilizado para navegar e interagir com o Google Maps.
Pandas: Para manipulação e exportação de dados.
Edge WebDriver: Configuração para o navegador Microsoft Edge, com flexibilidade para adaptação a outros navegadores.
Estrutura Flexível: Facilmente modificável para adicionar novas regiões e cidades.
## Pré-requisitos

Antes de executar o script, certifique-se de ter o Python instalado em seu sistema.

Além disso, é necessário ter o WebDriver adequado para o seu navegador configurado no seu diretório (apenas baixe e coloque na mesma pasta). 
- Eu usei o [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH)

---
Se preferir, você pode utilizar o ambiente virtual já configurado no projeto. Siga estas etapas para ativá-lo:
## 🚀 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/skyySea1/Massive-Web-Scraping-for-Regional-City-Distances
   cd seu-repositorio
   ```
### Configuração do Ambiente Virtual (Opcional)
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
python crawler_distancia.py
```

O script irá iterar sobre todas as combinações de origem e destino definidas em `regions.py`, coletará as distâncias via Google Maps e salvará os resultados em um arquivo Excel (`distancias_rotas.xlsx`) na pasta raiz do projeto.

## Estrutura do Projeto

- **`crawler_distancia.py`**: Script principal para iniciar o web scraping.
- **`regions.py`**: Módulo contendo as definições das regiões e suas respectivas cidades.
- **`Info/`**: Pasta contendo arquivos de suporte, como o módulo `regions.py`.

## 🌟 Oportunidades de Contribuição
.


Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorias, novos recursos ou correções.



# 🌟 Implementações Futuras

Estamos sempre buscando melhorar e expandir as funcionalidades do nosso projeto de **Web Scraping de Distâncias entre Cidades**. Aqui estão algumas das principais implementações futuras planejadas:

## 🚀 Futuras Implementações

### 1. Criar um Executável

Planejamos desenvolver um executável para simplificar ainda mais o uso do nosso projeto. Com isso, qualquer usuário poderá executar o programa sem precisar configurar um ambiente Python.

- **Facilidade de Uso**: Permite que usuários sem conhecimento técnico utilizem a ferramenta.
- **Portabilidade**: Facilita o compartilhamento e a distribuição da aplicação.
- **Automação Completa**: Executa todas as funcionalidades do script com um duplo clique.

### 2. Criar um GUI Selecionável

Estamos desenvolvendo uma interface gráfica de usuário (GUI) que tornará a interação com o projeto ainda mais intuitiva e amigável. A GUI permitirá:

- **Seleção Interativa**: Usuários poderão selecionar origens e destinos diretamente na interface.
- **Conversão de Dados**: Ferramentas para converter diferentes tipos de dados de forma simples e eficiente.
- **Inserção de Dados**: Possibilidade de inserir novos dados diretamente pela interface, facilitando a atualização e expansão da base de dados.

## 🎯 Benefícios Esperados

- **Melhoria na Usabilidade**: Interfaces intuitivas que reduzem a curva de aprendizado e aumentam a eficiência do usuário.
- **Aumento da Flexibilidade**: Usuários poderão personalizar e adaptar o uso da ferramenta conforme suas necessidades específicas.
- **Automação Aprimorada**: Processos totalmente automatizados, desde a coleta de dados até a geração de relatórios.

---

## 💡 Ideias Adicionais

Além das principais implementações, estamos considerando outras melhorias e recursos para o futuro:

- **Integração com APIs**: Para obter dados mais precisos e em tempo real.
- **Suporte Multiplataforma**: Garantir que o executável funcione perfeitamente em diferentes sistemas operacionais.
- **Melhorias na Performance**: Otimizações no código para reduzir o tempo de execução e aumentar a eficiência.

---

## 🌟 Participe do Desenvolvimento

Convidamos todos a participar do desenvolvimento dessas futuras implementações! Se você tem ideias, sugestões ou deseja contribuir com o código, sinta-se à vontade para abrir issues ou pull requests.

---

## 📫 Fique em Contato

Estamos sempre abertos a feedbacks e novas ideias. Entre em contato conosco para sugestões ou para saber mais sobre o andamento das implementações futuras:

- **LinkedIn**: [Marcell Henrique](linkedin.com/in/henrir1)
- **Email**: [henrir1020@gmail.com(mailto:henrir1020@gmail.com)


## Autor

Este projeto foi desenvolvido por [SkyySea1](https://github.com/skyySea1). Você pode entrar em contato comigo pelo LinkedIn, Discord, e-mail ou Instagram para qualquer dúvida, sugestão ou correção.




---

## English Version

---

# 🌟 Web Scraping de Distâncias entre Cidades por Regiões na Bahia

## 🌟 City Distance Web Scraping by Regions in Bahia
This is my City Distance Web Scraping project, an innovative solution developed to meet real demands in my work environment, providing automation and efficiency in collecting customizable geographic data.

## 🚀 Overview
This Python project automates the retrieval of distances between cities in Bahia using Google Maps as the data source.

## 🔧 Features

- **Automation**: Uses Selenium to automatically interact with Google Maps.
- **Region Organization**: Cities are grouped by specific regions in the state of Bahia.
- **Data Export**: Results are saved in an Excel file for further analysis.

## 🎯 Objective
The main objective of this project is to automate the collection of distance data between cities in Bahia, grouped by regions, for use in various applications, from logistical planning to geographical studies without using any external API or querying a database.

## 💡 Technical Highlights
- **Selenium WebDriver**: Used to navigate and interact with Google Maps.
- **Pandas**: For data manipulation and export.
- **Edge WebDriver**: Configuration for the Microsoft Edge browser, with flexibility for adaptation to other browsers.
- **Flexible Structure**: Easily modifiable to add new regions and cities.

## Prerequisites
Before running the script, make sure you have Python installed on your system.
Also, you need to have the appropriate WebDriver for your browser configured in your directory (just download and place it in the same folder). 
- I used [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH)

## 🚀 How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/skyySea1/Massive-Web-Scraping-for-Regional-City-Distances
   cd seu-repositorio
   ```

### Virtual Environment Setup (Optional)
2. Activate the virtual environment. Depending on your operating system:

   For Windows:
   ```bash
   venv\Scripts\activate
   ```

   For macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

3. Install the project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Script
To run the project:

```bash
python crawler_distancia.py
```

The script will iterate over all origin and destination combinations defined in `regions.py`, collect distances via Google Maps, and save the results in an Excel file (`distancias_rotas.xlsx`) in the project's root folder.

## Project Structure
- **`crawler_distancia.py`**: Main script to start web scraping.
- **`regions.py`**: Module containing region definitions and their respective cities.
- **`Info/`**: Folder containing support files, such as the `regions.py` module.

## 🌟 Contribution Opportunities
Contributions are welcome! Feel free to open issues and pull requests for improvements, new features, or fixes.

## 🌟 Future Implementations

### 1. Create an Executable
We plan to develop an executable to further simplify the use of our project. With this, any user can run the program without needing to set up a Python environment.

### 2. Create a Selectable GUI
We are developing a graphical user interface (GUI) that will make interaction with the project even more intuitive and user-friendly. The GUI will allow:
- **Interactive Selection**: Users can select origins and destinations directly in the interface.
- **Data Conversion**: Tools to convert different types of data simply and efficiently.
- **Data Insertion**: Possibility to insert new data directly through the interface, facilitating the update and expansion of the database.

---

## 💡 Additional Ideas
Besides the main implementations, we are considering other improvements and features for the future:
- **API Integration**: To obtain more accurate and real-time data.
- **Cross-Platform Support**: Ensuring the executable works perfectly on different operating systems.
- **Performance Improvements**: Code optimizations to reduce execution time and increase efficiency.

---

## 📫 Stay in Touch
We are always open to feedback and new ideas. Contact us for suggestions or to learn more about the progress of future implementations:
- **LinkedIn**: [Marcell Henrique](linkedin.com/in/henrir1)
- **Email**: henrir1020@gmail.com

## Author
This project was developed by [SkyySea1](https://github.com/skyySea1). You can contact me via LinkedIn, Discord, email, or Instagram for any questions, suggestions, or corrections.

