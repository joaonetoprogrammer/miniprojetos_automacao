from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import time

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service = servico)
# entrar na página 
caminho = os.getcwd()
arquivo = caminho + r"\login.html"
navegador.get(arquivo)

# preencher os dados de login
navegador.find_element(By.XPATH, '/html/body/div/form/input[1]').send_keys('jn@gmail.com')
navegador.find_element(By.XPATH, '/html/body/div/form/input[2]').send_keys('123456')

# clicar no botão fazer login
navegador.find_element(By.XPATH, '/html/body/div/form/button').click()

# preenchcer os dado da NF
navegador.find_element(By.NAME, 'nome').send_keys('Joao Neto Automação')
navegador.find_element(By.NAME, 'endereco').send_keys('Jose Bonifacio')
navegador.find_element(By.NAME, 'bairro').send_keys('Centro')
navegador.find_element(By.NAME, 'municipio').send_keys('Fortaleza')
navegador.find_element(By.NAME, 'cep').send_keys('65151541')
navegador.find_element(By.NAME, 'uf').send_keys('CE')
navegador.find_element(By.NAME, 'cnpj').send_keys('51215415154545215')
navegador.find_element(By.NAME, 'inscricao').send_keys('45152121212')
navegador.find_element(By.NAME, 'descricao').send_keys('Curso Joao Neto')
navegador.find_element(By.NAME, 'quantidade').send_keys('1')
navegador.find_element(By.NAME, 'valor_unitario').send_keys('50,00')
navegador.find_element(By.NAME, 'total').send_keys('50,00')

# clicar em emitir nota fiscal
navegador.find_element(By.CLASS_NAME, 'registerbtn').click()

time.sleep(2)