from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Scrapping(login, senha, ano):
    DRIVER = webdriver.Chrome()
    DRIVER.get('https://portaldoaluno.fiemg.com.br/FrameHTML/web/app/edu/PortalEducacional/#/notas')

    sleep(5)

    DRIVER.find_element(By.ID, 'User').send_keys(login)
    DRIVER.find_element(By.ID, 'Pass').send_keys(senha)

    DRIVER.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div[4]/input').click()
    serie = WebDriverWait(DRIVER, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'cursor-pointer ng-binding ng-hide'))
    )
    
    print(serie.text)




if __name__ == '__main__':
    Scrapping('00841012', 'LUIZIN091', '2º Ano')
