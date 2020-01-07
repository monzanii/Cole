##from monta_arq240 import layout_trailer_arq240, layout_trailer_lote_arq240, layout_seg_Q_arq240
from pf_beneficiario import trata_arq
from pf_beneficiario import trata_segmentos_arq240
from pf_beneficiario import monta_headarq_arq240
from pf_beneficiario import monta_segP_arq240
from pf_beneficiario import monta_segQ_arq240


class main:

# COB240BF
    #with open("/home/mirian/PycharmProjects/PCMulti-V4/pf_beneficiario/arq_ent_cli_3.txt") as arquivo:
# COB240BG
    #with open("/home/mirian/PycharmProjects/PCMulti-V4/pf_beneficiario/arq_ent_cli.txt") as arquivo:
# COB240BH
    #with open("/home/mirian/PycharmProjects/PCMulti-V4/pf_beneficiario/arq_ent_cli_2RT_cli.txt") as arquivo:
# COB240BI
    #with open("/home/mirian/PycharmProjects/PCMulti-V4/pf_beneficiario/arq_ent_cli_1RT_cli.txt") as arquivo:
# COB240BJ
    #with open("/home/mirian/PycharmProjects/PCMulti-V4/pf_beneficiario/arq_ent_cli_1.txt") as arquivo:
# COB240BL
    with open("/home/mirian/PycharmProjects/PCMulti-V4/pf_beneficiario/arq_ent_cli_Marcia.txt") as arquivo:

        for linha in arquivo:
            print(linha)

            id_reg  = linha[0:3]
#            for id_cli in linha[0:3]:
            if  id_reg[0] == "1":

                ag_beneficiario = "3240"
                ct_beneficiario = "19770"
                key_trans = trata_segmentos_arq240.Trata_segmentos_arq240(linha[0:3], ag_beneficiario, ct_beneficiario)

                Inc_mock = monta_headarq_arq240.Monta_headarq_arq240(linha, key_trans)

                linha_str_headarq = Inc_mock.monta_linha_headarq()

                print("linha_str_headarq1")
                print(linha_str_headarq)

                linha_str_headarq = ''.join(linha_str_headarq)

                print("linha_str_headarq2")
                print(linha_str_headarq)

                cont_lin_cob = 0

                cont_lin_det = 0
                cont_lin_det = cont_lin_det + 1

                cont_lin_lotes = 0
                cont_lin_lotes = cont_lin_lotes + 1

                cont_lin = 0
                cont_lin = cont_lin + 1

                #######
                arquivo = open("COB240BL.txt", "w")

                arquivo.write(linha_str_headarq + "\r\n")

                print("linha_str_headarq3")
                print(linha_str_headarq)

                linha_str_headlote = Inc_mock.monta_linha_headlote()

                linha_str_headlote = ''.join(linha_str_headlote)

                cont_lin = cont_lin + 1
                cont_lin_det = cont_lin_det + 1

                arquivo.write(linha_str_headlote + "\r\n")

                print('if idcli' )
            elif id_reg[0] == "2":

                Inc_mock_P = monta_segP_arq240.Monta_segP_arq240(key_trans)

                linha_str_seg_P = Inc_mock_P.monta_linha_segP(linha, cont_lin)

                linha_str_seg_P = ''.join(linha_str_seg_P)

                cont_lin = cont_lin + 1
                cont_lin_det = cont_lin_det + 1

                arquivo.write(linha_str_seg_P + "\r\n")

                print('else_idcli')

            elif id_reg[0] == "3":

                Inc_mock_Q = monta_segQ_arq240.Monta_segQ_arq240(key_trans)

                linha_str_seg_Q = Inc_mock_Q.monta_linha_segQ(linha, cont_lin)

                linha_str_seg_Q = ''.join(linha_str_seg_Q)

                cont_lin = cont_lin + 1
                cont_lin_det = cont_lin_det + 1
                cont_lin_cob = cont_lin_cob + 1

                arquivo.write(linha_str_seg_Q + "\r\n")

        else:
            print(" fim do arquivoH")


    ###########
    # INCLUSAO MOCK TRAILER LOTE

    cont_lin = cont_lin + 1

    dados_trailer_lote = key_trans.consulta_conteudo_trailer_lote( cont_lin_det, cont_lin_cob, '00000000000001000')

    listas_trailer_lote = trata_arq.Trata_arq('trailer_lote', dados_trailer_lote)
    linha_str_trailer_lote = listas_trailer_lote.trata_linha_trailer_lote()

    arquivo.write(linha_str_trailer_lote + "\r\n")


    ###########
    # INCLUSAO MOCK TRAILER ARQ

    cont_lin = cont_lin + 1
    dados_trailer_arq = key_trans.consulta_conteudo_trailer_arq(  cont_lin_lotes, cont_lin)


    listas_trailer_arq = trata_arq.Trata_arq('trailer_arq', dados_trailer_arq)
    linha_str_trailer_arq = listas_trailer_arq.trata_linha_trailer_arq()

    arquivo.write(linha_str_trailer_arq + "\r\n")



    arquivo.close()

