from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service = servico)

navegador.get("https://br.investing.com/currencies/usd-brl-historical-data")
time.sleep(20)
#maximiza a tela para que o botao de baixar fique visivel
navegador.maximize_window()
time.sleep(2)

navegador.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/span[2]').click()
time.sleep(3)
navegador.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/form/button[1]').click()
time.sleep(3)
navegador.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').sendkeys("joaonetoempreendedor@gmail.com")



time.sleep(5)