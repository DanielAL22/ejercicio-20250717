# Importar las bibliotecas necesarias
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Crear una instancia del navegador Chrome
driver = webdriver.Chrome()

# Navegar al sitio web de DuckDuckGo
driver.get("https://duckduckgo.com/")

# Encontrar el campo de búsqueda por su atributo 'name'
buscador = driver.find_element(By.NAME, "q")

# Escribir el texto "inmuebles en Bogotá" en el campo de búsqueda
buscador.send_keys("inmuebles en Bogotá")

# Simular que se presiona la tecla Enter para realizar la búsqueda
buscador.send_keys(Keys.RETURN)

# Esperar 2 segundos para que los resultados carguen (espera fija)
time.sleep(2)


# Esperar hasta que aparezcan elementos con la clase CSS '.result'
# Esto evita usar time.sleep y hace la prueba más estable
# WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, ".result"))
# )



# Buscar todos los elementos que tengan la clase CSS 'result'
resultados = driver.find_elements(By.CSS_SELECTOR, ".result")

# Verificar que al menos haya un resultado; si no, lanzar un error
assert len(resultados) > 0, "No se encontraron resultados."

# Imprimir mensaje de éxito si se encontraron resultados
print("✅ Prueba funcional completada con éxito")

# Cerrar el navegador
driver.quit()