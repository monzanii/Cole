from pf_beneficiario import formata_data
from pf_beneficiario import trata_segmentos_arq240
from pf_beneficiario import trata_arq



class Monta_headarq_arq240:

    def __init__(self, linha, key_trans):
        self.__linha = linha
        self.__key_trans = key_trans


    def monta_linha_headarq(self):
        ###########
        # INCLUSAO MOCK HEADARQ
        # alterar aqui para que o primeiro campo seja o conteudo que nao seja fixo
        pc_dados_beneficiario = self.__key_trans.consulta_conteudo_head_arq(self.__linha[0:3], self.__linha[91:99])
            #self.__linha[3:6], self.__linha[6:7], self.__linha[7:21], self.__linha[21:25],
            #                                                                self.__linha[25:30], self.__linha[30:31], self.__linha[31:61], self.__linha[61:91],
            #                                                                self.__linha[91:99])

        dados_head = trata_arq.Trata_arq('head_arq', pc_dados_beneficiario)

        print("pc_dados_beneficiario")
        print(pc_dados_beneficiario)

        retlinha_str_headarq = dados_head.trata_linha_head_arq()

        print("retlinha_str_headarq")
        print(retlinha_str_headarq)
        return [retlinha_str_headarq]


    def monta_linha_headlote(self):

        ###########
        # INCLUSAO MOCK HEADLOTE

        pc_dados_beneficiario_headlote = self.__key_trans.consulta_conteudo_head_lote(self.__linha[0:3], self.__linha[31:61], self.__linha[91:99])
        #self.__linha[3:6], self.__linha[6:7], self.__linha[7:21],
        #self.__linha[21:25], self.__linha[25:30], self.__linha[30:31],
        #self.__linha[31:61], ' ', self.__linha[91:99])

        listas_head_lote = trata_arq.Trata_arq('head_arq_lote', pc_dados_beneficiario_headlote)
        linha_str_headlote = listas_head_lote.trata_linha_head_lote()
        return [linha_str_headlote]