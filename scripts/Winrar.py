from time import sleep
from scripts.Pyautogui import Pyautogui


class Winrar(Pyautogui):
    def nome_do_arquivo(self, image: str, name: str):
        self.clickar(image, move=True, y=20)
        self.pressionar('ctrl', 'a')
        self.pressionar('backspace')
        self.escrever(name)

    def metodo_de_compressao(self, image: str, metodo_name: str):
        self.clickar(image, move=True, y=20)
        self.pressionar('up', presses=5)
        metodos_names = ['store', 'fastest', 'fast', 'normal', 'good', 'best']
        count = 0
        for metodo in metodos_names:
            count += 1
            if metodo_name.lower() == metodo.lower():
                self.pressionar('enter')
                break
            self.pressionar('down')
            if count == 6:
                print('Por favor escolha uma das seguintes opcões: store, fastest, fast, normal, good ou best.\n')

    def tamanho_do_dicionario(self, image: str):
        self.clickar(image, move=True, y=20)
        self.pressionar('down', presses=11)
        self.pressionar('enter')

    def setar_senha(self, set_password: str, show_password: str, enter_password: str, reenter_password: str, box: str,
                    password: str, ok: str):
        self.clickar(set_password)

        self.clickar(show_password, time=3, confidense=False, obrigatory=False)
        self.clickar(enter_password, move=True, y=20)
        self.escrever(password)
        self.clickar(reenter_password, move=True, y=20)
        self.escrever(password)
        self.clickar(box, time=5)

        self.clickar(ok)

    def apertar_em_ok(self, image: str):
        self.clickar(image)

    def esperar_comprimir(self, image: str):
        print('Esperando comprimir arquivo.\n')
        while True:
            if self.esta_presente(image) is True:
                pass
            else:
                print('\nArquivo comprimido.\n')
                break
            sleep(5)
