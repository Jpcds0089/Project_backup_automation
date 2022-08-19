import os
import locale
import shutil
import pyautogui
from time import sleep
from datetime import datetime


def GetDiaDaSemana():
    global dia
    dia_prun = 'Saturday'
    dia_prun1 = 'sábado'
    locale.setlocale(locale.LC_ALL, '')

    hoje = datetime.today()

    dia_da_semana = hoje.strftime("%A")

    if dia_da_semana == dia_prun or dia_da_semana == dia_prun1:
        dia = True
        print(dia_da_semana)
    else:
        print(dia_da_semana)
        dia = False


def click_with_pyautogui(nome_imagem:str):
    count = 0
    in_loop = True
    while in_loop:
        sleep(0.5)
        loc_buttton = pyautogui.locateCenterOnScreen(nome_imagem, confidence=0.9)
        if loc_buttton is None:
            count += 1
            if count > 20:
                print('Erro: Botão não encontrado. Encerrando programa.')
                in_loop = False
        else:
            pyautogui.click(loc_buttton)
            in_loop = False


if __name__ == "__main__":
    GetDiaDaSemana()


if dia:
    close = False
    message = 'Atencão: Por Favor Não Ultilize Seu Computador Enquanto A Altomacão Estiver "In_Running".\n\nDito Isso, Podemos Iniciar A Altomacão?'
    attention_window = pyautogui.confirm(message)
    if attention_window == 'Cancel':
        close = True
    if not close:


        class Nome:

            def __init__(self):
                global in_loop, in_loop1, in_loop2, in_loop3, in_loop4, in_loop5, in_loop6, locate, locate_onedriver, \
                    destination, source, locate_one_driver
                pyautogui.PAUSE = 0.5
                print("\nIniciando altomacão\n")
                user = os.getenv('USERNAME')
                locate = rf'C:\Users\{user}\PycharmProjects'
                source = rf'C:\Users\{user}\PycharmProjects\PycharmProjects.rar'
                destination = rf'C:\Users\{user}\OneDrive\Python projects\PycharmProjects.rar'
                locate_one_driver = rf'C:\Users\{user}\AppData\Local\Microsoft\OneDrive\OneDrive.exe'
                in_loop = True
                in_loop1 = True
                in_loop2 = True
                in_loop3 = True
                in_loop4 = True
                in_loop5 = True

            def Start(self):
                self.OpenLocFile()
                self.DelFile()
                self.SelectAllAndOpenWinrar()
                self.ConfigNewFile()
                self.SetPasswordInNewFile()
                self.ClickOk()
                self.CopyFileAndPastFile()
                self.OpenOneDriver()

            def OpenOneDriver(self):
                os.startfile(locate_one_driver)

            def OpenLocFile(self):
                os.startfile(locate)

            def DelFile(self):
                global in_loop
                clock = 0
                while in_loop:
                    clock += 1
                    img = r'./data/projects.png'
                    loc = pyautogui.locateCenterOnScreen(img, confidence=0.9)
                    if loc is None:
                        if clock == 5:
                            in_loop = False
                    else:
                        pyautogui.click(loc)
                        pyautogui.press('del')
                        in_loop = False

            def SelectAllAndOpenWinrar(self):
                pyautogui.hotkey('ctrl', 'a')
                global in_loop1
                while in_loop1:
                    img = r'./data/dir.png'
                    loc = pyautogui.locateCenterOnScreen(img, confidence=0.9)
                    if loc is None:
                        pass
                    else:
                        pyautogui.rightClick(loc)
                        in_loop1 = False

                in_loop1 = True
                while in_loop1:
                    img = r'./data/add.png'
                    loc = pyautogui.locateCenterOnScreen(img, confidence=0.9)
                    if loc is None:
                        pass
                    else:
                        pyautogui.click(loc)
                        in_loop1 = False

            def ConfigNewFile(self):
                global in_loop2
                pyautogui.press('backspace')
                pyautogui.write('PycharmProjects.rar')
                while in_loop2:
                    img = r'./data/normal.png'
                    loc = pyautogui.locateCenterOnScreen(img, confidence=0.9)
                    if loc is None:
                        pass
                    else:
                        pyautogui.click(loc)
                        pyautogui.press('down', presses=2)
                        pyautogui.press('enter')
                        pyautogui.press('tab')
                        pyautogui.press('down', presses=6)
                        in_loop2 = False

            def SetPasswordInNewFile(self):
                global in_loop3
                senha = 'senha'
                while in_loop3:
                    img = r'./data/set.png'
                    loc = pyautogui.locateCenterOnScreen(img, confidence=0.9)
                    if loc is None:
                        pass
                    else:
                        pyautogui.click(loc)
                        pyautogui.write(senha)
                        in_loop3 = False

                in_loop3 = True
                while in_loop3:
                    img = r'./data/box.png'
                    loc = pyautogui.locateCenterOnScreen(img, confidence=0.9)
                    if loc is None:
                        pass
                    else:
                        pyautogui.click(loc)
                        in_loop3 = False

                in_loop3 = True
                while in_loop3:
                    img = r'./data/ok.png'
                    loc = pyautogui.locateCenterOnScreen(img, confidence=0.9)
                    if loc is None:
                        pass
                    else:
                        pyautogui.click(loc)
                        in_loop3 = False

                # Repet
                pyautogui.press('enter')
                pyautogui.write(senha)

                in_loop3 = True
                while in_loop3:
                    img = r'./data/ok.png'
                    loc = pyautogui.locateCenterOnScreen(img, confidence=0.9)
                    if loc is None:
                        pass
                    else:
                        pyautogui.click(loc)
                        in_loop3 = False

            def ClickOk(self):
                global in_loop4
                while in_loop4:
                    img = r'./data/ok.png'
                    loc = pyautogui.locateCenterOnScreen(img, confidence=0.9)
                    if loc is None:
                        pass
                    else:
                        pyautogui.click(loc)
                        print('compactando')
                        in_loop4 = False

            def CopyFileAndPastFile(self):
                sleep(1)
                print('copiando')
                shutil.move(source, destination)
                print('colado')


        bot = Nome()
        bot.Start()
        message1 = "A Altomacão Acabou De Ser Finalizada. Tenha Um Bom Dia."
        pyautogui.alert(message1)
