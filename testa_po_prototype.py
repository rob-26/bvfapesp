from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from objectsprototype import *

dominio = 'https://bv.fapesp.br/pt/'

def run():

    pd = 1

    driver = webdriver.Firefox()
    driver.get(dominio)
    driver.maximize_window()
    time.sleep(2)

    pagina = PáginaFapesp(driver)
    pagina.fom.click()
    pagina.pag_pos_doc.click()
    pagina.inst.click()
    pagina.a1.click()
    time.sleep(2)
    pagina.a2.click()
    #abre as instituiçoes de ensino da usp

    nome_instituto = []
    num_de_bolsas = []
    #listas para colocar informações a planilhar

    pagina.unid1_cebimar.click()
    pagina.refino.click()
    time.sleep(5)
    #abre a primeira unidade

    nome_instituto.append(pagina.pega_nome[19:])
    len_anterior = len(pagina.pega_nome[19:])
    time.sleep(1.5)
    if pagina.retangulo.get_attribute('height') == '0':
        text_bolsas = 'Bolsas: 0'
    else:
        pagina.retangulo.click()
        time.sleep(2)
        text_bolsas = pagina.num_bolsas
    num_temp = int(text_bolsas[8:])
    num_de_bolsas.append(num_temp)
    #pega nome e numero de bolsas da primeira unidade

    while pd != 62: # itera sobre todas as unidades
    
        pd += 1
        time.sleep(3)
        somatorio = num_temp
        
        unid = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,
            '//li[@id = "pivot_expand_UniversidadedeSoPauloUSP"]/ul/li[{}]/input'.format(pd))))
        time.sleep(1)
        unid.click()
        pagina.refino.click()
        time.sleep(1)

        nome_instituto.append(pagina.pega_nome[len_anterior:])
        len_anterior = len(pagina.pega_nome)
        
        if pagina.retangulo.get_attribute('height') == '0':
            text_bolsas = 'Bolsas: 0'
        else:
            pagina.retangulo.click()
            time.sleep(1)
            text_bolsas = pagina.num_bolsas
            time.sleep(1)
        
        num_temp = int(text_bolsas[8:])
        num_final = num_temp - somatorio    
        num_de_bolsas.append(num_final)
    
    print(nome_instituto)
    print(num_de_bolsas)

    input()


run()