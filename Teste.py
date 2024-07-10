from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
import pandas as pd
from Info import regions
import time

# Configuração do WebDriver
service = EdgeService()
options = webdriver.EdgeOptions()
options.add_argument('--log-level=3')
# options.add_argument('headless')
driver = webdriver.Edge(service=service, options=options)


# Definição das variáveis de origem e destinos
origens = {
    "Salvador, Bahia": regions['Região Metropolitana de Salvador'],
    "Feira de Santana, Bahia": regions['Centro-Norte Baiano'],
    "Vitória da Conquista, Bahia": regions['Centro-Sul Baiano'],
    "Barreiras, Bahia": regions['Oeste Baiano'],
    "Juazeiro, Bahia": regions['Norte Baiano'],
    "Serrinha, Bahia": regions['Nordeste Baiano'],
    "Itabuna, Bahia": regions['Sul Baiano']
}

# Lista para armazenar os resultados
resultados = []

# Loop para cada origem e seus respectivos destinos
for origem, destinos in origens.items():
    for destino in destinos:
        try:
            # Abrir página inicial do Google Maps
            driver.get("https://www.google.com/maps")
            wait = WebDriverWait(driver, 30)  #   tempo de espera
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