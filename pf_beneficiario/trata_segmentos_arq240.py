from pf_beneficiario import formata_data
from monta_arq240 import layout_seg_P_arq240
class Trata_segmentos_arq240:

    def __init__(self, id_cliente , ag_benef , ct_benef):

        self.__id_cliente = id_cliente
        self.__ag_benef = ag_benef
        self.__ct_benef = ct_benef


# tem que receber a ultima quantidade da sequencia

    def consulta_conteudo_head_arq(self, id_cliente,  dt_data_ger20H):
        #(self, nr_banco1H, nr_cd_cpf_cnpj5H, nr_cpf_cnpj6H, nr_agencia10H, nr_conta13H, nr_dac15H, nm_nome16H,  nm_banco17H,  dt_data_ger20H )
        dt_now = formata_data.Formata_data.current_data(self)
        dt_data_ger20H = formata_data.Formata_data.formata_data(self, dt_now)
        #nr_cd_cpf_cnpj5H = Trata_segmentos_arq240.__trans_cod_pessoa(self, nr_cd_cpf_cnpj5H)
        return [id_cliente, dt_data_ger20H]

#seg_head_lote

    def consulta_conteudo_head_lote(self, id_cliente,  dt_data_ger23HL, dt_data_cred24HL  ):
        #nr_cod_emp9HL = Trata_segmentos_arq240.__trans_cod_pessoa(self, nr_cod_emp9HL)
        dt_now = formata_data.Formata_data.current_data(self)
        dt_venc = formata_data.Formata_data.data_do_vencimento(self, dt_now, 1)
        dt_data_ger23HL = formata_data.Formata_data.formata_data(self, dt_now)
        dt_data_cred24HL = formata_data.Formata_data.formata_data(self, dt_venc)
        return [id_cliente, dt_data_ger23HL, dt_data_cred24HL]

#seg P

    def consulta_conteudo_seg_P(self, nr_banco_compensacao1DP, qtd_reg,  nr_ag_ben9DP, nr_conta_ben12DP, nr_dac15DP,
                                nr_nosso_numero17DP, nr_dac18DP, dt_venc23DP, n_vl_titulo24DP, nr_dt_emi_tit29DP, nr_dt1_desc34DP, nr_prazo_baixa42DP):
        nr_nosso_numero17DP = Trata_segmentos_arq240.__nosso_numero(self)
        nr_dac18DP = Trata_segmentos_arq240.__dac_nosso_numero(self, nr_nosso_numero17DP, nr_ag_ben9DP, nr_conta_ben12DP)
#       nr_dac18DP = Trata_segmentos_arq240.__dac_nosso_numero(self, nr_nosso_numero17DP, self.__ag_benef, self.__ct_benef)

        data_now = formata_data.Formata_data.current_data(self)
        nr_dt_emi_tit29DP = formata_data.Formata_data.formata_data(self, data_now)
        print(nr_dt_emi_tit29DP)

        dt_venc = formata_data.Formata_data.data_do_vencimento(self, data_now, 1)
        dt_venc23DP = formata_data.Formata_data.formata_data(self, dt_venc)
        print("data venc")
        print(dt_venc23DP)
        nr_dt1_desc34DP = dt_venc23DP

#parei aqui
#        nr_reg_seq4DP = Trata_segmentos_arq240.__calcula_seq_reg(self , qtd_reg)

        nr_reg_seq4DP = qtd_reg -1

        return [self.__id_cliente, nr_banco_compensacao1DP, nr_reg_seq4DP, nr_ag_ben9DP, nr_conta_ben12DP, nr_dac15DP,
                nr_nosso_numero17DP, nr_dac18DP, dt_venc23DP, n_vl_titulo24DP, nr_dt_emi_tit29DP, nr_dt1_desc34DP, nr_prazo_baixa42DP]

    def __nosso_numero(self):
        return formata_data.Formata_data.construcao_nossnr_data_time(self)

    def __dac_nosso_numero(self, nr_nosso_numero, nr_agencia, nr_conta):
        nr_nosso_num = str(nr_nosso_numero)
        #nr_nosso_num =  '12345678'
        print(nr_nosso_num)
        full_nr_agencia = "{:04d}".format(int(nr_agencia))
        #full_nr_agencia = "0057"
        print(full_nr_agencia)
        full_nr_conta = "{:05d}".format(int(nr_conta))
        #full_nr_conta = "12345"
        print(full_nr_conta)

        lista_campos = layout_seg_P_arq240.Layout_seg_P_arq240.conteudo_fixo()
        carteira = lista_campos['nr_cart16DP']
        print("carTEIRA")
        print(carteira)
        calc_agencia = []
        calc_conta = []
        calc_cart = []
        calc_noss_nr = []

        calc_agencia.append(1 * (int(full_nr_agencia[0])))
        calc_agencia.append(2 * (int(full_nr_agencia[1])))
        calc_agencia.append(1 * (int(full_nr_agencia[2])))
        calc_agencia.append(2 * (int(full_nr_agencia[3])))
        calc_conta.append(1 * (int(full_nr_conta[0])))
        calc_conta.append(2 * (int(full_nr_conta[1])))
        calc_conta.append(1 * (int(full_nr_conta[2])))
        calc_conta.append(2 * (int(full_nr_conta[3])))
        calc_conta.append(1 * (int(full_nr_conta[4])))
        calc_cart.append(2 * (int(carteira[0])))
        calc_cart.append(1 * (int(carteira[1])))
        calc_cart.append(2 * (int(carteira[2])))
        calc_noss_nr.append(1 * (int(nr_nosso_num[0])))
        calc_noss_nr.append(2 * (int(nr_nosso_num[1])))
        calc_noss_nr.append(1 * (int(nr_nosso_num[2])))
        calc_noss_nr.append(2 * (int(nr_nosso_num[3])))
        calc_noss_nr.append(1 * (int(nr_nosso_num[4])))
        calc_noss_nr.append(2 * (int(nr_nosso_num[5])))
        calc_noss_nr.append(1 * (int(nr_nosso_num[6])))
        calc_noss_nr.append(2 * (int(nr_nosso_num[7])))

        soma_agencia = 0
        for x in range(0, 4):
            if calc_agencia[x] < 10:
                soma_agencia += calc_agencia[x]
                print('if {}'.format(calc_agencia[x]))
                print('soma_agencia - {}'.format(soma_agencia))
            else:
                soma_maior_9 = str(calc_agencia[x])
                soma_agencia += (int(soma_maior_9[0]) + int(soma_maior_9[1]))
                print('else_agencia {}'.format(soma_agencia))

        soma_conta = 0
        for i in range(0, 5):
            if calc_conta[i] < 10:
                soma_conta += calc_conta[i]
                print('if conta {}'.format( calc_conta[i]))
            else:
                soma_maior_9 = str(calc_conta[i])
                soma_conta += (int(soma_maior_9[0]) + int(soma_maior_9[1]))
                print('sdjf {}'.format(int(soma_maior_9[0]) + int(soma_maior_9[1])))
                print('soma_conta {}'.format(soma_conta))

        soma_cart = 0
        for a in range(0, 3):
            if calc_cart[a] < 10:
                soma_cart += calc_cart[a]
                print('if cart {}'.format( calc_cart[a]))
                print('soma_cart {}'.format(soma_cart))
            else:
                soma_maior_9 = str(calc_cart[a])
                soma_cart += (int(soma_maior_9[0]) + int(soma_maior_9[1]))
                print('sdjf cart {}'.format(int(soma_maior_9[0]) + int(soma_maior_9[1])))
                print('soma_cart {}'.format(soma_cart))

        soma_noss_nr = 0
        for a in range(0, 8):
            if calc_noss_nr[a] < 10:
                soma_noss_nr += calc_noss_nr[a]
                print('if noss {}'.format(calc_noss_nr[a]))
                print('soma_noss {}'.format(soma_noss_nr))
            else:
                soma_maior_9 = str(calc_noss_nr[a])
                soma_noss_nr += (int(soma_maior_9[0]) + int(soma_maior_9[1]))
                print('sdjf {}'.format(int(soma_maior_9[0]) + int(soma_maior_9[1])))
                print('soma_noss {}'.format(soma_noss_nr))

        print( 'somas {}'.format( soma_agencia + soma_conta + soma_cart + soma_noss_nr ))
        soma_total = soma_agencia + soma_conta + soma_cart + soma_noss_nr

        print(soma_total)
        print(soma_total % 10)
        print("soma total - 10 ")
        print(10 - (soma_total % 10))

        return (10 - (soma_total % 10))

    def __trans_cod_pessoa(self, nr_cd_cpf_cnpj):

        if (nr_cd_cpf_cnpj == 'J'):
            nr_cd_cpf_cnpj = '2'
        else:
            nr_cd_cpf_cnpj = '1'
        print("e agora " + nr_cd_cpf_cnpj)

        return nr_cd_cpf_cnpj


#seg_Q

    def consulta_conteudo_seg_Q(self, nr_cpf_cnpj_pagador09DQ, qtd_reg, st_nome10DQ, st_logr12DQ, st_bairro13DQ, nr_cep14DQ, nr_sufixo_cep15DQ, st_cidade16DQ, st_UF17DQ
                    , nr_ins_num19DQ, st_sac_aval20DQ):

#       nr_nr_reg04DQ = Trata_segmentos_arq240.__soma_seq_reg(self)

        nr_nr_reg04DQ = qtd_reg -1

        return [self.__id_cliente, nr_nr_reg04DQ, nr_cpf_cnpj_pagador09DQ, st_nome10DQ, st_logr12DQ, st_bairro13DQ, nr_cep14DQ, nr_sufixo_cep15DQ, st_cidade16DQ, st_UF17DQ
                    , nr_ins_num19DQ, st_sac_aval20DQ ]

#seg_trailer_lote

    def consulta_conteudo_trailer_lote(self, nr_qtd_reg5TL , nr_qtd_req6TL, nr_vl_cobSimp7TL):
        return [self.__id_cliente, nr_qtd_reg5TL, nr_qtd_req6TL, nr_vl_cobSimp7TL  ]

#seg_trailer_arq

    def consulta_conteudo_trailer_arq(self, nr_tot_qtd_lote5TA , nr_tot_qtd_arq6TA):
        return [self.__id_cliente, nr_tot_qtd_lote5TA, nr_tot_qtd_arq6TA  ]

#conta da sequencia dos registros

    def __calcula_seq_reg(self, nrSeqReg):

        nrSeqReg += 1

        return nrSeqReg
