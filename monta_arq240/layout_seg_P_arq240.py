
class  Layout_seg_P_arq240:


#    // REGISTRO DETALHE do segmento P;  TAMANHO DO REGISTRO = 240 Bytes

#    // mudandca de layout

#    String  nrBancoCompensacao1DP;           //	N.º DO BANCO NA CÂMARA DE COMPENSAÇÃO	1	3	9(03)	341	341
#    String  nrCodLote2DP;                    //CÓDIGO DO LOTE	// "LOTE DE SERVIÇO"	4	7	9(04)	NOTA 1	0001'
#    String  nrTpReg3DP;                      //TIPO DE REGISTRO	// REGISTRO DETALHE	8	8	9(01)	'3'	'3'
#    String  nrRegSeq4DP;                     //N.º DO REGISTRO	 // N.º SEQUENCIAL DO REGISTRO NO LOTE	9	13	9(05)	NOTA 3	00001'
#    String  stSegDet5DP;                     // SEGMENTO	// CÓD. SEGMENTO DO REGISTRO DETALHE	14	14	X(01)	'P'	'P'
#    String  stBrancos6_X01DP;                //BRANCOS	// COMPLEMENTO DE REGISTRO	15	15	X(01)	BRANCOS	 '
#    String  nrCodOcor7DP;                    //CÓD. DE OCORRÊNCIA //	IDENTIFICAÇÃO DA OCORRÊNCIA	16	17	9(02)	NOTA 4	01'
#    String  nrBrancos8_9_01DP;               //ZEROS	// COMPLEMENTO DE REGISTRO	18	18	9(01)	'0'	0'
#    String  nrAgDebitada9DP;                 //AGÊNCIA	// AGÊNCIA MANTENEDORA DA CONTA	19	22	9(04)		3240
#    String  stBrancos10_X01DP;               //BRANCOS	// COMPLEMENTO DE REGISTRO	23	23	X(01)	BRANCOS	 '
#    String  nrBrancos11_9_07DP;              // ZEROS	// COMPLEMENTO DE REGISTRO	24	30	9(07)	'0000000'	'0000000'
#    String  nrContaDebitada12DP;             //CONTA	// NÚMERO DA CONTA CORRENTE DA EMPRESA	31	35	9(05)		19770
#    String  stBrancos13_X01DP;               //BRANCOS	// COMPLEMENTO DE REGISTRO	36	36	X(01)	BRANCOS	 '
#    String  nrDac15DP;                       //DAC	// "DÍGITO DE AUTO CONFERÊNCIA AG./CONTA EMPRESA"	37	37	9(01)		1
#    String  nrCart16DP;                      // N.º DA CARTEIRA	//" NÚMERO DA CARTEIRA NO BANCO"	38	40	9(03)	NOTA 5	110
#    String  nrNossoNumero17DP;               // NOSSO NÚMERO	// IDENTIFICAÇÃO DO TÍTULO NO BANCO	41	48	9(08)	NOTA 6	12345678'
#    String  nrDac18DP;                       // DAC //"DÍGITO DE AUTO - CONFERÊNCIA NOSSO NÚMERO"	49	49	9(01)	NOTA 25	1'
#    String  stBrancos19_X08DP;               // BRANCOS	// COMPLEMENTO DE REGISTRO	50	57	X(08)	BRANCOS	        '
#    String  nrBrancos20_9_05DP;              // ZEROS	// "COMPLEMENTO DEREGISTRO"	58	62	9(05)		00000'
#    String  stNrDocumento21DP;               // N.º DO DOCUMENTO	//NÚMERO DO DOCUMENTO DE COBRANÇA (DUPL.NP...)	63	72	X(10)	NOTA 7	          '
#    String  stBrancos22_X05DP;               // BRANCOS	//COMPLEMENTO DE REGISTRO	73	77	X(05)	BRANCOS	     '
#    String  dtVenc23DP;                      // VENCIMENTO	// DATA DE VENCIMENTO DO TÍTULO	78	85	9(08)	NOTA 8	01082017'
#    String  nVlTitulo24DP;                   // VALOR DO TÍTULO //	"VALOR NOMINALDO TÍTULO"	86	100	9(13)V9(2)	NOTA 9	000000000001000'
#    String  nrAgencia25DP;                   // AG.COBRADORA	// AGÊNCIA ONDE O TÍTULO SERÁ COBRADO	101	105	9(05)	NOTA 10	00000'
#    String  nrDAC26DP;	                      // "DÍGITO AUTO CONFERÊNCIA   AGÊNCIA COBRADORA "	106	106	9(01)		0'
#    String  nrEspecie27DP;                   // ESPÉCIE TÍTULO	// ESPÉCIE DO TÍTULO	107	108	9(02)	NOTA 11	17
#    String  stAceite28DP;	                  // "IDENTIFICAÇÃO DE TÍTULO ACEITO/NÃO ACEITO"	109	109	X(01)	"A –SIM N –NÃO"	A
#    String  nrDtEmiTit29DP;                  // DATA EMISSÃO TÍTULO	// DATA DA EMISSÃO DO TÍTULO	110	117	9(08)	DDMMAAAA	13072017
#    String  nrBrancos30_9_01DP;              // ZEROS	//COMPLEMENTO DE REGISTRO	118	118	9(01)		0'
#    String  nrDtJurMoraDt31DP;               // JUROS MORA	// DATA BASE P/COBRANÇA DE JUROS DE MORA	119	126	9(08)	NOTA 12	01082017'
#    String  nrVlJuros1Dia32DP;               // JUROS DE 1 DIA	// VALOR DE MORA POR DIA DE ATRASO	127	141	9(13)V9(2)	NOTA 13	000000000001000'
#    String  nrBrancos33_9_01DP;              // ZEROS	// COMPLEMENTO DE REGISTRO	142	142	9(01)		0'
#    String  nrDt1Desc34DP;                   // DATA 1º DESC.	// DATA LIMITE DO 1º DESCONTO	143	150	9(08)	DDMMAAAA	13082017
#    String  nrVl1Desc35DP;                   // VALOR 1º DESC	//VALOR DO 1º DESCONTO A SER CONCEDIDO	151	165	9(13)V9(2)	NOTA 14	000000000001000'
#    String  nrVlIOF36DP;                     // VALOR IOF	  // VALOR DO IOF A SER RECOLHIDO P/NOTAS SEGURO	166	180	9(13)V9(2)	NOTA 15	000000000000000'
#    String  nrVlAbati37DP;                   // VALOR ABATIMENTO	// VALOR DO ABATIMENTO	181	195	9(13)V9(2)	NOTA 16	000000000000000'
#    String  stUsoEmp38DP;                    // USO DA EMPRESA	// "IDENTIFICAÇÃO DO TÍTULO NA EMPRESA"	196	220	X(25)	NOTA 17	                         '
#    String  nrCodNegProt39DP;                //"CÓDIGO P/ NEGATIVAÇÃO OU PROTESTO"	//"CÓDIGO PARA NEGATIVAÇÃO OU PROTESTO"	221	221	9(01)	NOTA 18	3
#    String  nrPrazoNegProt40DP;              //"PRAZO PARA NEGATIVAÇÃO OU PROTESTO"	//"NÚMERO DE DIAS PARA NEGATIVAÇÃO OU PROTESTO"	222	223	9(02)	NOTA 18	03'
#    String  nrCodBaixa41DP;                  // BAIXA	// "CÓDIGO PARA BAIXA"	224	224	9(01)	NOTA 19	1
#    String  nrPrazoBaixa42DP;                // PRAZO BAIXA	// NÚMERO DE DIAS PARA BAIXA	225	226	9(02)	NOTA 19	05'
#    String  nrZeros43_9_13DP;                // ZEROS	// COMPLEMENTO DE REGISTRO	227	239	9(13)		0000000000000'
#    String  stBRANCOS44_01DP;	              // COMPLEMENTO DE REGISTRO	240	240	X(01)	BRANCOS	 '

#    // REGISTRO DETALHE segumento P FIM


    @staticmethod
    def tamanho_campos():
        return {'nr_banco_compensacao1DP' : 3
              , 'nr_cod_lote2DP'          : 4
              , 'nr_tp_reg3DP'            : 1
              , 'nr_reg_seq4DP'           : 5
              , 'st_seg_det5DP'           : '1'
              , 'st_brancos6_X01DP'       : '1'
              , 'nr_cod_ocor7DP'          : 2
              , 'nr_brancos8_9_01DP'      : 1
              , 'nr_ag_debitada9DP'       : 4
              , 'st_brancos10_X01DP'      : '1'
              , 'nr_brancos11_9_07DP'     : 7
              , 'nr_conta_debitada12DP'   : 5
              , 'st_brancos13_X01DP'      : '1'
              , 'nr_dac15DP'              : 1
              , 'nr_cart16DP'             : 3
              , 'nr_nosso_numero17DP'     : 8
              , 'nr_dac18DP'              : 1
              , 'st_brancos19_X08DP'      : '8'
              , 'nr_brancos20_9_05DP'     : 5
              , 'st_nr_documento21DP'     : '10'
              , 'st_brancos22_X05DP'      :  '5'
              , 'dt_venc23DP'             : 8
              , 'n_vl_titulo24DP'         : 15
              , 'nr_agencia25DP'          : 5
              , 'nr_dac26DP'              : 1
              , 'nr_especie27DP'          : 2
              , 'st_aceite28DP'           : '1'
              , 'nr_dt_emi_tit29DP'       : 8
              , 'nr_brancos30_9_01DP'     : 1
              , 'nr_dt_jur_mora_dt31DP'   : 8
              , 'nr_vl_juros1_dia32DP'    : 15
              , 'nr_brancos33_9_01DP'     : 1
              , 'nr_dt1_desc34DP'         : 8
              , 'nr_vl1_desc35DP'         : 15
              , 'nr_vl_IOF36DP'           : 15
              , 'nr_vl_abati37DP'         : 15
              , 'st_uso_emp38DP'          : '25'
              , 'nr_cod_neg_prot39DP'     : 1
              , 'nr_prazo_neg_prot40DP'   : 2
              , 'nr_cod_baixa41DP'        : 1
              , 'nr_prazo_baixa42DP'      : 2
              , 'nr_zeros43_9_13DP'       : 13
              , 'st_brancos44_01DP'       : '1'
                }


    @staticmethod
    def conteudo_fixo():
        return {'nr_banco_compensacao1DP' : 'dados_clientePC'
              , 'nr_cod_lote2DP'          : '0001'
              , 'nr_tp_reg3DP'            : '3'
              , 'nr_reg_seq4DP'           : 'dados_clientePC'
              , 'st_seg_det5DP'           : 'P'
              , 'st_brancos6_X01DP'       : ' '
              , 'nr_cod_ocor7DP'          : '01'
              , 'nr_brancos8_9_01DP'      : '0'
              , 'nr_ag_debitada9DP'       : 'dados_clientePC'
              , 'st_brancos10_X01DP'      : ' '
              , 'nr_brancos11_9_07DP'     : '0'
              , 'nr_conta_debitada12DP'   : 'dados_clientePC'
              , 'st_brancos13_X01DP'      : ' '
              , 'nr_dac15DP'              : 'dados_clientePC'
              , 'nr_cart16DP'             : '109'
              , 'nr_nosso_numero17DP'     : 'dados_clientePC'
              , 'nr_dac18DP'              : 'dados_clientePC'
              , 'st_brancos19_X08DP'      : ' '
              , 'nr_brancos20_9_05DP'     : '0'
              , 'st_nr_documento21DP'     : ' '
              , 'st_brancos22_X05DP'      : ' '
              , 'dt_venc23DP'             : 'dados_clientePC'
              , 'n_vl_titulo24DP'         : 'dados_clientePC'
              , 'nr_agencia25DP'          : '0'
              , 'nr_dac26DP'              : '0'
              , 'nr_especie27DP'          : '1'
              , 'st_aceite28DP'           : 'A'
              , 'nr_dt_emi_tit29DP'       : 'dados_clientePC'
              , 'nr_brancos30_9_01DP'     : '0'
              , 'nr_dt_jur_mora_dt31DP'   : '0'
              , 'nr_vl_juros1_dia32DP'    : '0'
              , 'nr_brancos33_9_01DP'     : '0'
              , 'nr_dt1_desc34DP'         : 'dados_clientePC'
              , 'nr_vl1_desc35DP'         : '0'
              , 'nr_vl_IOF36DP'           : '0'
              , 'nr_vl_abati37DP'         : '0'
              , 'st_uso_emp38DP'          : ' '
              , 'nr_cod_neg_prot39DP'     : '0'
              , 'nr_prazo_neg_prot40DP'   : '0'
              , 'nr_cod_baixa41DP'        : '0'
              , 'nr_prazo_baixa42DP'      : 'dados_clientePC'
              , 'nr_zeros43_9_13DP'       : '0'
              , 'st_brancos44_01DP'       : ' '
                }

        # return {
        #       'nr_banco_compensacao1DP'
        #     ' 'nr_ag_debitada9DP'
        #     ' 'nr_conta_debitada12DP'
        #     , 'nr_dac15DP'
        #     , 'nr_nosso_numero17DP'
        #     , 'nr_dac18DP'
        #     , 'dt_venc23DP'
        #     , 'n_vl_titulo24DP
        #     , 'nr_dt_emi_tit29DP
        #     , 'nr_dt1_desc34DP
        #     , 'nr_prazo_baixa42DP
        #         }


    @staticmethod
    def list_campos_head():
        return ['nr_banco_compensacao1DP'
              , 'nr_cod_lote2DP'
              , 'nr_tp_reg3DP'
              , 'nr_reg_seq4DP'
              , 'st_seg_det5DP'
              , 'st_brancos6_X01DP'
              , 'nr_cod_ocor7DP'
              , 'nr_brancos8_9_01DP'
              , 'nr_ag_debitada9DP'
              , 'st_brancos10_X01DP'
              , 'nr_brancos11_9_07DP'
              , 'nr_conta_debitada12DP'
              , 'st_brancos13_X01DP'
              , 'nr_dac15DP'
              , 'nr_cart16DP'
              , 'nr_nosso_numero17DP'
              , 'nr_dac18DP'
              , 'st_brancos19_X08DP'
              , 'nr_brancos20_9_05DP'
              , 'st_nr_documento21DP'
              , 'st_brancos22_X05DP'
              , 'dt_venc23DP'
              , 'n_vl_titulo24DP'
              , 'nr_agencia25DP'
              , 'nr_dac26DP'
              , 'nr_especie27DP'
              , 'st_aceite28DP'
              , 'nr_dt_emi_tit29DP'
              , 'nr_brancos30_9_01DP'
              , 'nr_dt_jur_mora_dt31DP'
              , 'nr_vl_juros1_dia32DP'
              , 'nr_brancos33_9_01DP'
              , 'nr_dt1_desc34DP'
              , 'nr_vl1_desc35DP'
              , 'nr_vl_IOF36DP'
              , 'nr_vl_abati37DP'
              , 'st_uso_emp38DP'
              , 'nr_cod_neg_prot39DP'
              , 'nr_prazo_neg_prot40DP'
              , 'nr_cod_baixa41DP'
              , 'nr_prazo_baixa42DP'
              , 'nr_zeros43_9_13DP'
              , 'st_brancos44_01DP'
                ]


