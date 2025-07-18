from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def test_github_hero_heading():
    # Configurar Chrome en modo headless para entornos como GitHub Actions
    options = Options()
    options.add_argument("--headless=new")  # `new` es más estable desde Chrome 109+
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)
    browser.get('https://github.com')

    # Espera simple (mejor usar WebDriverWait en casos reales)
    time.sleep(2)

    # Buscar el elemento y validar el contenido
    title_element = browser.find_element(By.ID, 'hero-section-brand-heading')
    expected_text = 'Build and ship software on a single, collaborative platform'

    assert title_element.text.strip() == expected_text

    browser.quit()
