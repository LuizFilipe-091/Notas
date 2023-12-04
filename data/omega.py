from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium import webdriver

def Scrapping_Omega(DRIVER : webdriver.Chrome):

    NOTAS = {}

    MATERIAS = ['BIOLOGIA (BIOL)', 'ECOLOGIA APLICADA E IMPACTOS AMBIENTAIS (NEM-OMEGA-ECOLOGAPLI)'
                , 'FILOSOFIA (FILO)','FÍSICA (FISI)', 'FONTES DE ENERGIA E SUAS APLICAÇÕES (NEM-OMEGA-FENERGAPLI)', 
                'GEOGRAFIA (GEOG)','HISTÓRIA (HIST)', 'LÍNGUA INGLESA (LIEM)', 
                'LÍNGUA PORTUGUESA (LPOR)', 'LITERATURA (NEM-LITE)', 'MATEMÁTICA (MATE)',
                'PRODUÇÃO DE TEXTO (NEM-PTEX)', 'QUÍMICA (QUIM)', 'SOCIOLOGIA (SOCI)']
    
    ELEMENTO_SELECT = Select(DRIVER.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/totvs-page/div/div[3]/div/div/div/div/div/div[1]/div/totvs-page/div/div/div[1]/fieldset/div/edu-selecao-turmadisciplina/field/div/div/div/select'))
    #(len(MATERIAS))

    for materia in range(0, len(MATERIAS)+1):
        ELEMENTO_SELECT.select_by_index(materia)
        
