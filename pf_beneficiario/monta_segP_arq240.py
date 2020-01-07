from pf_beneficiario import formata_data
from pf_beneficiario import trata_segmentos_arq240
from pf_beneficiario import trata_arq



class Monta_segP_arq240:

    def __init__(self, key_trans):
        #self.__linha_seg_P = linha_seg_P
        self.__key_trans = key_trans


    def monta_linha_segP(self, linha_seg_P, qtd_reg ):
        pc_dados_seg_P = self.__key_trans.consulta_conteudo_seg_P(linha_seg_P[3:6], qtd_reg,  linha_seg_P[6:10], linha_seg_P[10:15],
                                                           linha_seg_P[15:16], linha_seg_P[16:24], linha_seg_P[24:25],
                                                           linha_seg_P[25:33], linha_seg_P[33:48], linha_seg_P[48:56], linha_seg_P[56:64],
                                                           linha_seg_P[64:65])

        listas_seg_p = trata_arq.Trata_arq('seg_p', pc_dados_seg_P)
        linha_str_seg_P = listas_seg_p.trata_linha_seg_p()
        return [linha_str_seg_P]
