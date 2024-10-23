import undetected_chromedriver as uc
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import pickle
import pyperclip

from main import gerar_cookies


#gerar_cookies()
time.sleep(2)  # Aguarda o carregamento completo da página

# Configura o serviço e o driver
driver = uc.Chrome()

# Acessa a página do site onde os cookies serão aplicados
driver.get('https://tjrj.pje.jus.br/1g/Painel/painel_usuario/advogado.seam')
time.sleep(5)  # Aguarda o carregamento completo da página

# Carrega os cookies do arquivo cookies.pkl
cookies = pickle.load(open("cookies.pkl", "rb"))
print("Cookies carregados:", cookies)

# Adiciona os cookies ao navegador
for cookie in cookies:
    if 'expiry' in cookie:
        del cookie['expiry']  # Remove a data de expiração dos cookies, se necessário
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print(f"Erro ao adicionar cookie: {e}")



