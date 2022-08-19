import os
import time
import random
import pyautogui
from colorama import (Fore, Style)


class Pyautogui:
    def colar(self):
        pyautogui.hotkey('ctrl', 'v')

    def copiar(self):
        pyautogui.hotkey('ctrl', 'c')

    def segurar_tecla(self, key: str):
        pyautogui.keyDown(key)

    def soltar_tecla(self, key: str):
        pyautogui.keyUp(key)

    def minimizar_todos_os_programas(self):
        pyautogui.hotkey('winleft', 'd')

    def obter_posicao_do_mouse(self, x=False, y=False):
        return pyautogui.position()

    def screenshot(self, image_name: str, left: int, top: int, width: int, height: int):
        pyautogui.screenshot(image_name, region=(int(left), int(top), int(width), int(height)))

    def alerta(self, text: str, title: str):
        alerta = pyautogui.alert(text=text, title=title)
        if alerta == 'OK':
            return True
        else:
            return False

    def confirm(self, text: str, buttons: list, title=None):
        dialog = pyautogui.confirm(text=text, title=title, buttons=buttons)
        if dialog is not None:
            for button in buttons:
                if dialog.lower() == button.lower():
                    return button
        else:
            return None

    def caixa_de_dialogo(self, text: str, title=None, default=None):
        dialog = str(pyautogui.prompt(text=text, title=title, default=default))
        if dialog != "None":
            return dialog
        else:
            return False

    def pressionar(self, key1, key2=None, presses: int = 1):
        for i in range(presses):
            if key2:
                pyautogui.hotkey(key1, key2)
            else:
                pyautogui.press(key1)

    def escrever(self, text: str, delay: float = 0, realist=False):
        if realist:
            for letra in text:
                pyautogui.write(letra)
                time.sleep(random.random() / delay)
        else:
            pyautogui.write(text)

    def esta_presente(self, image, loop: int = 50):
        img_name = image.split('\\')[-1]
        print(Fore.CYAN + 'Tentando encontrar "{}".'.format(img_name) + Style.RESET_ALL)
        for i in range(loop):
            try:
                button = pyautogui.locateCenterOnScreen(image, confidence=0.9)
                assert button is not None
                print(Fore.GREEN + '"{}" foi encontrada. Tentativas: {}.'.format(img_name, i + 1) + Style.RESET_ALL)
                return True
            except:
                loop -= 1
            if loop == 0:
                print(Fore.RED + '"{}" não pôde ser encontrada.'.format(img_name) + Style.RESET_ALL)
                return False

    def selecionar_todas_as_pastas_de(self, python_projects_folder: str, img_expand: str, img_select_all: str, img_move_to: str):
        # Abrir pasta
        self.minimizar_todos_os_programas()
        os.startfile(python_projects_folder)
        print('Pasta aberta.\n')

        # Selecionar todos os arquivos
        self.clickar(img_expand, time=5, confidense=False, obrigatory=False)
        self.clickar(img_select_all)
        assert self.esta_presente(img_move_to) is True
        print('Arquivos selecionados.\n')
        return 'Todas'

    def clickar_como_humano(self, image: str, right=False, confidense=True):
        loop = 10
        for i in range(loop):
            try:
                if confidense:
                    button = pyautogui.locateOnScreen(image, confidence=0.9)
                else:
                    button = pyautogui.locateOnScreen(image)
                assert button is not None
                if right:
                    pyautogui.rightClick(button[0] + random.randint(0, button[2]) / 1.5,
                                         button[1] + random.randint(0, button[3]) / 1.5)
                else:
                    pyautogui.click(button[0] + random.randint(0, button[2]) / 1.5,
                                    button[1] + random.randint(0, button[3]) / 1.5)
                break
            except:
                loop -= 1
            if loop == 0:
                print('Infelizmente não foi possivel clickar no botão especificado.\n')

    def clickar(self, image: str, need_click=True, right=False, time: int = 100, confidense=True, move=False, x: int = 0, y: int = 0, obrigatory=True):
        img_name = image.split('\\')[-1]
        print(Fore.CYAN + 'Tentando clickar em "{}"'.format(img_name) + Style.RESET_ALL)
        for i in range(time):
            try:
                if confidense:
                    button = pyautogui.locateCenterOnScreen(image, confidence=0.9)
                else:
                    button = pyautogui.locateCenterOnScreen(image)

                assert button is not None

                if move:
                    if need_click:
                        if right:
                            pyautogui.rightClick(button[0] + x, button[1] + y)
                            print(Fore.GREEN + 'Clickou com o botão direito em "{}". Tentativas: {}.'.format(img_name, i + 1) + Style.RESET_ALL)
                        else:
                            pyautogui.click(button[0] + x, button[1] + y)
                            print(Fore.GREEN + 'Clickou em "{}". Tentativas: {}.'.format(img_name, i + 1) + Style.RESET_ALL)
                    else:
                        pyautogui.moveTo(button[0] + x, button[1] + y)
                else:
                    if need_click:
                        if right:
                            pyautogui.rightClick(button)
                            print(Fore.GREEN + 'Clickou com o botão direito em "{}". Tentativas: {}.'.format(img_name, i + 1) + Style.RESET_ALL)
                        else:
                            pyautogui.click(button)
                            print(Fore.GREEN + 'Clickou em "{}". Tentativas: {}.'.format(img_name, i + 1) + Style.RESET_ALL)

                break
            except:
                time -= 1
            if time == 0:
                ...
                print(Fore.YELLOW + 'Não foi possivel clickar em "{}". Tentativas: {}.'.format(img_name, i + 1) + Style.RESET_ALL)

            if obrigatory:
                assert time > 0, '\nInfelizmente não foi possivel clickar em "{}". Tentativas: {}.\n'.format(img_name, i + 1)
