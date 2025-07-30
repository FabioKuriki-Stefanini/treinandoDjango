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
li = driver.find_elements(By.TAG_NAME, 'li')
li[8].click()
time.sleep(2)
iframe = driver.find_element(By.XPATH, "//iframe[@title='Recibo de Pagamento']")


# Entrar no iframe
driver.switch_to.frame(iframe)

select_element = driver.find_element(By.ID, "P55_DATA_REF")
select = Select(select_element)
select.select_by_index(1)

# Clicar no botão
bot = driver.find_element(By.ID, 'B122641727466359905239')
bot.click()
time.sleep(2)

driver.quit()