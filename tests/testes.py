import os
import time
import shutil
import random
import pyautogui
from time import sleep
from datetime import datetime


# ------------------------------------------------------------------------------------------------------------#
# Functions
# ------------------------------------------------------------------------------------------------------------#


# Obter dia da semana


def obter_dia_da_semana():
    hoje = datetime.today()
    return hoje.strftime("%A")


# Os


def abrir(directory: str):
    os.startfile(directory)


def criar_pastas(directory: str):
    os.makedirs(directory)


def ir_para(directory: str):
    os.chdir(directory)
    return os.getcwd()


def obter_usuario():
    return os.getenv('USERNAME')


def remove(archive: str):
    os.remove(archive)


def rename(name_beforce, name_after):
    os.rename(name_beforce, name_after)


def criar_pasta(directory: str):
    try:
        os.mkdir(directory)
    except:
        pass


def obter_arquivos_em(directory: str):
    for root, dirs, files in os.walk(directory):
        return files


def obter_pastas_em(directory: str):
    for root, dirs, files in os.walk(directory):
        return dirs


def obter_caminhos_em(directory: str):
    for root, dirs, files in os.walk(directory):
        return root


def obter_caminhos_e_arquivos_em(directory: str):
    roots_and_files = []
    for root, dirs, files in os.walk(directory):
        roots_and_files.append(root)
        roots_and_files.append(files)
    return roots_and_files


def obter_pastas_escolhidas(directory: str, chosen_folders):
    folders_oltputs = obter_pastas_em(directory)
    folders_for_select = []
    for folder_oltput in folders_oltputs:
        for folder_input in chosen_folders:
            if folder_oltput.lower().replace(' ', '') == folder_input.lower().replace(' ', ''):
                folders_for_select.append(folder_oltput)
    return folders_for_select


# Pyautogui


def colar():
    pyautogui.hotkey('ctrl', 'v')


def copiar():
    pyautogui.hotkey('ctrl', 'c')


def segurar_tecla(key: str):
    pyautogui.keyDown(key)


def soltar_tecla(key: str):
    pyautogui.keyUp(key)


def minimizar_todos_os_programas():
    pyautogui.hotkey('winleft', 'd')


def obter_posicao_do_mouse(x=False, y=False):
    return pyautogui.position()


def screenshot(image_name: str, left: int, top: int, width: int, height: int):
    pyautogui.screenshot(image_name, region=(int(left), int(top), int(width), int(height)))


def alerta(text: str, title: str):
    alerta = pyautogui.alert(text=text, title=title)
    if alerta == 'OK':
        return True
    else:
        return False


def confirm(text: str, buttons: list, title=None):
    dialog = pyautogui.confirm(text=text, title=title, buttons=buttons)
    if dialog is not None:
        for button in buttons:
            if dialog.lower() == button.lower():
                return button
    else:
        return None


def caixa_de_dialogo(text: str, title=None):
    dialog = [pyautogui.prompt(text=text, title=title)]
    if str(dialog[0]) != 'None':
        splited_dialog = str(dialog[0]).split(',')
        return splited_dialog
    else:
        return None


def pressionar(key1, key2=None, presses: int = 1):
    for i in range(presses):
        if key2:
            pyautogui.hotkey(key1, key2)
        else:
            pyautogui.press(key1)


def escrever(text: str, time: float = 0, realist=False):
    if realist:
        for letra in text:
            pyautogui.write(letra)
            sleep(random.random() / time)
    else:
        pyautogui.write(text)


def is_present(image):
    loop = 10
    for i in range(loop):
        try:
            button = pyautogui.locateCenterOnScreen(image, confidence=0.9)
            assert button is not None
            return True
        except:
            loop -= 1
        if loop == 0:
            return False


def selecionar_todas_as_pastas_de(python_projects_folder: str, img_expand: str, img_select_all: str, img_move_to: str):
    # Abrir pasta
    minimizar_todos_os_programas()
    os.startfile(python_projects_folder)
    print('Pasta aberta.\n')

    # Selecionar todos os arquivos
    clickar(img_expand, time=5, confidense=False)
    clickar(img_select_all)

    assert is_present(img_move_to) is True
    print('Arquivos selecionados.\n')
    return 'Todas'


def clickar_como_humano(image: str, right=False, confidense=True):
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


def clickar(image: str, need_click=True, right=False, time: int = 20, confidense=True, move=False,
            x: int = 0, y: int = 0):
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
                        return 'Clickou'
                    else:
                        pyautogui.click(button[0] + x, button[1] + y)
                        return 'Clickou'
                else:
                    pyautogui.moveTo(button[0] + x, button[1] + y)
                    return 'Clickou'
            else:
                if need_click:
                    if right:
                        pyautogui.rightClick(button)
                        return 'Clickou'
                    else:
                        pyautogui.click(button)
                        return 'Clickou'
            break
        except:
            time -= 1
        if time == 0:
            print('Infelizmente não foi possivel clickar no botão especificado.\n')
            return None


# Escolha


def criar_pastas_necessarias():
    criar_pasta(r'.\folder')
    criar_pasta(r'.\folder for del')


def obter_e_mover_pastas(get_from_folder: str, move_for_folder: str):
    pastas_obtidas = obter_pastas_em(get_from_folder)
    if pastas_obtidas is not None:
        for pasta_obtida in pastas_obtidas:
            sorteio = random.randint(0, 1000000)
            rename(fr'{get_from_folder}\{pasta_obtida}', fr'{pasta_obtida}{sorteio}')
            mover_arquivo(fr'.\{pasta_obtida}{sorteio}', move_for_folder)


def obter_e_mover_imagens(screenshot_name: str):
    for arquivo_obtido in obter_arquivos_em(r'.\data'):
        if screenshot_name.replace('.PNG', '') in arquivo_obtido:
            sorteio = random.randint(0, 1000000)
            rename(fr'.\data\{arquivo_obtido}', f'{arquivo_obtido.replace(".PNG", "")}{sorteio}.PNG')
            for image in obter_arquivos_em(r'.'):
                if 'folder' in image:
                    mover_arquivo(image, r'.\folder for del')


def escolher_pasta(screenshot_name: str, img: str, names_folders: list):
    # Criando pastas necesarias
    criar_pastas_necessarias()

    # Obter imagens e move-las para a pasta folder for del
    obter_e_mover_imagens(screenshot_name)

    # Criando pastas e tirando screenshots de cada uma
    count = 0
    abrir(r'.\folder')
    for name_folder in names_folders:
        # Obter e mover pastas obtidas para a pasta folder for del
        obter_e_mover_pastas(r'.\folder', r'.\folder for del')

        # Criar pastas
        criar_pasta(fr'.\folder\{name_folder}')
        time.sleep(0.5)

        # Tirar screenshot da pasta
        count += 1
        clickar(img, need_click=False, move=True, x=-40, y=18)
        screenshot(fr'{screenshot_name.replace(".PNG", "")}{count}.PNG',
                   obter_posicao_do_mouse()[0],
                   obter_posicao_do_mouse()[1], 150, 20)

        # Mover imagem para a pasta data
        mover_arquivo(fr'{screenshot_name.replace(".PNG", "")}{count}.PNG', r'.\data')


# Caixa de escrita


def write_box(python_projects_folder: str, folders_for_compress: list, text_write_box: str, title_write_box: str):
    while True:
        # Retorna nome das pastas que a pessoa escreveu
        obtained_folders = caixa_de_dialogo(text_write_box, title_write_box)

        if obtained_folders is not None:
            # Para cada pasta obtida que a pessoa escreveu
            for obtained_folder in obtained_folders:

                # E para cada pasta existente em "python_projects_folder"
                for folder_existing in obter_pastas_em(python_projects_folder):

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


# WinRar


def nome_do_arquivo(image: str, name: str):
    clickar(image, move=True, y=20)
    pressionar('ctrl', 'a')
    pressionar('backspace')
    escrever(name)


def metodo_de_compressao(image: str, metodo_name: str):
    clickar(image, move=True, y=20)
    pressionar('up', presses=5)
    metodos_names = ['store', 'fastest', 'fast', 'normal', 'good', 'best']
    count = 0
    for metodo in metodos_names:
        count += 1
        if metodo_name.lower() == metodo.lower():
            pressionar('enter')
            break
        pressionar('down')
        if count == 6:
            print('Por favor escolha uma das seguintes opcões: store, fastest, fast, normal, good ou best.\n')


def tamanho_do_dicionario(image: str):
    clickar(image, move=True, y=20)
    pressionar('down', presses=11)
    pressionar('enter')


def setar_senha(set_password: str, show_password: str, enter_password: str, reenter_password: str, box: str, password: str, ok: str):
    clickar(set_password)

    clickar(show_password, time=3, confidense=False)
    clickar(enter_password, move=True, y=20)
    escrever(password)
    clickar(reenter_password, move=True, y=20)
    escrever(password)
    clickar(box, time=5)

    clickar(ok)


def apertar_em_ok(image: str):
    clickar(image)


def esperar_comprimir(image: str):
    print('Esperando comprimir arquivo.\n')
    while True:
        if is_present(image) is True:
            pass
        else:
            print('Arquivo comprimido.\n')
            break
        time.sleep(5)


# Shutil


def mover_arquivo(archive, destination):
    shutil.move(archive, destination)


def copiar_arquivo(archive, destination):
    shutil.copy(archive, destination)


# Others


def get_week_day():
    if obter_dia_da_semana() == 'Saturday' or obter_dia_da_semana() == 'sábado':
        return True
    else:
        return False


def confirmar():
    if pyautogui.confirm(text, title=title, buttons=['Ok', 'Cancel']) == 'Ok':
        return True
    else:
        return False


def alert():
    alerta(text_alert, title_alert)


def caixa_de_escolha():
    dialog = pyautogui.confirm(text=text_dialog_box, title='Todas ou escolher alguma em especifica?', buttons=['Todas', 'Pastas especificas'])
    if dialog == 'Todas':
        return 'Todas'
    elif dialog == 'Pastas especificas':
        return 'Pastas especificas'
    else:
        return None


# ------------------------------------------------------------------------------------------------------------#
# Variables
# ------------------------------------------------------------------------------------------------------------#


print('Iniciando.\n')

# Mudando para pasta raiz
loc = os.getcwd()
new_loc = loc.split('\\')
os.chdir(loc.replace(fr'\{new_loc[-1]}', ''))

# Definindo variaveis
folders_for_compress = []
user = obter_usuario()
screenshot_name = 'folder.PNG'
password = 'None'
title_alert = 'Altomacão concluida'
archive_name = r'PycharmProjectsTeste.rar'
title = 'Podemos iniciar a altomacão?'
title_write_box = 'Quais são as pastas?'
text_alert = 'Altomacão concluida. Tenha um bom dia.'
text_write_box = 'Quais as pastas que serão comprimidas?\nObs: Separar as pastas so com virgula(,)'
text = 'Por favor, não ultilize seu computador enquanto estiver ocorrendo a altomacão. ' \
            'Dito isso, podemos iniciar a altomacão?'
text_dialog_box = 'Voce deseja fazer backup de todas as pastas ou de pastas especificas?'

# Definindo localizacões de pastas
python_projects_folder = fr'C:\Users\{user}\PycharmProjects'
one_driver_folder = fr'C:\Users\{user}\OneDrive\Python projects'
locate_one_driver = fr'C:\Users\{user}\AppData\Local\Microsoft\OneDrive\OneDrive.exe'

# Definindo imagens
image_folder = r'.\data\img'
img_ok = r'{}/ok.PNG'.format(image_folder)
img_box = r'{}/box.PNG'.format(image_folder)
img_name = r'{}/name.PNG'.format(image_folder)
img_cancel = r'{}/cancel.PNG'.format(image_folder)
img_expand = r'{}/expand.PNG'.format(image_folder)
img_ok_blue = r'{}/ok_blue.PNG'.format(image_folder)
img_move_to = r'{}/move_to.PNG'.format(image_folder)
img_selected = r'{}/selected.PNG'.format(image_folder)
img_show_password = r'{}/show.PNG'.format(image_folder)
img_select_all = r'{}/select_all.PNG'.format(image_folder)
img_winrar_logo = r'{}/winrar_logo.PNG'.format(image_folder)
img_set_password = r'{}/set_password.PNG'.format(image_folder)
img_archive_name = r'{}/archive_name.PNG'.format(image_folder)
img_enter_password = r'{}/enter_password.PNG'.format(image_folder)
img_reenter_password = r'{}/reenter_password.PNG'.format(image_folder)
img_add_to_archive = r'{}/add_to_archive.PNG'.format(image_folder)
img_dictionary_size = r'{}/dictionary_size.PNG'.format(image_folder)
img_compression_method = r'{}/compression_method.PNG'.format(image_folder)


# ------------------------------------------------------------------------------------------------------------#
# Source
# ------------------------------------------------------------------------------------------------------------#


def Start():
    abrir_winrar()
    config_winrar()
    waint_compress()
    move_file()
    abrir_one_driver()


def selecionar_pastas():
    dialog = caixa_de_escolha()
    # Se a escolha for "Todas". Selecionar todas as pastas.
    if dialog == 'Todas':
        selecionar_todas_as_pastas_de(python_projects_folder, img_expand, img_select_all,
                                                     img_move_to)
        print('Escolha: "Todas"')
        return True

    # Se a escolha for "Pastas especificas". Selecionar so as pastas passadas pela pessoa.
    elif dialog == 'Pastas especificas':
        print('Escolha: "Pastas especificas"\n')
        # Escolher pastas
        if write_box(python_projects_folder, folders_for_compress, text_write_box,
                                 title_write_box) is not None:
            # Tirar foto das pastas escolhidas para obter localilacão delas mais adiante
            print('Folders name:', folders_for_compress)
            assert len(folders_for_compress) != 0
            escolher_pasta(screenshot_name, img_name, folders_for_compress)

            # Minimizar todos os programas abertos
            minimizar_todos_os_programas()

            # Abrir localizacão das pastas que irão ser compactadas
            abrir(python_projects_folder)


            # Selecionar pastas que irão ser compactadas
            for arquivo in obter_arquivos_em(r'.\data'):
                segurar_tecla('ctrl')
                print(arquivo, f'Screenshot: {screenshot_name.replace(".PNG", "")}')
                if screenshot_name.replace('.PNG', '') in arquivo:
                    print(f'{screenshot_name.replace(".PNG", "")} E igual a {arquivo}')
                    clickar(fr'.\data\{arquivo}')
            soltar_tecla('ctrl')
            return 'Pastas especificas'
        else:
            pass
    else:
        return None


def abrir_winrar():
    # Clickando com botão direito
    assert_message = 'Não foi possivel apertar na pasta.'
    assert clickar(img_selected, right=True, confidense=False) is not None, assert_message

    # Clkickando em add to archive
    clickar(img_add_to_archive)

    # Minimizar programas
    minimizar_todos_os_programas()

    # Apertar em windows
    pressionar('Winleft')

    # Abrir winrar
    clickar(img_winrar_logo)
    print('WinRar aberto.\n')


def config_winrar():
    # Nome do arquivo
    nome_do_arquivo(img_archive_name, archive_name)

    # Metodo de compressão
    metodo_de_compressao(img_compression_method, 'good')

    # Tamanho do dicionario
    tamanho_do_dicionario(img_dictionary_size)

    # Setar senha
    setar_senha(img_set_password, img_show_password, img_enter_password,
                            img_reenter_password, img_box, password, img_ok)

    # Apertar em ok
    sleep(0.5)
    apertar_em_ok(img_ok)
    print('Configuracõs do winrar completas.\n')


def waint_compress():
    esperar_comprimir(img_cancel)


def move_file():
    copiar_arquivo(rf'{python_projects_folder}\{archive_name}', one_driver_folder)
    os.remove(fr'{python_projects_folder}\{archive_name}')
    print('Aquivo movido.\n')


def abrir_one_driver():
    abrir(locate_one_driver)
    print('OneDriver aberto.\n')


# ------------------------------------------------------------------------------------------------------------#
# Init
# ------------------------------------------------------------------------------------------------------------#


if get_week_day() is False:
    if confirmar() is True:
        if selecionar_pastas() is not None:
            Start()
            alert()
else:
    print('Hoje não e sabado. Finalizando.\n')
