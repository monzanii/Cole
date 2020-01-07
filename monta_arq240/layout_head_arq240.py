class  Monta_head_arq240:

    #      // HEADER do Arquivo TpReg=0 tamReg: 240 Bytes
    #.       private String nrBanco1H;                // CÓDIGO DO BCO NA COMPENSAÇÃO 001 003 9(03) '341'
    #       private String nrLote2H;                 // LOTE DE SERVIÇO 004 007 9(04) '0000'
    #       private String nrTpReg3H;                // REGISTRO HEADER DE ARQUIVO 008 008 9(01) '0'
    #       private String stBrancos4_X9H;           // COMPLEMENTO DE REGISTRO 009 017 X(09) BRANCOS
    #.       private String nrCdCpfCnpj5H;            // TIPO DE INSCRIÇÃO DA EMPRESA 018 018 9(01) '1' = CPF '2' = CGC
    #.       private String nrCpfCnpj6H;              // NÚMERO DO CGC/CPF DA EMPRESA 019 032 9(14) NOTA 1
    #       private String stBrancos7_X20H;          // COMPLEMENTO DE REGISTRO	33	52	X(20)	BRANCOS	                   '
    #       private String nrBrancos8_9_1H;          // COMPLEMENTO DE REGISTRO	53	53	9(01)	'0'	'0'
    #.       private String nrAgencia10H;             // AGENCIA REFERENTE CONVÊNIO ASSINADO 054 057 9(04) NOTA 1
    #       private String stBrancos11_X01H;         // COMPLEMENTO DE REGISTRO 058 058 X(01) BRANCOS
    #       private String nrBrancos12_9_07H;        // COMPLEMENTO DE REGISTRO	59	65	9(07)	'0000000'	'0000000'
    #.       private String nrConta13H;               // NÚMERO DA CONTA CORRENTE DA EMPRESA	66	70	9(05)		19770
    #       private String stBrancos14_X01H;         // COMPLEMENTO DE REGISTRO 071 071 X(01) BRANCOS
    #.       private String nrDac15H;                 // DÍGITO DE AUTO CONFERÊNCIA AG./CONTA EMPRESA	72	72	9(01)		1
    #.       private String nmNome16H;                // NOME POR EXTENSO DA EMPRESA 'Mae'	73	102	X(30)	NOTA 2	MIRIANDAAPARECIDAMONZANI-ME   '
    #.       private String nmBanco17H;               // NOME POR EXTENSO DO BANCO COBRADOR	103	132	X(30)	BANCO ITAU SA	BANCO ITAU SA                 '
    #       private String nmBrancos18_X10H;         // COMPLEMENTO DE REGISTRO 133 142 X(10) BRANCOS
    #       private String nrCodigo19H;              // CÓDIGO REMESSA / RETORNO	143	143	9(01)	1'= Remessa ' 2'= Retorno	1
    #.       private String dtDataGer20H;             // DATA DE GERAÇÃO DO ARQUIVO 144 151 9(08) DDMMAAAA
    #       private String hrHoraGer21H;             // HORA DE GERAÇÃO DO ARQUIVO	152	157	9(06)	(HHMMSS)	143500
    #       private String nrSeqArq22H;              // NÚMERO SEQUENCIAL DO ARQUIVO RETORNO	158	163	9(06)		000000'
    #       private String nrLay23H;                 // N.º DA VERSÃO DO LAYOUT DO ARQUIVO	164	166	9(03)	'040'	'040'
    #       private String nrBrancos24_9_05H;        // COMPLEMENTO DE REGISTRO	167	171	9(05)		00000'
    #       private String stBrancos25_X54H;         // COMPLEMENTO DE REGISTRO	172	225	X(54)	BRANCOS	 '
    #       private String nrBrancos26_9_03H;        // COMPLEMENTO DE REGISTRO	226	228	9(03)		000'
    #       private String stBrancos27_X12H;         // COMPLEMENTO DE REGISTRO	229	240	X(12)	BRANCOS	            '
    #
    #        // FIM HEADER do arquivo

    @staticmethod
    def tamanho_campos():
        return {'nr_banco1H'        : 3
                ,'nr_Lote2H'        : 4
                ,'nr_tp_reg3H'      : 1
                ,'st_brancos4'      : '9'
                ,'nr_cd_cpf_cnpj5H' : 1
                ,'nr_cpf_cnpj6H'    : 14
                ,'st_brancos7H'     : '20'
                ,'nr_brancos8H'     : 1
                ,'nr_agencia10H'    : 4
                ,'st_brancos11H'    : 1
                ,'nr_brancos12H'    : 7
                ,'nr_conta13H'      : 5
                ,'st_brancos14H'    : '1'
                ,'nr_dac15H'        : 1
                ,'nm_nome16H'       : '30'
                ,'nm_banco17H'      : '30'
                ,'nm_brancos18H'    : '10'
                ,'nr_codigo19H'     : 1
                ,'dt_data_ger20H'    : 8
                ,'hr_hora_ger21H'    : 6
                ,'nr_seq_arq22H'     : 6
                ,'nr_lay23H'        : 3
                ,'nr_brancos24H'    : 5
                ,'st_brancos25H'    : '54'
                ,'nr_brancos26H'    : 3
                ,'st_brancos27H'    : '12'
                }


    @staticmethod
    def conteudo_fixo():
        return {'nr_banco1H': '341'
        , 'nr_Lote2H'       : '0'
        , 'nr_tp_reg3H'     : '0'
        , 'st_brancos4'     : '         '
        , 'nr_cd_cpf_cnpj5H': '2'
        , 'nr_cpf_cnpj6H'   : '06278504000154'
        , 'st_brancos7H'    : '                    '
        , 'nr_brancos8H'    : '0'
        , 'nr_agencia10H'   : '3240'
        , 'st_brancos11H'   : ' '
        , 'nr_brancos12H'   : '0000000'
        , 'nr_conta13H'     : '19770'
        , 'st_brancos14H'   : ' '
        , 'nr_dac15H'       : '1'
        , 'nm_nome16H'      : 'PASSACHEQUE SUA GESTAO ELETRON'
        , 'nm_banco17H'     : 'BANCO ITAU SA                 '
        , 'nm_brancos18H'   : '          '
        , 'nr_codigo19H'    : '1'
        , 'dt_data_ger20H'  : 'dados_clientePC'
        , 'hr_hora_ger21H'  : '143500'
        , 'nr_seq_arq22H'   : '000000'
        , 'nr_lay23H'       : '040'
        , 'nr_brancos24H'   : '00000'
        , 'st_brancos25H'   : ' '
        , 'nr_brancos26H'   : '000'
        , 'st_brancos27H'   : '            '
            }

        # return {'nr_banco1H': 3
        #     , 'nr_cd_cpf_cnpj5H': 1
        #     , 'nr_cpf_cnpj6H': 14
        #     , 'nr_agencia10H': 4
        #     , 'nr_conta13H': 5
        #     , 'nr_dac15H': 1
        #     , 'nm_nome16H': '30'
        #     , 'nm_banco17H': '30'
        #     , 'dt_data_ger20H': 8
        #     , 'hr_hora_ger21H': 6
        #     , 'nr_seq_arq22H': 6
        #         }


    @staticmethod
    def list_campos_head():
        return ['nr_banco1H'
            , 'nr_Lote2H'
            , 'nr_tp_reg3H'
            , 'st_brancos4'
            , 'nr_cd_cpf_cnpj5H'
            , 'nr_cpf_cnpj6H'
            , 'st_brancos7H'
            , 'nr_brancos8H'
            , 'nr_agencia10H'
            , 'st_brancos11H'
            , 'nr_brancos12H'
            , 'nr_conta13H'
            , 'st_brancos14H'
            , 'nr_dac15H'
            , 'nm_nome16H'
            , 'nm_banco17H'
            , 'nm_brancos18H'
            , 'nr_codigo19H'
            , 'dt_data_ger20H'
            , 'hr_hora_ger21H'
            , 'nr_seq_arq22H'
            , 'nr_lay23H'
            , 'nr_brancos24H'
            , 'st_brancos25H'
            , 'nr_brancos26H'
            , 'st_brancos27H'
            ]


