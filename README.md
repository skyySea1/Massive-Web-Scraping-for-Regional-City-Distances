

# 🌟 Web Scraping de Distâncias entre Cidades por Regiões na Bahia
Este é o meu projeto de Web Scraping de Distâncias entre Cidades, uma solução inovadora desenvolvida para atender demandas reais de meu ambiente de trabalho, proporcionando automação e eficiência na coleta de dados geográficos customizáveis
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



📫 Contato
Estou sempre aberto a feedbacks e novas oportunidades. Entre em contato comigo pelo LinkedIn ou envie um email para seu-email@example.com.


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





