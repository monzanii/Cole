
class  Layout_trailer_lote_arq240:

#   // TRAILER DE LOTE
#
#      nrBanco1TL;                     //CÓDIGO DO BANCO	  //N.º DO BANCO NA CÂMARA DE COMPENSAÇÃO	1	3	9(03)	341	341
#      nrCodLote2TL;                   //CÓDIGO DO LOTE	//LOTE DE SERVIÇO	4	7	9(04)	NOTA 1	0001'
#      nrTpReg3TL;                     //TIPO DE REGISTRO	//REGISTRO TRAILER DO LOTE	8	8	9(01)	'5'	'5'
#      stBrancos4_X09TL;               //BRANCOS	//COMPLEMENTO DE REGISTRO	9	17	X(09)	BRANCOS	         '
#      nrQtdReg5TL;                    //"QTDE. DE REGISTROS"	//QUANTIDADE DE REGISTROS DO LOTE	18	23	9(06)	NOTA 26	000006'
#      nrQtdReq6TL;                    //QTDE. COBR. SIMPLES	//QTDE. DE TÍTULOS EM COBRANÇA SIMPLES	24	29	9(06)	NOTA 24	000000'
#      nrVlCobSimp7TL;                 //VLR. COBR.SIMPLES	//VALOR TOTAL TÍTULOS EM COBRANÇA SIMPLES	30	46	9(15)V9(2)	NOTA 24	00000000000001000'
#      nrQtdCobVinc8TL;                //QTDE. COB.VINCULADA	//QTDE. DE TÍTULOS EM COBRANÇA VINCULADA	47	52	9(06)	NOTA 24	000000'
#      nrVlCobVinc9TL;                 //VLR. COBR.VINCULADA	//VALOR TOTAL TÍTULOS EM COBRANÇA VINCULADA	53	69	9(15)V9(2)	NOTA 24	00000000000000000'
#      nrZeros10_46TL;                 //ZEROS	//COMPLEMENTO DE REGISTRO	70	115	9(46)		0000000000000000000000000000000000000000000000'
#      stAvisoBanc11TL;                //AVISO BANCÁRIO	//REFERÊNCIA DO AVISO BANCÁRIO	116	123	X(08)	NOTA 25	        '
#      stBrancos12_X117TL;             //BRANCOS	//COMPLEMENTO DE REGISTRO	124	240	X(117) Brancos

#    // FIM TRAILER DE LOTE


    @staticmethod
    def tamanho_campos():
        return {   'nr_banco1TL'	         : 3
               ,   'nr_cod_lote2TL'	     : 4
               ,   'nr_tp_reg3TL'	         : 1
               ,   'st_brancos4_X09TL'      : '9'
               ,   'nr_qtd_reg5TL'	         : 6
               ,   'nr_qtd_req6TL'	         : 6
               ,   'nr_vl_cob_simp7TL'       : 17
               ,   'nr_qtd_cob_vinc8TL'      : 6
               ,   'nr_vl_cob_vinc9TL'       : 17
               ,   'nr_zeros10_46TL'        : 46
               ,   'st_aviso_banc11TL'      : '8'
               ,   'st_brancos12_X117TL'    : '117'
                   }


    @staticmethod
    def conteudo_fixo():
           return {    'nr_banco1TL'             : '341'
                  ,   'nr_cod_lote2TL'	         : '0001'
                  ,   'nr_tp_reg3TL'	         : '5'
                  ,   'st_brancos4_X09TL'       : ' '
                  ,   'nr_qtd_reg5TL'	         : 'dados_clientePC'
                  ,   'nr_qtd_req6TL'	         : 'dados_clientePC'
                  ,   'nr_vl_cob_simp7TL'       : 'dados_clientePC'
                  ,   'nr_qtd_cob_vinc8TL'       : '0'
                  ,   'nr_vl_cob_vinc9TL'        : '0'
                  ,   'nr_zeros10_46TL'         : '0'
                  ,   'st_aviso_banc11TL'       : '00000000'
                  ,   'st_brancos12_X117TL'     : ' '
                      }

#               ,  + 'nr_qtd_reg5TL'	      : 6
#               ,  + 'nr_qtd_req6TL'	      : 6
#               ,  + 'nr_vl_cobSimp7TL'       : 17
#



    @staticmethod
    def list_campos_head():
        return [    'nr_banco1TL'
               ,   'nr_cod_lote2TL'
               ,   'nr_tp_reg3TL'
               ,   'st_brancos4_X09TL'
               ,   'nr_qtd_reg5TL'
               ,   'nr_qtd_req6TL'
               ,   'nr_vl_cob_simp7TL'
               ,   'nr_qtd_cob_vinc8TL'
               ,   'nr_vl_cob_vinc9TL'
               ,   'nr_zeros10_46TL'
               ,   'st_aviso_banc11TL'
               ,   'st_brancos12_X117TL'
              ]

