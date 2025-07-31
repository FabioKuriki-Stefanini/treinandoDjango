from selenium import webdriver
import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from credenciais import usuario_login, usuario_senha

def setup_driver_para_download():
    """Configura driver para baixar PDFs automaticamente"""
    
    options = Options()
    
    pasta_download = "/home/fabiokuriki/pdfs"
    
    # Criar pasta se não existir
    if not os.path.exists(pasta_download):
        os.makedirs(pasta_download)
        print(f"Pasta criada: {pasta_download}")
    
    prefs = {
        "download.default_directory": pasta_download,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "plugins.always_open_pdf_externally": True,  # Força download
        "plugins.plugins_disabled": ["Chrome PDF Viewer"]  # Desabilita viewer
    }
    
    options.add_experimental_option('prefs', prefs)
    
    return webdriver.Chrome(options=options), pasta_download

# INÍCIO DO SCRIPT - Criar driver configurado
driver, pasta_download = setup_driver_para_download()

driver.get("https://www.natcorpbr.com.br/apex/hcm/f?p=310:")

# Login
time.sleep(2)
botao = driver.find_element(By.TAG_NAME, 'button')
usuario = driver.find_element(By.ID, "P900_USUARIO")
senha = driver.find_element(By.ID, "P900_SENHA")

usuario.send_keys(usuario_login)
senha.send_keys(usuario_senha)

botao.click()

# Acesso a tela de relatórios

partes = driver.current_url.split(':')
sessao = partes[3]
partes[2] = '11'
nova_url = ':'.join(partes)
driver.get(nova_url)

time.sleep(2)
# .//h3 - h3 dentro de li, independente se estiver dentro de uma div
li_recibo_pagamento = driver.find_element(By.XPATH, "//li[.//h3[contains(text(), 'Recibo de Pagamento')]]")
li_recibo_pagamento.click()
time.sleep(2)
iframe = driver.find_element(By.XPATH, "//iframe[@title='Recibo de Pagamento']")


# Entrar no iframe
driver.switch_to.frame(iframe)

select_element = driver.find_element(By.ID, "P55_DATA_REF")
select_mes = Select(select_element)
select_mes.select_by_index(1)

# Clicar no botão
botao_gerar_relatorio = driver.find_element(By.XPATH, "//button[span[contains(text(), 'Gerar Relatório')]]")
botao_gerar_relatorio.click()
time.sleep(2)

driver.quit()
