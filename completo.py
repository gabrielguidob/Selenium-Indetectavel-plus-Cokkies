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
import pyperclip


options = uc.ChromeOptions()
options.binary_location = "/usr/bin/google-chrome"
driver = uc.Chrome(options=options)


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
# Após adicionar os cookies, recarrega a página
driver.get('https://tjrj.pje.jus.br/1g/Painel/painel_usuario/advogado.seam')
time.sleep(5)  # Aguarda o carregamento da página com os cookies aplicados
driver.get('https://tjrj.pje.jus.br/1g/Processo/ConsultaProcesso/listView.seam')


def search_process(url, process_number, search_box_id, search_result_id):
    driver.get(url)
    #input('asdaw')
   
    pyperclip.copy(process_number)
    search_box = driver.find_element(By.ID, search_box_id)
    search_box.click()
    # Simula o comando "CTRL + V" (ou "Command + V" no Mac) para colar o conteúdo
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()  # No Mac, troque CONTROL por COMMAND se necessário

    # Envia a tecla ENTER para submeter o formulário
    search_box.send_keys(Keys.RETURN)
    input('asdaw')
    time.sleep(1)
    search_result = driver.find_element(By.ID, search_result_id).text
    print(search_result)

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