
---

# Web Scraping de Distâncias entre Cidades por Regiões
Devido a demandas internas do meu ambiente de trabalho, desenvolvi esta solução para melhorar suprir demandas atuais e servir de uso para futuras (planejo em breve adicionar um executável com formato GUI, que permite que o usuário escolha o que quer adicioinar, converta tipos de dados e alimente o script)
Este projeto realiza web scraping para obter distâncias entre duas cidades na Bahia utilizando o Google Maps . O objetivo é automatizar a coleta de dados de distância entre várias cidades (2 por vez no esquema 1:! agrupadas por regiões específicas do estado da Bahia.

## Funcionalidades

- **Automatização**: Utiliza Selenium para automatizar a interação com o Google Maps.
- **Organização por Regiões**: Cidades estão organizadas por regiões, facilitando a busca por distâncias específicas.
- **Exportação de Dados**: Os resultados são exportados para um arquivo Excel para fácil análise e compartilhamento.

## Pré-requisitos

Certifique-se de ter os seguintes requisitos instalados:

- Python 3.x
- Selenium
- Pandas
- Webdriver do Microsoft Edge (é fácil alterar para outros navegadores, só mudar um parâmetro
- Ou se preferir, pode baixar meu ambiente virtual para esse projeto com todas importações, módulos e dependências que o script usa (explicaado melhor em [Clique aqu (venv)](#uso-do-ambiente-virtual-venv)

Você pode instalar as dependências utilizando pip:

```bash
pip install selenium pandas
```

## Configuração

1. **WebDriver**: Este projeto utiliza o Microsoft Edge WebDriver. Certifique-se de baixar e configurar o WebDriver compatível com sua versão do navegador.

2. **Atualização das Regiões**: Para adicionar ou modificar as regiões e suas respectivas cidades, edite o arquivo `regions.py`.

## Uso

Para executar o projeto:

```bash
python main.py
```

O script irá iterar sobre todas as combinações de origem e destino definidas em `regions.py`, coletar as distâncias via Google Maps e salvar os resultados em um arquivo Excel.

## Estrutura do Projeto

- **`main.py`**: O script principal para iniciar o web scraping.
- **`regions.py`**: Módulo contendo as definições das regiões e suas respectivas cidades.
- **`Info/`**: Pasta contendo arquivos de suporte, como o módulo `regions.py`.

Entendi! O código que você forneceu utiliza Selenium para automatizar o Google Maps e calcular distâncias entre diferentes origens e destinos na Bahia. Aqui está a documentação e README para este script:

---

## Web Scraping de Distâncias entre Cidades - Google Maps

Este script em Python utiliza Selenium para automatizar a obtenção de distâncias entre cidades na Bahia, utilizando o Google Maps como fonte de dados.

### Pré-requisitos

Antes de executar o script, certifique-se de ter o Python instalado em seu sistema. Além disso, é necessário instalar as seguintes bibliotecas Python:

```bash
pip install selenium pandas openpyxl
```

Certifique-se também de ter o WebDriver adequado para o seu navegador instalado e configurado no seu PATH. Este script foi configurado para usar o Microsoft Edge.

### Configuração do Ambiente Virtual (Opcional)

Se preferir, você pode usar o ambiente virtual configurado fornecido no projeto. Veja as instruções no README para ativá-lo.

### Executando o Script

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Execute o script Python:
   ```bash
   python calculo_distancias.py
   ```

### Funcionamento

O script utiliza Selenium para abrir o Google Maps, inserir os locais de origem e destino, e capturar a distância das rotas calculadas. Os resultados são armazenados em um arquivo Excel (`distancias_rotas.xlsx`) na pasta raiz do projeto.

### Observações

- Certifique-se de ter uma conexão estável com a internet durante a execução do script.
- O tempo de espera (`wait.until`) pode ser ajustado conforme necessário, dependendo da velocidade da sua conexão e do desempenho do Google Maps.

## Uso do Ambiente Virtual (venv) {#uso-do-ambiente-virtual-venv}

Se preferir utilizar o ambiente virtual configurado para este projeto, siga estas etapas:

1. Copie o diretório do ambiente virtual (`venv`) para a raiz do projeto.
2. Ative o ambiente virtual. Dependendo do seu sistema operacional, o comando pode variar:

   Para Windows:
   ```bash
   venv\Scripts\activate
   ```

   Para macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

3. Após ativar o ambiente virtual, instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```

4. Agora você pode executar o projeto conforme descrito na seção de Uso do README.

## Contribuição

Contribuições são bem-vindas! Se você deseja adicionar novas funcionalidades, melhorar a eficiência do código ou corrigir problemas, sinta-se à vontade para abrir um pull request.

## Autor

Este projeto foi desenvolvido por [SkyySea1].
_qualquer dúvida, sugestão ou correção pode entrar em contato comigo pelo linkedin, discord, emaim ou instagram

---

