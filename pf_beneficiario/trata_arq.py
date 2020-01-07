from monta_arq240 import layout_head_arq240
from monta_arq240 import layout_head_lote240
from monta_arq240 import layout_seg_P_arq240
from monta_arq240 import layout_seg_Q_arq240
from monta_arq240 import layout_trailer_lote_arq240
from monta_arq240 import layout_trailer_arq240
from monta_arq240 import trata_campos_arq



class Trata_arq:

    def __init__(self, tp_linha_arq ,  conteudo_variavel_entrada ):
                self.__tp_linha_arq = tp_linha_arq
                self.__conteudo_variavel_entrada = conteudo_variavel_entrada


###########
    #INCLUSAO MOCK HEADARQ

    #def trata_linha_arq240(self):
    #    listas_de_layout = trata_campos_arq.Trata_campos_arq(self.__conteudo_fixo, self.__tamanho_campos, self.__list_campos)
    #    linha_list = listas_de_layout.preenche_conteudo_campos(self.__conteudo_variavel_entrada)
    #    return  "".join(linha_list)

#INCLUSAO MOCK HEADLOTE

    def trata_linha_head_arq(self):
        listas_de_layout_head_arq240 = trata_campos_arq.Trata_campos_arq(layout_head_arq240.Monta_head_arq240.conteudo_fixo(),
                                                                         layout_head_arq240.Monta_head_arq240.tamanho_campos(),
                                                                         layout_head_arq240.Monta_head_arq240.list_campos_head())
        return "".join(listas_de_layout_head_arq240.preenche_conteudo_campos(self.__conteudo_variavel_entrada))

    def trata_linha_head_lote(self):
        listas_de_layout_head_lote = trata_campos_arq.Trata_campos_arq(layout_head_lote240.Head_lote_arq240.conteudo_fixo(),
                                                                       layout_head_lote240.Head_lote_arq240.tamanho_campos(),
                                                                       layout_head_lote240.Head_lote_arq240.list_campos_head())
        return "".join(listas_de_layout_head_lote.preenche_conteudo_campos(self.__conteudo_variavel_entrada))

    def trata_linha_seg_p(self):
        listas_de_layout_seq_p = trata_campos_arq.Trata_campos_arq(layout_seg_P_arq240.Layout_seg_P_arq240.conteudo_fixo(),
                                                                       layout_seg_P_arq240.Layout_seg_P_arq240.tamanho_campos(),
                                                                       layout_seg_P_arq240.Layout_seg_P_arq240.list_campos_head()
                                                                       )
        return "".join(listas_de_layout_seq_p.preenche_conteudo_campos(self.__conteudo_variavel_entrada))

    def trata_linha_seg_q(self):
        listas_de_layout_seq_q = trata_campos_arq.Trata_campos_arq(layout_seg_Q_arq240.Layout_seg_Q_arq240.conteudo_fixo(),
                                                                   layout_seg_Q_arq240.Layout_seg_Q_arq240.tamanho_campos(),
                                                                   layout_seg_Q_arq240.Layout_seg_Q_arq240.list_campos_head()
                                                                   )
        return "".join(listas_de_layout_seq_q.preenche_conteudo_campos(self.__conteudo_variavel_entrada))

    def trata_linha_trailer_lote(self):
        listas_de_layout_trailer_lote = trata_campos_arq.Trata_campos_arq(layout_trailer_lote_arq240.Layout_trailer_lote_arq240.conteudo_fixo(),
                                                                          layout_trailer_lote_arq240.Layout_trailer_lote_arq240.tamanho_campos(),
                                                                          layout_trailer_lote_arq240.Layout_trailer_lote_arq240.list_campos_head(),
                                                                          )
        return "".join(listas_de_layout_trailer_lote.preenche_conteudo_campos(self.__conteudo_variavel_entrada))


    def trata_linha_trailer_arq(self):
        listas_de_layout_trailer_arq = trata_campos_arq.Trata_campos_arq(layout_trailer_arq240.Layout_trailer_arq240.conteudo_fixo(),
                                                                         layout_trailer_arq240.Layout_trailer_arq240.tamanho_campos(),
                                                                         layout_trailer_arq240.Layout_trailer_arq240.list_campos_head()
                                                                         )
        return "".join(listas_de_layout_trailer_arq.preenche_conteudo_campos(self.__conteudo_variavel_entrada))


