from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
from selenium.webdriver import ActionChains
import time
import pandas as pd
from IPython.display import display

# criar o navegador
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service = servico)

# abrir a página index (entrar no site da busca juridica)
caminho = os.getcwd()
arquivo = caminho + r"\index.html"

#importar base de dados
tabela = pd.read_excel("Processos.xlsx")
display(tabela)

for linha in tabela.index:

    navegador.get(arquivo)
    #abrir lista de cidades
    botao = navegador.find_element(By.CLASS_NAME, 'dropdown-menu')
    ActionChains(navegador).move_to_element(botao).perform()
    cidade = tabela.loc[linha, "Cidade"]

    navegador.find_element(By.PARTIAL_LINK_TEXT, cidade).click()

    #mudar para nova aba
    aba_original = navegador.window_handles[0]
    indice = 1 + linha
    nova_aba = navegador.window_handles[indice]

    #seleciona a aba nova
    navegador.switch_to.window(nova_aba)

    # preencher o formulario com os dados de busca
    navegador.find_element(By.ID, 'nome').send_keys(tabela.loc[linha, "Nome"])
    navegador.find_element(By.ID, 'advogado').send_keys(tabela.loc[linha, "Advogado"])
    navegador.find_element(By.ID, 'numero').send_keys(tabela.loc[linha, "Processo"])

    # clicar em pesquisar
    navegador.find_element(By.CLASS_NAME, 'registerbtn').click()

    #finaliza o primeiro alerta
    alerta = navegador.switch_to.alert
    alerta.accept()

    while True:
        try:
            alerta = navegador.switch_to.alert
            break
        except:
            time.sleep(1)
    
    texto_alerta = alerta.text

    if "Processo encontrado" in texto_alerta:
        alerta.accept()
        tabela.loc[linha, "Status"] = "Encontrado"
    else:
        alerta.accept()
        tabela.loc[linha, "Status"] = "Não Encontrado"

display(tabela)
tabela.to_excel("Tabela Atualizada.xlsx")
""""



# esperar o resultado da pesquisa e agir de acordo com o resultado


time.sleep(10)
"""