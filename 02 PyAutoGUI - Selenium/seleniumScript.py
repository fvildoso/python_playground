import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

# take environment variables from .env.
load_dotenv()


def main():
    print("Inicio")
    print(os.getcwd())  # ruta de donde estamos corriendo el script

    # podemos setear opciones del browser
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.headless = False  # con esto podemos ocultar el browser

    # lista de drivers https://selenium-python.readthedocs.io/installation.html
    # llamamos al driver
    driver = webdriver.Firefox(service=Service('drivers/geckodriver.exe'))
    driver.implicitly_wait(10)

    # vamos a la pagina de ucursos
    driver.get("https://www.u-cursos.cl/")

    # buscamos donde hacer login
    elem = driver.find_element(By.CSS_SELECTOR, ".autofocus")
    elem.send_keys(os.getenv('UCURSOS_USER'))

    # buscamos donde poner el password
    elem = driver.find_element(By.CSS_SELECTOR, "#upform > form:nth-child(1) > dl:nth-child(7) > dd:nth-child(4) > "
                                                "input:nth-child(1)")
    elem.send_keys(os.getenv('UCURSOS_PASS'))

    # buscamos el botón para hacer submit
    elem = driver.find_element(By.CSS_SELECTOR, "input.boton:nth-child(6)")
    elem.click()

    # vamos a la pagina de integrantes
    driver.get("https://www.u-cursos.cl/ingenieria/2021/1/IN4535/1/integrantes/")

    # seleccionamos los elementos que nos pueden decir los nombres
    elems = driver.find_elements(By.CSS_SELECTOR, "td.string > h1 > a")

    print('Elementos encontrados: ' + str(len(elems)))
    nombres = []
    for elemento in elems:
        nombres.append(elemento.text)
        print(elemento.text)
    print(nombres)

    # buscamos los registros unicos
    unique_nombres = list(dict.fromkeys(nombres))
    print(unique_nombres)

    elem = driver.find_element(By.CSS_SELECTOR, 'a.file:nth-child(1)')
    elem.click()

    time.sleep(30)
    driver.close()


if __name__ == '__main__':
    main()
