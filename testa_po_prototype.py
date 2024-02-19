from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from objectsprototype import *

dominio = 'https://bv.fapesp.br/pt/'

def run():

    dd = 1
    driver = webdriver.Firefox()
    driver.get(dominio)
    driver.maximize_window()
    time.sleep(2)

    pagina = PáginaFapesp(driver)
    pagina.fom.click()
    pagina.pag_doc_dir.click()
    pagina.inst.click()
    pagina.a1.click()
    time.sleep(2)
    pagina.a2.click()
    #abre as instuituiçoes de ensino da usp
    nome_instituto = []
    num_de_bolsas = []
    #listas para colocar informações a planilhar

    input()


run()