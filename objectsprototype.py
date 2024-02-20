from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PáginaFapesp:

    def __init__(self, driver):
        self.driver = driver
        self._fom =  WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'dropdown')))
        
    @property
    def fom (self):
        return WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'dropdown')))     

    @property
    def pag_mest(self):
        return WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.LINK_TEXT, 'Mestrado')))
    
    @property
    def pag_doc(self):
        return WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.LINK_TEXT, 'Doutorado')))

    @property
    def pag_doc_dir(self):
        return WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.LINK_TEXT, 'Doutorado Direto')))

    @property
    def pag_pos_doc(self):
        return WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.LINK_TEXT, 'Pós-Doutorado')))
    
    @property
    def inst(self):
        return WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.ID, 'pivot_expand_instfacet')))
    
    @property
    def a1(self):
        return WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH,
             '//li[@id="pivot_expand_Universidades"]/a')))

    @property
    def a2(self):
        time.sleep(2)
        return WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, 
            '//li[@id="pivot_expand_UniversidadedeSoPauloUSP"]/a')))

    @property
    def unid1_cebimar(self):
        time.sleep(0.5)
        return WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, 
            '//*[@id="34_checkbox_UniversidadesUniversidadedeSoPauloUSPCentrodeBiologiaMarinhaCEBIMAR"]')))
    
    @property
    def unid1_cena(self):
        time.sleep(0.5)
        return WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, 
            '//*[@id="34_checkbox_UniversidadesUniversidadedeSoPauloUSPCentrodeEnergiaNuclearnaAgriculturaCENA"]')))

    @property
    def refino(self):
        time.sleep(0.5)
        return WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, 
            '//div[@id="refinamento_instfacet"]/li[2]/input')))

    @property
    def pega_nome(self):
        time.sleep(0.5)
        return WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, 
            '//*[@id="conteudo"]/div[2]/div/div[1]/section/div[1]/span'))).text

    @property
    def retangulo(self):
        return WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, 
            '//body/div[3]/div/div[6]/section/div/div[1]/*[name()="svg" and @class = "svg-content"]/*[name()="g"]/*[name()="g"][34]/*[local-name()="rect"][2]')))

    @property
    def num_bolsas(self):
        return WebDriverWait(self.driver,15).until(EC.presence_of_element_located((By.XPATH, 
            '//body/div[@class = "d3-tip n"]/span'))).text
         
        