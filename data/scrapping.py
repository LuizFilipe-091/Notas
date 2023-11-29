from selenium import webdriver

def Scrapping():
    DRIVER = webdriver.Chrome()
    DRIVER.get('https://portaldoaluno.fiemg.com.br/FrameHTML/web/app/edu/PortalEducacional/#/notas')