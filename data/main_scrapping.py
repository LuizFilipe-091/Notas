from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from alfa import Scrapping_Alfa
from omega import Scrapping_Omega

def Scrapping(login, senha, ano):
    chrome = Options()
    #chrome.add_argument('--headless')
    DRIVER = webdriver.Chrome(options=chrome)
    DRIVER.get('https://portaldoaluno.fiemg.com.br/FrameHTML/web/app/edu/PortalEducacional/#/notas')

    sleep(5)

    DRIVER.find_element(By.ID, 'User').send_keys(login)
    DRIVER.find_element(By.ID, 'Pass').send_keys(senha)

    DRIVER.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div[4]/input').click()
    sleep(10)

    series = [DRIVER.find_element(By.CSS_SELECTOR, f'#divListaCursos > div:nth-child({i}) > div:nth-child(2) > div > div.media-body > div:nth-child(3) > small:nth-child(2)')
              for i in range(1,4)]
    
    INPUTS = {'1ª Série': '/html/body/div[7]/div/div/div[2]/div[2]/form/div[3]/div[3]/div[2]/div/div[1]/div[1]/input',
              '2ª Série': '/html/body/div[7]/div/div/div[2]/div[2]/form/div[3]/div[2]/div[2]/div/div[1]/div[1]/input',
              '3ª Série': '/html/body/div[7]/div/div/div[2]/div[2]/form/div[3]/div[1]/div[2]/div/div[1]/div[1]/input'}
    for serie in series:
        if ano == serie.text:
            DRIVER.find_element(By.XPATH, INPUTS[ano]).click()

    DRIVER.find_element(By.ID, 'btnConfirmar').click()
    sleep(4)
    DRIVER.find_element(By.XPATH, '/html/body/div[2]/div[2]/div/div/div[2]/div/div/totvs-page/div/div[3]/div/div/div/div/ul/li[2]/a').click()
    
    ITINERÁRIO = DRIVER.find_element(By.CSS_SELECTOR, '#menu-header-items > ul > li:nth-child(4) > span').text
    
    if 'Novo' in ITINERÁRIO:
        sleep(3)
        Scrapping_Alfa(DRIVER)
    else:
        sleep(3)
        Scrapping_Omega(DRIVER)
    sleep(5)

if __name__ == '__main__':
    #Scrapping('0000470798', 'Em103796@', '2ª Série')
    Scrapping('00841012', 'LUIZIN091', '2ª Série')
