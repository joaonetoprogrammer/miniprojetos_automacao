from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
import time
import pandas as pd
from IPython.display import display

tabela = pd.read_excel("NotasEmitir.xlsx")

# libera download suspeito
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": r"C:\Users\jn\Downloads",
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service = servico, options=options)
# entrar na página 
caminho = os.getcwd()
arquivo = caminho + r"\login.html"
navegador.get(arquivo)

# preencher os dados de login
navegador.find_element(By.XPATH, '/html/body/div/form/input[1]').send_keys('jn@gmail.com')
navegador.find_element(By.XPATH, '/html/body/div/form/input[2]').send_keys('123456')

# clicar no botão fazer login
navegador.find_element(By.XPATH, '/html/body/div/form/button').click()

for linha in tabela.index:
    # preenchcer os dado da NF
    navegador.find_element(By.NAME, 'nome').send_keys(tabela.loc[linha, "Cliente"])
    navegador.find_element(By.NAME, 'endereco').send_keys(tabela.loc[linha, "Endereço"])
    navegador.find_element(By.NAME, 'bairro').send_keys(tabela.loc[linha, "Bairro"])
    navegador.find_element(By.NAME, 'municipio').send_keys(tabela.loc[linha, "Municipio"])
    navegador.find_element(By.NAME, 'cep').send_keys(str(tabela.loc[linha, "CEP"]))
    navegador.find_element(By.NAME, 'uf').send_keys(tabela.loc[linha, "UF"])
    navegador.find_element(By.NAME, 'cnpj').send_keys(str(tabela.loc[linha, "CPF/CNPJ"]))
    navegador.find_element(By.NAME, 'inscricao').send_keys(str(tabela.loc[linha, "Inscricao Estadual"]))
    navegador.find_element(By.NAME, 'descricao').send_keys(tabela.loc[linha, "Descrição"])
    navegador.find_element(By.NAME, 'quantidade').send_keys(str(tabela.loc[linha, "Quantidade"]))
    navegador.find_element(By.NAME, 'valor_unitario').send_keys(str(tabela.loc[linha, "Valor Unitario"]))
    navegador.find_element(By.NAME, 'total').send_keys(str(tabela.loc[linha, "Valor Total"]))

    # clicar em emitir nota fiscal
    navegador.find_element(By.CLASS_NAME, 'registerbtn').click()
    navegador.refresh()

time.sleep(2)