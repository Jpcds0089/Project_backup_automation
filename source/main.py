from time import sleep
from scripts.Os import Os
from os import getcwd, chdir
from scripts.Shutil import Shutil
from scripts.Winrar import Winrar
from scripts.Others import Others
from scripts.Datetime import Datetime
from scripts.Pyautogui import Pyautogui


# ------------------------------------------------------------------------------------------------------------#
# Init
# ------------------------------------------------------------------------------------------------------------#


class Backup:
    def __init__(self):
        print('Iniciando.\n')

        # Mudando para pasta raiz
        loc = getcwd()
        new_loc = loc.split('\\')
        chdir(loc.replace(fr'\{new_loc[-1]}', ''))

        # Definindo quem são os objetos
        self.os = Os()
        self.shitil = Shutil()
        self.winrar = Winrar()
        self.others = Others()
        self.datetime = Datetime()
        self.pyautogui = Pyautogui()

        # Definindo variaveis
        self.folders_for_compress = []
        self.user = self.os.obter_usuario()
        self.screenshot_name = 'folder.PNG'
        self.password = 'None'
        self.title_alert = 'Altomacão concluida'
        self.archive_name = r'PycharmProjects.rar'
        self.title = 'Podemos iniciar a altomacão?'
        self.title_write_box = 'Quais são as pastas?'
        self.text_alert = 'Altomacão concluida. Tenha um bom dia.'
        self.text_write_box = 'Quais as pastas que serão comprimidas?\nObs: Separar as pastas so com virgula(,)'
        self.text = 'Por favor, não ultilize seu computador enquanto estiver ocorrendo a altomacão. ' \
                    'Dito isso, podemos iniciar a altomacão?'
        self.text_dialog_box = 'Voce deseja fazer backup de todas as pastas ou de pastas especificas?'

        # Definindo localizacões de pastas
        self.pasta_das_imagens = r"./assets/img/"
        self.python_projects_folder = fr'C:\Users\{self.user}\PycharmProjects'
        self.one_driver_folder = fr'C:\Users\{self.user}\OneDrive\Python projects'
        self.locate_one_driver = fr'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\OneDrive.exe'

        # Definindo imagens
        self.img_ok = r'{}ok.PNG'.format(self.pasta_das_imagens)
        self.img_box = r'{}box.PNG'.format(self.pasta_das_imagens)
        self.img_name = r'{}name.PNG'.format(self.pasta_das_imagens)
        self.img_cancel = r'{}cancel.PNG'.format(self.pasta_das_imagens)
        self.img_expand = r'{}expand.PNG'.format(self.pasta_das_imagens)
        self.img_ok_blue = r'{}ok_blue.PNG'.format(self.pasta_das_imagens)
        self.img_move_to = r'{}move_to.PNG'.format(self.pasta_das_imagens)
        self.img_selected = r'{}selected.PNG'.format(self.pasta_das_imagens)
        self.img_show_password = r'{}show.PNG'.format(self.pasta_das_imagens)
        self.img_select_all = r'{}select_all.PNG'.format(self.pasta_das_imagens)
        self.img_select_none = r'{}select_none.PNG'.format(self.pasta_das_imagens)
        self.img_winrar_logo = r'{}winrar_logo.PNG'.format(self.pasta_das_imagens)
        self.img_set_password = r'{}set_password.PNG'.format(self.pasta_das_imagens)
        self.img_archive_name = r'{}archive_name.PNG'.format(self.pasta_das_imagens)
        self.img_enter_password = r'{}enter_password.PNG'.format(self.pasta_das_imagens)
        self.img_reenter_password = r'{}reenter_password.PNG'.format(self.pasta_das_imagens)
        self.img_add_to_archive = r'{}add_to_archive.PNG'.format(self.pasta_das_imagens)
        self.img_dictionary_size = r'{}dictionary_size.PNG'.format(self.pasta_das_imagens)
        self.img_compression_method = r'{}compression_method.PNG'.format(self.pasta_das_imagens)

    def obter_dia_da_semana(self):
        if self.datetime.obter_dia_da_semana() == 'Saturday' or self.datetime.obter_dia_da_semana() == 'sábado':
            return True
        else:
            return False

    def confirm(self):
        if self.pyautogui.confirm(self.text, title=self.title, buttons=['Ok', 'Cancel']) == 'Ok':
            return True
        else:
            return False

    def alerta(self):
        self.pyautogui.alerta(self.text_alert, self.title_alert)

    def caixa_de_escolha(self):
        options = self.pyautogui.confirm(text=self.text_dialog_box, title='Todas ou escolher alguma em especifica?', buttons=['Todas', 'Pastas especificas'])
        if options == 'Todas':
            return 'Todas'
        elif options == 'Pastas especificas':
            return 'Pastas especificas'
        else:
            return None

    def selecionar_pastas(self):
        options = self.caixa_de_escolha()
        # Se a escolha for "Todas". Selecionar todas as pastas.
        if options == 'Todas':
            self.pyautogui.selecionar_todas_as_pastas_de(self.python_projects_folder, self.img_expand, self.img_select_all, self.img_move_to)
            print('Opção escolhida: "Todas"\n')
            return True

        # Se a escolha for "Pastas especificas". Selecionar so as pastas passadas pela pessoa.
        elif options == 'Pastas especificas':
            print('Opção escolhida: "Pastas especificas"\n')
            # Escolher pastas
            if self.others.write_box(self.python_projects_folder, self.folders_for_compress, self.text_write_box, self.title_write_box) is not None:
                # Tirar foto das pastas escolhidas para obter localilacão delas mais adiante
                print('Nome das pastas:', self.folders_for_compress)
                assert len(self.folders_for_compress) != 0
                self.others.escolher_pasta(self.screenshot_name, self.img_name, self.folders_for_compress)

                # Minimizar todos os programas abertos
                self.pyautogui.minimizar_todos_os_programas()

                # Abrir localizacão das pastas que irão ser compactadas
                self.os.abrir(self.python_projects_folder)

                # Deselecionar todas as pastas
                self.pyautogui.clickar(self.img_expand, time=5, confidense=False, obrigatory=False)
                self.pyautogui.clickar(self.img_select_none, confidense=False)

                # Selecionar pastas que irão ser compactadas
                for arquivo in self.os.obter_arquivos_em(r'.\assets\img'):
                    self.pyautogui.segurar_tecla('ctrl')
                    #print(arquivo, f'Screenshot: {self.screenshot_name.replace(".PNG", "")}')
                    if self.screenshot_name.replace('.PNG', '') in arquivo:
                        #print(f'   {self.screenshot_name.replace(".PNG", "")} É igual a {arquivo}')
                        self.pyautogui.clickar(fr'.\assets\img\{arquivo}')
                self.pyautogui.soltar_tecla('ctrl')
                return 'Pastas especificas'
            else:
                pass
        else:
            return None

    def Start(self):
        self.abrir_winrar()
        self.config_winrar()
        self.esperar_comprimir()
        self.mover_arquivo()
        self.abrir_one_driver()

    def abrir_winrar(self):
        # Clickando com botão direito
        self.pyautogui.clickar(self.img_selected, right=True, confidense=False)

        # Clkickando em add to archive
        self.pyautogui.clickar(self.img_add_to_archive)

        # Minimizar programas
        self.pyautogui.minimizar_todos_os_programas()

        # Apertar em windows
        self.pyautogui.pressionar('Winleft')

        # Abrir winrar
        self.pyautogui.clickar(self.img_winrar_logo)
        print('\nWinRar aberto.\n')

    def config_winrar(self):
        # Nome do arquivo
        self.winrar.nome_do_arquivo(self.img_archive_name, self.archive_name)

        # Metodo de compressão
        self.winrar.metodo_de_compressao(self.img_compression_method, 'good')

        # Tamanho do dicionario
        self.winrar.tamanho_do_dicionario(self.img_dictionary_size)

        # Setar senha
        self.winrar.setar_senha(self.img_set_password, self.img_show_password, self.img_enter_password, self.img_reenter_password, self.img_box, self.password, self.img_ok)

        # Apertar em ok
        sleep(0.5)
        self.winrar.apertar_em_ok(self.img_ok)
        print('\nConfiguracõs do winrar completas.\n')

    def esperar_comprimir(self):
        self.winrar.esperar_comprimir(self.img_cancel)

    def mover_arquivo(self):
        self.os.remove(fr'{self.one_driver_folder}\{self.archive_name}', obrigatory=False)
        self.shitil.mover_arquivo(rf'{self.python_projects_folder}\{self.archive_name}', self.one_driver_folder)
        print('Aquivo movido.\n')

    def abrir_one_driver(self):
        self.pyautogui.pressionar("winleft", "s")
        sleep(0.25)
        self.pyautogui.escrever("OneDrive")
        sleep(0.25)
        self.pyautogui.pressionar("enter")
        print('OneDriver aberto.\n')


bot = Backup()
if bot.obter_dia_da_semana() is True:
    if bot.confirm() is True:
        if bot.selecionar_pastas() is not None:
            bot.Start()
            bot.alerta()
else:
    print('Hoje não e sabado. Finalizando.\n')
