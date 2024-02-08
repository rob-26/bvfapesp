from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def run():
#função  principal

    with webdriver.Chrome() as driver:

        m = 1

        ### PARTE 1 - encontrar o gráfico
        driver.get('https://bv.fapesp.br/pt/')
        time.sleep(3)
        #abre o site da biblioteca virtual

        
        fom  = driver.find_element(By.CLASS_NAME, 'dropdown')
        fom.click()
        time.sleep(1)
        #abre o item de fomento à pesquisa
        
        pg = driver.find_element(By.LINK_TEXT, 'Mestrado')
        pg.click()
        time.sleep(2.5)
        #abre a página de cada programa

        inst = driver.find_element(By.ID, 'pivot_expand_instfacet')
        inst.click()
        time.sleep(5)
        #abre instituições sede

        a1 = driver.find_element(By.XPATH, '//li[@id="pivot_expand_Universidades"]/a')
        a1.click()
        time.sleep(2.5)
        a2 = driver.find_element(By.XPATH, '//li[@id="pivot_expand_UniversidadedeSoPauloUSP"]/a')
        a2.click()
        time.sleep(1.5)
        #abre as instuituiçoes de ensino da usp
        
        
        unid = driver.find_element(By.XPATH, '//*[@id="34_checkbox_UniversidadesUniversidadedeSoPauloUSPCentrodeBiologiaMarinhaCEBIMAR"]')
        time.sleep(0.5)
        unid.click()

        refino = driver.find_element(By.XPATH, '//body/div[3]/div/div[2]/div/div[2]/section[2]/div[1]/form/ul/div[4]/li[2]/input')
        refino.click()
        time.sleep(5)
        
        #/html/body/div[3]/div/div[6]/section/div/div[1]/svg/g/g[23]/rect[2]    RETANGULO COM BOLSAS
        retangulo = driver.find_element(By.XPATH, '//body/div[3]/div/div[6]/section/div/div[1]/*[name()="svg" and @class = "svg-content"]/*[name()="g"]/*[name()="g"][23]/*[local-name()="rect"][2]')
        time.sleep(1.5)
        retangulo.click()
        time.sleep(2)

        num_bolsas = driver.find_element(By.XPATH, '//body/div[6]/span')
        text_bolsas = num_bolsas.text
        print(text_bolsas)

        

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