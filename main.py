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

email = 'bielcomecuzin@gmail.com'
password = 'bebezinho1337'
def gerar_cookies():
    # Configura o serviço e o driver
    service = Service(ChromeDriverManager().install())
    driver = uc.Chrome()

    # Faz login no Google
    #driver.get('https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fwww.google.com%3Fhl%3Dpt-BR&ec=GAlA8wE&hl=pt-BR&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S216395%3A1729675689328078&ddm=0')
    #
    #email_selector = 'identifierId'
    #
    #WebDriverWait(driver, 10).until(
    #    EC.visibility_of_all_elements_located((By.ID, email_selector))
    #)
    #
    #driver.find_element(By.ID, email_selector).send_keys(email)
    #driver.find_element(By.CSS_SELECTOR, '#identifierNext > div > button > span').click()
    #
    #password_selector = '#password > div.aCsJod.oJeWuf > div > div.Xb9hP > input'
    #
    #WebDriverWait(driver, 10).until(
    #    EC.visibility_of_all_elements_located((By.CSS_SELECTOR, password_selector))
    #)
    #driver.find_element(By.CSS_SELECTOR, password_selector).send_keys(password)
    #driver.find_element(By.CSS_SELECTOR,'#passwordNext > div > button > span').click()
    #
    #time.sleep(5)

    driver.get('https://tjrj.pje.jus.br/1g/Painel/painel_usuario/advogado.seam')

    time.sleep(2)

    # Cria a instância do ActionChains
    actions = ActionChains(driver)

    # Enviar 8 vezes a tecla Tab
    for _ in range(8):
        actions.send_keys(Keys.TAB)

    # Enviar o número e mais Tab e Enter
    actions.send_keys('93762755604')
    actions.send_keys(Keys.TAB)
    actions.send_keys('m@cedo8163')
    actions.send_keys(Keys.ENTER)

    # Executar todas as ações de uma vez
    actions.perform()

    time.sleep(5)

    cookies = driver.get_cookies()
    print(cookies)

    pickle.dump(cookies, open("cookies.pkl", "wb"))

    driver.close()

#input('Pressione qualquer tecla para sair...')
