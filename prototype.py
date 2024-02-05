from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def run():
#função  principal

    with webdriver.Chrome() as driver:

        ### PARTE 1 - encontrar o gráfico
        driver.get('https://bv.fapesp.br/pt/')
        time.sleep(3)
        #abre o site da biblioteca virtual

        programas = ['Mestrado', 'Doutorado', 'Doutorado Direto', 'Pós-Doutorado']

        for programa in programas:

            inst = 1
            
            fom  = driver.find_element(By.CLASS_NAME, 'dropdown')
            fom.click()
            time.sleep(2)
            #abre o item de fomento à pesquisa
            
            pg = driver.find_element(By.LINK_TEXT, programa)
            pg.click()
            time.sleep(3.5)
            #abre a página de cada programa

            inst = driver.find_element(By.ID, 'pivot_expand_instfacet')
            inst.click()
            time.sleep(4.5)
            #abre instituições sede

            a1 = driver.find_element(By.XPATH, '//li[@id="pivot_expand_Universidades"]/a')
            a1.click()
            time.sleep(3.5)
            a2 = driver.find_element(By.XPATH, '//li[@id="pivot_expand_UniversidadedeSoPauloUSP"]/a')
            a2.click()
            time.sleep(2.5)
            #abre as instuituiçoes de ensino da usp

            unidusp = driver.find_elements(By.XPATH, 
                '/html/body/div[3]/div/div[2]/div/div[2]/section[2]/div[1]/form/ul/div[4]/ul/div/li/ul/li[10]/ul/li[67]/ul/li/input')
            time.sleep(3)

            for unidade in unidusp:
                unidade.click()
                time.sleep(1)
                unidade.click()
                time.sleep(1)

            ######ALGORITMO DE ABRE E FECHA
            '''
            cebi = driver.find_element(By.XPATH, 
                '//*[@id="34_checkbox_UniversidadesUniversidadedeSoPauloUSPCentrodeBiologiaMarinhaCEBIMAR"]')
            cebi.click()
            time.sleep(1)
            cebi.click()
            time.sleep(1)
            cena = driver.find_element(By.XPATH, 
                '//*[@id="34_checkbox_UniversidadesUniversidadedeSoPauloUSPCentrodeEnergiaNuclearnaAgriculturaCENA"]')
            time.sleep(1)
            cena.click()
            '''
            ############ FIM DO ALGORITMO
            '''
            unid = driver.find_element(By.XPATH, '//body/div[3]/div/div[2]/div/div[2]/section[2]/div[2]/form/ul/div[4]/ul/div/li/ul/li[10]/ul/li[67]/ul/li[1]/input')
            unid.click()
            while inst != 59:

                unid = driver.find_element(By.XPATH, '//body/div[3]/div/div[2]/div/div[2]/section[2]/div[2]/form/ul/div[4]/ul/div/li/ul/li[10]/ul/li[67]/ul/li[inst]/input')
                unid.click()
                inst += 1
                time.sleep(1)
                unid = driver.find_element(By.XPATH, '//body/div[3]/div/div[2]/div/div[2]/section[2]/div[2]/form/ul/div[4]/ul/div/li/ul/li[10]/ul/li[67]/ul/li[inst]/input')
                unid.click()
                time.sleep(2)

                refino = driver.find_element(By.XPATH, '//body/div[3]/div/div[2]/div/div[2]/section[2]/div[1]/form/ul/div[4]/li[2]/input')
                refino.click()
                time.sleep(5)
                #refina
            #itera sobre cada instituto
'''


            

            '''
            ###PARTE 2 - pegar o número de bolsas
            retangulo = driver.find_element(By.XPATH, '//div[@id = "barras_historico_vinc"]/svg/g/g[34]/rect[2]')
            retangulo.click()
            time.sleep(2)
            texto = driver.find_element(By.XPATH, '//body/div[6]/span')
            print(texto.text)
            ##/html/body/div[3]/div/div[6]/section/div/div[1]/svg/g/g[34]/rect[2]
            ##/html/body/div[6]/span
            '''
            

        input()



if __name__ == '__main__':
    run()

