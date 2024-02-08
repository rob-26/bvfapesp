from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl

#https://openpyxl.readthedocs.io/en/stable/api/openpyxl.worksheet.worksheet.html  documentação openpyxl

def run():
#função  principal


### o que foi feito até agora:
### o programa consegue ir até a página de mestrado, abrir as unidades da usp, refinar a pesquisa apenas para o primeiro item.
### não é possível repetir o processo para outros programas.
### pegar o número de bolsas dentro do gráfico é obscuro ainda também.

###entender waits explícitos e colocá-los no lugar de sleeps
###como fazer para pegar do último caso em que para a iteração



    with webdriver.Chrome() as driver:

        ### PARTE 1 - encontrar o gráfico
        driver.get('https://bv.fapesp.br/pt/')
        #abre o site da biblioteca virtual

        programas = ['Mestrado', 'Doutorado', 'Doutorado Direto', 'Pós-Doutorado']

        ###MESTRADO

        m = 1
        
        fom = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME, 'dropdown')))
        fom.click()
        #abre o item de fomento à pesquisa
        
        pg = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Mestrado')))
        pg.click()
        #abre a página de cada programa

        inst = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, 'pivot_expand_instfacet')))
        inst.click()
        #abre instituições sede

        a1 = driver.find_element(By.XPATH, '//li[@id="pivot_expand_Universidades"]/a')
        a1.click()
        time.sleep(3.5)
        a2 = driver.find_element(By.XPATH, '//li[@id="pivot_expand_UniversidadedeSoPauloUSP"]/a')
        a2.click()
        time.sleep(2.5)
        #abre as instuituiçoes de ensino da usp

        unid = driver.find_element(By.XPATH, '//*[@id="34_checkbox_UniversidadesUniversidadedeSoPauloUSPCentrodeBiologiaMarinhaCEBIMAR"]')
        time.sleep(0.5)
        unid.click()

        refino = driver.find_element(By.XPATH, '//body/div[3]/div/div[2]/div/div[2]/section[2]/div[1]/form/ul/div[4]/li[2]/input')
        refino.click()
        time.sleep(5)
        
        while m != 59:

            unid = driver.find_element(By.XPATH,
                '//body/div[3]/div/div[2]/div/div[2]/section[2]/div[2]/form/ul/div[4]/ul/div/li/ul/li[10]/ul/li[67]/ul/li[{}]/input'.format(m))
            time.sleep(1)
            unid.click()
            m += 1
            time.sleep(1)
            unid = driver.find_element(By.XPATH,
                '//body/div[3]/div/div[2]/div/div[2]/section[2]/div[2]/form/ul/div[4]/ul/div/li/ul/li[10]/ul/li[67]/ul/li[{}]/input'.format(m))
            time.sleep(1)
            unid.click()
            time.sleep(2)

            refino = driver.find_element(By.XPATH, '//body/div[3]/div/div[2]/div/div[2]/section[2]/div[2]/form/ul/div[4]/li[2]/input')
            time.sleep(1)
            refino.click()
            time.sleep(5)
            #refina
        #itera sobre cada instituto


        

        input()







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
   

