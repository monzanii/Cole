
class  Head_lote_arq240:


#//REGISTRO HEADER DE LOTE   TAMANHO DO REGISTRO = 240 Bytes
#
#       String  nrCodBanco1HL;                // CÓDIGO DO BANCO CÓDIGO BANCO NA COMPENSAÇÃO 001 003 9(03) '341'
#        String  nrCodLote2HL;                // CÓDIGO DO LOTE LOTE IDENTIFICAÇÃO DE SERVIÇO 004 007 9(04) NOTA 5
#        String  tpReg3HL;                    // TIPO DE REGISTRO REGISTRO HEADER DE LOTE 008 008 9(01) '1'
#        String  tpOper4HL;                   // TIPO DE OPERAÇÃO	9	9	X(01)	"R –Remessa T -Retorno      "	R
#        String  nrServ5HL;                   // IDENTIFICAÇÃO DO TIPO DE SERVIÇO	10	11	9(02)	'01'	'01'
#        String  nrZeros6_9_02HL;  	          // COMPLEMENTO DE REGISTRO	12	13	9(02)		00'
#        String  stLayOut7HL;                 // N.º DA VERSÃO DO LAYOUT DO LOTE	14	16	9(03)	'030'	'030'
#        String  stBrancos8_X01HL;            // BRANCOS COMPLEMENTO DE REGISTRO 017 017 X(01) BRANCOS
#        String  nrCodEmp9HL;                 // TIPO DE INSCRIÇÃO DA EMPRESA	18	18	9(01)	"1' – CPF '2' – CNPJ"	2
#        String  nrCpfCnpj10HL;               // N.º DE INSCRIÇÃO DA EMPRESA	19	33	9(15)	NOTA 2	006278504000154'
#        String  nrZeros11_9_20HL;            // COMPLEMENTO DE REGISTRO	34	53	9(20)	BRANCOS	                    '
#        String  nrBrancos13_9_01HL;          // COMPLEMENTO DE REGISTRO	54	54	9(01)	'0'	'0'
#        String  nrAgencia14_9_04HL;          // AGÊNCIA MANTENEDORA DA CONTA	55	58	9(04)		3240
#        String  nrBrancos15_X01HL;           // COMPLEMENTO DE REGISTRO	59	59	X(01)	BRANCOS	 '
#        String  nrBrancos16_9_07HL;          // COMPLEMENTO DE REGISTRO	60	66	9(07)	'0000000'	'0000000'
#        String  nrContaCreditada17HL;        // NÚMERO DA CONTA CORRENTE	67	71	9(05)		 19770
#        String  stBrancos18_X01_1HL;         // COMPLEMENTO DE REGISTRO	72	72	X(01)	BRANCOS	 '
#        String  nrDacCtCreditada19HL;        // DÍGITO DE AUTO - CONFERÊNCIA AG./CONTA EMPRESA	73	73	9(01)		1
#        String  nmEmp20HL;                   // NOME DA EMPRESA	74	103	X(30)		MIRIANDAAPARECIDAMONZANI-ME   '
#        String  stBrancos21_X80HL;           // COMPLEMENTO DE REGISTRO	104	183	X(80)	BRANCOS
#        String  nrSeqArq22_9_08HL;           // ARQUIVO RET.	NÚMERO SEQUENCIAL DO ARQUIVO RETORNO	184	191	9(08)		00000000'
#        String  dtDataGer23HL;               // DATA DE GRAVAÇÃO DO ARQUIVO	192	199	9(08)	DDMMAAAA	12072017
#        String  dtDataCred24HL;              // DATA DO CRÉDITO	200	207	9(08)	DDMMAAAA	14072017
#        String  stBrancos25_X33HL;	         // COMPLEMENTO DE REGISTRO	208	240	X(33)	BRANCOS	                                 '

#        // FIM DO REGISTRO HEADER LOTE

    @staticmethod
    def tamanho_campos():
        return {'nr_cod_banco1HL'         : 3
                ,'nr_cod_lote2HL'         : 4
                ,'tp_reg3HL'             : 1
                ,'tp_oper4HL'            : '1'
                ,'nr_serv5HL'            : 2
                ,'nr_zeros6_9_02HL'      : 2
                ,'st_lay_out7HL'          : 3
                ,'st_brancos8_X01HL'     : '1'
                ,'nr_cod_emp9HL'          : 1
                ,'nr_cpf_cnpj10HL'        : 15
                ,'nr_zeros11_9_20HL'     : '20'
                ,'nr_brancos13_9_01HL'   : 1
                ,'nr_agencia14_9_04HL'   : 4
                ,'nr_brancos15_X01HL'    : '1'
                ,'nr_brancos16_9_07HL'   : 7
                ,'nr_conta_creditada17HL' : 5
                ,'st_brancos18_X01_1HL'  : '1'
                ,'nr_dac_ct_creditada19HL' : 1
                ,'nm_emp20HL'            : '30'
                ,'st_brancos21_X80HL'    : '80'
                ,'nr_seq_arq22_9_08HL'    : 8
                ,'dt_data_ger23HL'        : 8
                ,'dt_data_cred24HL'       : 8
                ,'st_brancos25_X33HL'    : '33'
                }


    @staticmethod
    def conteudo_fixo():
        return {'nr_cod_banco1HL'          : '341'
                ,'nr_cod_lote2HL'          : '0001'
                ,'tp_reg3HL'               : '1'
                ,'tp_oper4HL'              : 'R'
                ,'nr_serv5HL'              : '01'
                ,'nr_zeros6_9_02HL'        : '00'
                ,'st_lay_out7HL'           : '030'
                ,'st_brancos8_X01HL'       : ' '
                ,'nr_cod_emp9HL'           : '2'
                ,'nr_cpf_cnpj10HL'         : '06278504000154'
                ,'nr_zeros11_9_20HL'       : ' '
                ,'nr_brancos13_9_01HL'     : '0'
                ,'nr_agencia14_9_04HL'     : '3240'
                ,'nr_brancos15_X01HL'      : ' '
                ,'nr_brancos16_9_07HL'     : '0'
                ,'nr_conta_creditada17HL'  : '19770'
                ,'st_brancos18_X01_1HL'    : ' '
                ,'nr_dac_ct_creditada19HL' : '1'
                ,'nm_emp20HL'              : 'PASSACHEQUE SUA GESTAO ELETRON'
                ,'st_brancos21_X80HL'      : ' '
                ,'nr_seq_arq22_9_08HL'     : '0'
                ,'dt_data_ger23HL'         : 'dados_clientePC'
                ,'dt_data_cred24HL'        : 'dados_clientePC'
                ,'st_brancos25_X33HL'      : ' '
                }

        # return {
        #       'nr_cod_banco1HL'
        #     ' 'nr_cod_emp9HL'
        #     ' 'nr_cpf_cnpj10HL': 3
        #     , 'nr_agencia14_9_04HL': 1
        #     , 'nr_conta_creditada17HL': 14
        #     , 'nr_dac_ct_creditada19HL': 4
        #     , 'nm_emp20HL': 5
        #     , 'dt_data_ger23HL': 1
        #     , 'dt_data_cred24HL': '30'
        #         }


    @staticmethod
    def list_campos_head():
        return ['nr_cod_banco1HL'
                ,'nr_cod_lote2HL'
                ,'tp_reg3HL'
                ,'tp_oper4HL'
                ,'nr_serv5HL'
                ,'nr_zeros6_9_02HL'
                ,'st_lay_out7HL'
                ,'st_brancos8_X01HL'
                ,'nr_cod_emp9HL'
                ,'nr_cpf_cnpj10HL'
                ,'nr_zeros11_9_20HL'
                ,'nr_brancos13_9_01HL'
                ,'nr_agencia14_9_04HL'
                ,'nr_brancos15_X01HL'
                ,'nr_brancos16_9_07HL'
                ,'nr_conta_creditada17HL'
                ,'st_brancos18_X01_1HL'
                ,'nr_dac_ct_creditada19HL'
                ,'nm_emp20HL'
                ,'st_brancos21_X80HL'
                ,'nr_seq_arq22_9_08HL'
                ,'dt_data_ger23HL'
                ,'dt_data_cred24HL'
                ,'st_brancos25_X33HL'
                ]


