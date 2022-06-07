import pyautogui
import time


# libreria para controlar mouse y teclado
# https://pyautogui.readthedocs.io/en/latest/
import pyperclip


def main():
    # escribir en un excel a la mala
    screen_width, screen_height = pyautogui.size()  # obtenemos las dimensiones

    # vamos a hacer  click en el boton de windows
    # pyautogui.moveTo(50, screen_height - 50)  # Move the mouse to XY coordinates.
    # pyautogui.click()
    pyautogui.press("win")

    # poner algunos sleep para esperar a que ocurran las acciones
    time.sleep(3)

    # escribir la palabra excel -> entre cada tipeo, esperamos 0.25 segundos
    pyautogui.write("excel", interval=0.25)
    pyautogui.press("enter")

    # volvemos a esperar
    time.sleep(4.1)

    # seleccionamos el template de excel, por defecto debería ser en blanco
    pyautogui.press("enter")

    # aqui vamos a escribir en la primera celada
    pyautogui.write('holi')

    # nos movemos a la celda B2
    pyautogui.press(['down', 'right'])
    pyperclip.copy('(✿◡‿◡)')
    pyautogui.hotkey('ctrl', 'v')

    # nos movemos a la C3
    pyautogui.press(['down', 'right'])
    pyautogui.write('+1+3')
    pyautogui.press("enter")

    # ahora vamos a guardar el archivo
    pyautogui.hotkey('ctrl', 's')

    # volvemos a esperar un rato
    time.sleep(2.1)

    # escribimos el nombre del archivo
    pyautogui.write('este es mi curso favorito')

    # guardamos finalmente
    pyautogui.press("enter")

    pyautogui.alert('Terminamos el script.')


if __name__ == '__main__':
    main()
