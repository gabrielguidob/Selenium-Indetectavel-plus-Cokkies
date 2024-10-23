from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyperclip

# Configurações para o Chrome com webdriver normal
options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

# Iniciando o WebDriver com o Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Função para aguardar o carregamento completo da página
def wait_for_page_load(driver, timeout=5):
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        return True
    except TimeoutException:
        print("A página demorou muito para carregar.")
        return False

# Função para aguardar o elemento ficar presente
def wait_for_element(driver, by, value, timeout=5):
    try:
        return WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
    except TimeoutException:
        print(f"Elemento com {by} = '{value}' demorou muito para aparecer.")
        return None

# Parte de login
driver.get('https://tjrj.pje.jus.br/1g/Painel/painel_usuario/advogado.seam')
wait_for_page_load(driver)

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

# Aguardar recarregamento e login
time.sleep(5)

# Recarrega a página
driver.get('https://tjrj.pje.jus.br/1g/Painel/painel_usuario/advogado.seam')
wait_for_page_load(driver)

# Acessa a página de consulta de processos
driver.get('https://tjrj.pje.jus.br/1g/Processo/ConsultaProcesso/listView.seam')
wait_for_page_load(driver)

# Função para buscar processo, com tentativa de reabrir a URL se um elemento não for encontrado
def search_process(url, process_number, search_box_id, search_result_id, max_retries=3):
    retries = 0
    while retries < max_retries:
        driver.get(url)
        if wait_for_page_load(driver):
            try:
                pyperclip.copy(process_number)
                
                # Aguardar a presença do campo de busca
                search_box = wait_for_element(driver, By.ID, search_box_id)
                if search_box:
                    search_box.click()
                    time.sleep(0.3)
                    # Simula o comando "CTRL + V" para colar o conteúdo
                    actions = ActionChains(driver)
                    actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
                    
                    # Envia a tecla ENTER para submeter o formulário
                    search_box.send_keys(Keys.RETURN)
                    
                    # Aguardar o carregamento dos resultados
                    result_element = wait_for_element(driver, By.ID, search_result_id)
                    if result_element:
                        # Extrai o resultado
                        search_result = result_element.text
                        print(search_result)
                        break
                    else:
                        # Reabre a URL caso o resultado não apareça
                        print("Resultado não encontrado, reabrindo a URL.")
                        driver.get(url)
                else:
                    print("Campo de busca não encontrado, reabrindo a URL.")
                    driver.get(url)
            except Exception as e:
                print(f"Ocorreu um erro: {e}. Tentando novamente...")
                driver.get(url)
        else:
            print("Página não carregou corretamente, reabrindo a URL.")
            driver.get(url)
        retries += 1
    if retries == max_retries:
        print(f"Não foi possível realizar a busca após {max_retries} tentativas.")

# Testando com os sites e números de processos
url = 'https://tjrj.pje.jus.br/1g/Processo/ConsultaProcesso/listView.seam'
process_number = '0808927-80.2023.8.19.0075'
search_box_id = 'fPP\:numeroProcesso\:numeroSequencial'
search_result_id = 'fPP\:processosTable\:3157330\:j_id492'
search_process(url, process_number, search_box_id, search_result_id)

url = 'https://pje1g.tjrn.jus.br/pje/ConsultaPublica/listView.seam'
process_number = '0868308-55.2023.8.20.5001'
search_box_id = 'fPP:numProcesso-inputNumeroProcessoDecoration:numProcesso-inputNumeroProcesso'
search_result_id = 'fPP:processosTable:3334498:j_id233'
search_process(url, process_number, search_box_id, search_result_id)

url = 'https://pje1g.trf3.jus.br/pje/ConsultaPublica/listView.seam'
process_number = '5003889-93.2024.4.03.6181'
search_box_id = 'fPP:numProcesso-inputNumeroProcessoDecoration:numProcesso-inputNumeroProcesso'
search_result_id = 'fPP:processosTable:10791562:j_id234'
search_process(url, process_number, search_box_id, search_result_id)

url = 'https://pje.tjes.jus.br/pje/ConsultaPublica/listView.seam'
process_number = '5031621-53.2023.8.08.0024'
search_box_id = 'fPP:numProcesso-inputNumeroProcessoDecoration:numProcesso-inputNumeroProcesso'
search_result_id = 'fPP:processosTable:7545966:j_id232'
search_process(url, process_number, search_box_id, search_result_id)
