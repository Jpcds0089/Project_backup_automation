import ctypes
from time import sleep
from scripts.Os import Os
from random import randint
from scripts.Shutil import Shutil
from scripts.Pyautogui import Pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as CondicaoExperada


class Others(Os, Shutil, Pyautogui):
    def obter_resolucao(self):
        user32 = ctypes.windll.user32
        return user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

    def criar_pastas_necessarias(self):
        self.criar_pasta(r'.\folder')
        self.criar_pasta(r'.\folder for del')

    def obter_e_mover_pastas(self, get_from_folder: str, move_for_folder: str):
        pastas_obtidas = self.obter_pastas_em(get_from_folder)
        if pastas_obtidas is not None:
            for pasta_obtida in pastas_obtidas:
                sorteio = randint(0, 1000000)
                self.rename(fr'{get_from_folder}\{pasta_obtida}', fr'{pasta_obtida}{sorteio}')
                self.mover_arquivo(fr'.\{pasta_obtida}{sorteio}', move_for_folder)

    def obter_e_mover_imagens(self, screenshot_name: str):
        for arquivo_obtido in self.obter_arquivos_em(r'.\data\img'):
            if screenshot_name.replace('.PNG', '') in arquivo_obtido:
                sorteio = randint(0, 1000000)
                self.rename(fr'.\data\img\{arquivo_obtido}', f'{arquivo_obtido.replace(".PNG", "")}{sorteio}.PNG')
                for image in self.obter_arquivos_em(r'.'):
                    if 'folder' in image:
                        self.mover_arquivo(image, r'.\folder for del')

    def escolher_pasta(self, screenshot_name: str, img: str, names_folders: list):
        # Criando pastas necesarias
        self.criar_pastas_necessarias()

        # Obter imagens e move-las para a pasta folder for del
        self.obter_e_mover_imagens(screenshot_name)

        # Criando pastas e tirando screenshots de cada uma
        count = 0
        self.abrir(r'.\folder')
        for name_folder in names_folders:
            # Obter e mover pastas obtidas para a pasta folder for del
            self.obter_e_mover_pastas(r'.\folder', r'.\folder for del')

            # Criar pastas
            self.criar_pasta(fr'.\folder\{name_folder}')
            sleep(0.5)

            # Tirar screenshot da pasta
            count += 1
            self.clickar(img, need_click=False, move=True, x=-40, y=18)
            self.screenshot(fr'{screenshot_name.replace(".PNG", "")}{count}.PNG',
                            self.obter_posicao_do_mouse()[0],
                            self.obter_posicao_do_mouse()[1], 150, 20)

            # Mover imagem para a pasta data
            self.mover_arquivo(fr'{screenshot_name.replace(".PNG", "")}{count}.PNG', r'.\data\img')

    def write_box(self, python_projects_folder: str, folders_for_compress: list, text_write_box: str, title_write_box: str):
        while True:
            # Retorna nome das pastas que a pessoa escreveu
            obtained_folders = self.caixa_de_dialogo(text_write_box, title_write_box)

            if obtained_folders is not None:
                # Para cada pasta obtida que a pessoa escreveu
                for obtained_folder in obtained_folders:

                    # E para cada pasta existente em "python_projects_folder"
                    for folder_existing in self.obter_pastas_em(python_projects_folder):

                        # Se a pasta que a pessoa escreveu existir em "python_projects_folder"
                        if obtained_folder.lower().replace(' ', '') in folder_existing.lower().replace(' ', ''):
                            # Adicionar ela na lista de pastas para compactar
                            folders_for_compress.append(folder_existing)

                # Se todas as pastas que a pessoa mandou compactar existir
                if len(obtained_folders) == len(folders_for_compress):

                    # Parar o loop porque o objetivo foi conluido
                    return folders_for_compress

                # Caso nem todas as pastas existir pedir para a pessoa escrever novamente
                else:
                    folders_for_compress.clear()

                    # Se as pastas passadas pela pessoa for maior que uma.
                    if len(obtained_folders) > 1:
                        title_write_box = 'Alguma das pastas escolhidas não existe'
                        text_write_box = 'Alguma das pastas escolhidas não existe. Por favor digite novamente as ' \
                                         'pastas que serão comprimidas.\nObs: Separar as pastas so com virgula(,)'

                    # Caso so for ima.
                    else:
                        title_write_box = 'A pasta escolhida não existe'
                        text_write_box = 'A pasta escolhida não existe. Por favor digite novamente a pasta que ' \
                                         'sera comprimida.\nObs: Separar as pastas so com virgula(,)'
            else:
                return None

    def download_extension_logic(self, driver, waint, url, adicionar_img, ok_img, config=None, aceito_img=None):
        # Instalando extencão
        driver.get(url)
        loc_button = (By.CSS_SELECTOR, 'a[class="Button Button--action AMInstallButton-button Button--puffy"]')
        button = waint.until(CondicaoExperada.element_to_be_clickable(loc_button))
        button.click()

        # Apertando em adicionar
        self.clickar(adicionar_img)

        # Config
        if config == 'sim':
            self.clickar(aceito_img)
            self.pressionar('alt', 'f4')
        # Apertando em ok
        self.clickar(ok_img, obrigatory=False)

