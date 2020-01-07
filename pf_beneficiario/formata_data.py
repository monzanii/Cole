from datetime import datetime
from datetime import timedelta


class Formata_data:

    def __init__(self, data_ent  ):
        self.__data_ent = data_ent


    def current_data(self):
        return datetime.utcnow()

    def formata_data(self, dt_recebida):
        data_formatada = ('{:02d}'.format(dt_recebida.day) + ('{:02d}'.format(dt_recebida.month)) + ('{:04d}'.format(dt_recebida.year)))
        return data_formatada

    def data_do_vencimento(self, dt_recebida, qtd_dia):
        #intervalo = 5
        data_alterada = timedelta(qtd_dia) + (dt_recebida.today())
        return  data_alterada

    def construcao_nossnr_data_time(self):
        dtnossnr = datetime.utcnow()
        nossnr = (str(dtnossnr.day) + str(dtnossnr.month) + str(dtnossnr.minute) + str(dtnossnr.second))
        nossnr_full = "{:08d}".format(int(nossnr))
        return nossnr_full

