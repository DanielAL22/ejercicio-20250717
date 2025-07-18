from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

def test_page_title():
    # Reemplaza la ruta por el path correcto a tu ChromeDriver
    # service = Service(r"C:\Program Files\chromedriver-win32\chromedriver.exe")
    browser = webdriver.Chrome()

    browser.get('https://github.com')

    # Buscar el elemento por su ID
    titleElement = browser.find_element(By.ID, 'hero-section-brand-heading')

    # Validar el texto exacto del elemento
    assert titleElement.text == 'Build and ship software on a single, collaborative platform'

    # Cerrar el navegador
    browser.quit()


