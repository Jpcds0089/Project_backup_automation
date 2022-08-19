from datetime import datetime


class Datetime:
    def obter_dia_da_semana(self):
        hoje = datetime.today()
        return hoje.strftime("%A")
