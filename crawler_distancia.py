from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
import pandas as pd
from module.regions import regions
import time
import openpyxl
# Configuração do WebDriver
service = EdgeService()
options = webdriver.EdgeOptions()
options.add_argument('--log-level=1')
options.add_argument('--disable-extensions')
options.add_argument('headless')

driver = webdriver.Edge(service=service, options=options)

final_date = driver,
# Definição das variáveis de origem e destinos
# dicionário que recebe a lista de destinos do módulo regions	e associa esses valores a chave origem(que é a cidade de origem)
origens = {
     "Paulo Afanoso, Bahia": regions.get['Itaparica, Bahia'], 'Semiárido Nordeste II'],
     "Salvador, Bahia": regions.get['Região Metropolitana de Salvador'],
     "Feira de Santana, Bahia": regions.get['Centro-Norte Baiano'],
     "Vitória da Conquista, Bahia": regions.get['Centro-Sul Baiano'],
     "Barreiras, Bahia": regions.get['Oeste Baiano'],
     "Juazeiro, Bahia": regions.get['Norte Baiano'],
     "Serrinha, Bahia": regions.get['Nordeste Baiano'],
     "Itabuna, Bahia": regions.get['Sul Baiano']
}

# Lista para armazenar os resultados
resultados = []

# Loop para cada origem e seus respectivos destinos
# a variável origem é a chave do dicionário origens, e destinos é o valor associado a essa chave
# a iteração é feita sobre o método items() do dicionário, que retorna uma tupla com a chave e o valor associado
#ou seja, para cada origem (chave) há um destino (valor) que por sua vez compõe uma lista de valores 
#exemplo de iteração: para a origem "Paulo Afanoso, Bahia", os destinos são "Itaparica, Bahia" e "Semiárido Nordeste II"
# imprima todos os pares chave-valor de juazeiro e ele imprimirá, juazeiro: cidade 1; juazeiro cidade 2 até a lista acabar
for origem, destinos in origens.items():
    # para o método items funcionar, o dicionário origens deve ser um dicionário de listas e não um dicionário de dicionários (porque ele retorna uma tupla, que é uma lista imutável)
    #também é possível usar o método values() que retorna apenas os valores associados a cada chave
    #ou seja, para cada origem há uma lista de destinos, e laço segue essa lógica
    #o método items() não aceita parâmetros, se fosse para imprimir apenas as cidades, seria necessário usar o método values()
    for destino in destinos:
        try:
            # Abrir página inicial do Google Maps
            driver.get("https://www.google.com/maps")
            wait = WebDriverWait(driver, 15)  #   tempo de espera
            # Aguardar até que o campo de pesquisa esteja disponível
            search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchboxinput"]')))
            search_box.clear()
            search_box.send_keys(f"{origem} to {destino}")
            search_box.send_keys(Keys.ENTER)
            click = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="omnibox-directions"]/div/div[2]/div/div/div/div[2]')))
            click.click()

            # Aguardar até que a distância da rota seja carregada
            distancia = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="section-directions-trip-0"]/div[1]/div/div[1]/div[2]/div')))
            distancia_texto = distancia.text
            print(f"Distância de {origem} para {destino}: {distancia_texto}")
            
            
            # Armazenar o resultado na lista
            resultados.append({
                'Origem': origem,
                'Destino': destino,
                'Distância': distancia_texto
            })
        
        except Exception as e:
            print(f"Erro ao calcular a rota de {origem} para {destino}: {str(e)}")

driver.quit()

# Converter resultados para DataFrame do pandas
df = pd.DataFrame(resultados)

# Salvar em Excel
nome_arquivo = 'distancias_rotas.xlsx'
df.to_excel(nome_arquivo, index=False)

print(f"Resultados salvos em '{nome_arquivo}'")
input("Pressione Enter para sair") # adicione system pause no terminal