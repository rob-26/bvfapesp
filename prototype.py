from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl
import os

#https://openpyxl.readthedocs.io/en/stable/api/openpyxl.worksheet.worksheet.html  documentação openpyxl

def run():
#função  principal



    driver = webdriver.Firefox()
    driver.get('https://bv.fapesp.br/pt/')
    driver.maximize_window()
    time.sleep(2)
    #abre o site da biblioteca virtual

    programas = ['Mestrado', 'Doutorado', 'Doutorado Direto', 'Pós-Doutorado']

    ###MESTRADO

    m = 1
    
    fom = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.CLASS_NAME, 'dropdown')))
    fom.click()
    #abre o item de fomento à pesquisa
    
    pg = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.LINK_TEXT, 'Mestrado')))
    pg.click()
    #abre a página de cada programa

    inst = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.ID, 'pivot_expand_instfacet')))
    inst.click()
    #abre instituições sede

    a1 = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, '//li[@id="pivot_expand_Universidades"]/a')))
    a1.click()
    time.sleep(2)
    a2 = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH, '//li[@id="pivot_expand_UniversidadedeSoPauloUSP"]/a')))
    a2.click()
    #abre as instuituiçoes de ensino da usp

    nome_instituto = []
    num_de_bolsas = []
    #listas para colocar informações a planilhar

    unid = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="34_checkbox_UniversidadesUniversidadedeSoPauloUSPCentrodeBiologiaMarinhaCEBIMAR"]')))
    time.sleep(0.5)
    unid.click()
    refino = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//body/div[3]/div/div[2]/div/div[2]/section[2]/div[1]/form/ul/div[4]/li[2]/input')))
    refino.click()
    time.sleep(5)
    #abre a primeira unidade
    
    ni = WebDriverWait(driver,15).until(EC.presence_of_element_located((
        By.XPATH, '//*[@id="conteudo"]/div[2]/div/div[1]/section/div[1]/span')))
    nome_instituto.append(ni.text[19:])
    retangulo = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, '//body/div[3]/div/div[6]/section/div/div[1]/*[name()="svg" and @class = "svg-content"]/*[name()="g"]/*[name()="g"][16]/*[local-name()="rect"][2]')))
    time.sleep(1.5)
    verifica_nulo = retangulo.get_attribute('height')
    if verifica_nulo == '0':
        text_bolsas = 'Bolsas: 0'
    else:
        retangulo.click()
        time.sleep(2)
        num_bolsas = driver.find_element(By.XPATH, '//body/div[6]/span')
        text_bolsas = num_bolsas.text
    num_de_bolsas.append(text_bolsas[8:])
    #pega nome e numero de bolsas da primeira unidade


    while m != 58: # itera sobre todas as unidades
        
        time.sleep(2)
        unid = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,
            '//li[@id = "pivot_expand_UniversidadedeSoPauloUSP"]/ul/li[{}]/input'.format(m))))
        #//*[@id="34_checkbox_UniversidadesUniversidadedeSoPauloUSPEscoladeEngenhariadeLorenaEEL"]
        #//*[@id="pivot_expand_UniversidadedeSoPauloUSP"]
        #/html/body/div[3]/div/div[2]/div/div[2]/section[2]/div[2]/form/ul/div[4]/ul/div/li/ul/li[10]/ul/li[67]
        time.sleep(3)
        unid.click()
        
        m += 1
        time.sleep(3)
        
        unid = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,
            '//li[@id = "pivot_expand_UniversidadedeSoPauloUSP"]/ul/li[{}]/input'.format(m))))
        time.sleep(1)
        unid.click()

        refino = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,
            '//div[@id="refinamento_instfacet"]/li[2]/input')))
        time.sleep(1)
        refino.click()
        time.sleep(1)

        ni = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="conteudo"]/div[2]/div/div[1]/section/div[1]/span')))
        nome_instituto.append(ni.text[19:])
        
        retangulo = WebDriverWait(driver,10).until(
            EC.presence_of_element_located((By.XPATH, '//body/div[3]/div/div[6]/section/div/div[1]/*[name()="svg" and @class = "svg-content"]/*[name()="g"]/*[name()="g"][34]/*[local-name()="rect"][2]')))
        time.sleep(1.5)
        verifica_nulo = retangulo.get_attribute('height')
        if verifica_nulo == '0':
            text_bolsas = 'Bolsas: 0'
        else:
            retangulo.click()
            time.sleep(1)
            num_bolsas = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH, '//body/div[@class = "d3-tip n"]/span')))
            text_bolsas = num_bolsas.text
            time.sleep(1)
        num_de_bolsas.append(text_bolsas[8:])


    planilha = openpyxl.Workbook()
    sheet = planilha.active

    sheet['A1'] = 'Unidade'
    sheet['B1'] = 'Bolsas mestrado'

    i = 2
    for elemento in nome_instituto:
        sheet['A{}'.format(i)] = elemento
        i += 1

    j = 2
    for elemento in num_de_bolsas:
        sheet['B{}'.format(j)] = int(elemento)
        j += 1

    planilha.save('Bolsas Fapesp_final.xlsx')








def planilhar_dados():
#rascunho do recurso de pegar numero de bolsas e colocar em planilha
    
    with webdriver.Chrome() as driver:
        driver.get('https://bv.fapesp.br/pt/')
        time.sleep(3)

        navbar = driver.find_element(By.XPATH, '//*[@id="navbarNavDropdown"]/ul')

        texto = navbar.find_elements(By.XPATH, '//li/a/b')
        
        lista = []

        for elemento in texto:
            lista.append(elemento.text)
            time.sleep(1)
        
        planilha = openpyxl.Workbook()
        sheet = planilha.active

        i = 1
        for elemento in lista:
            sheet['A{}'.format(i)] = elemento
            i += 1

        planilha.save('hello.xlsx')

        
if __name__ == '__main__':
    run()
   

