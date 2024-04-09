# Importação das bibliotecas utilizadas
import time
import os
import openpyxl
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome  import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

# Acessar o site
service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://contabilidade-devaprender.netlify.app/")
time.sleep(3)

# Obter dados de e-mail e senha da planilha:
caminho_arquivo_email = 'dados_email'
arquivo = os.listdir(caminho_arquivo_email)
nome_arquivo = arquivo[0]
planilha = os.path.join(caminho_arquivo_email, nome_arquivo)
dados_planilha = pd.read_excel(planilha)
for indice, linha in dados_planilha.iterrows():
    email = linha['E-mail']
    senha = linha['senha']

# Digitar e-mail e senha - clicar em entrar
nav.find_element('xpath', '//*[@id="email"]').click()
nav.find_element('xpath', '//*[@id="email"]').send_keys(email)
time.sleep(1)
nav.find_element('xpath', '//*[@id="senha"]').click()
nav.find_element('xpath', '//*[@id="senha"]').send_keys(senha)
time.sleep(1)
nav.find_element('xpath', '//*[@id="Entrar"]').send_keys(Keys.ENTER)
time.sleep(5)

# obter os dados da planilha para colar nos campos de cadastro
caminho_arquivo_empresas = 'empresas'
arquivo_empresas = os.listdir(caminho_arquivo_empresas)
dados_empresas = arquivo_empresas[0]
planilha_empresas = os.path.join(caminho_arquivo_empresas, dados_empresas)
dados_planilha_empresas = pd.read_excel(planilha_empresas)

# for para criar as variáveis que serão utilizadas para o cadastro
for indice, linha in dados_planilha_empresas.iterrows():
    empresa = linha['Nome da Empresa']
    email = linha['Email']
    telefone = linha['Telefone']
    endereco = linha['Endereço']
    cnpj = linha['CNPJ']
    area = linha['Área de Atuação']
    qt_funcionario = linha['Quantidade de Funcionários']
    fundacao = linha['Data de Fundação']

    # colando cada variável em seu respectivo campo
    nav.find_element('xpath', '//*[@id="nomeEmpresa"]').send_keys(empresa)
    time.sleep(1)
    nav.find_element('xpath', '//*[@id="emailEmpresa"]').send_keys(email)
    time.sleep(1)
    nav.find_element('xpath', '//*[@id="telefoneEmpresa"]').send_keys(telefone)
    time.sleep(1)
    nav.find_element('xpath', '//*[@id="enderecoEmpresa"]').send_keys(endereco)
    time.sleep(1)
    nav.find_element('xpath', '//*[@id="cnpj"]').send_keys(cnpj)
    time.sleep(1)
    nav.find_element('xpath', '//*[@id="areaAtuacao"]').send_keys(area)
    time.sleep(1)
    nav.find_element('xpath', '//*[@id="numeroFuncionarios"]').send_keys(qt_funcionario)
    time.sleep(1)
    nav.find_element('xpath', '//*[@id="dataFundacao"]').send_keys(fundacao)
    time.sleep(1)
    # salvando o cadastro e aguardando nova tela para reiniciar o cadastro.
    nav.find_element('xpath', '//*[@id="Cadastrar"]').send_keys(Keys.ENTER)
    time.sleep(1)