from shutil import (move, copy)


class Shutil:
    def mover_arquivo(self, archive, destination, obrigatory=True):
        if obrigatory:
            move(archive, destination)
        else:
            try:
                move(archive, destination)
            except:
                print("Não foi possível mover o arquivo.\n")

    def copiar_arquivo(self, archive, destination):
        copy(archive, destination)
