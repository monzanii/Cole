from pf_beneficiario import formata_data
from pf_beneficiario import trata_segmentos_arq240
from pf_beneficiario import trata_arq



class Monta_segQ_arq240:

    def __init__(self, key_trans):
        #self.__linha_seg_P = linha_seg_P
        self.__key_trans = key_trans


    def monta_linha_segQ(self, linha_seg_Q, qtd_reg ):
        pc_dados_seg_Q = self.__key_trans.consulta_conteudo_seg_Q(linha_seg_Q[3:18], qtd_reg, linha_seg_Q[18:48], linha_seg_Q[48:88], linha_seg_Q[88:103], linha_seg_Q[103:108], linha_seg_Q[108:111],
                                                                  linha_seg_Q[111:126], linha_seg_Q[126:128], linha_seg_Q[128:143], linha_seg_Q[143:173])

        listas_seg_Q = trata_arq.Trata_arq('seg_q', pc_dados_seg_Q)
        linha_str_seg_Q = listas_seg_Q.trata_linha_seg_q()
        return [linha_str_seg_Q]
