
class  Layout_seg_Q_arq240:

#    // REGISTRO DETALHE do segmento Q;  TAMANHO DO REGISTRO = 240 Bytes
#
#      nr_cod_banco01DQ;     //CÓDIGO DO BANCO	N.º DO BANCO NA CÂMARA DE COMPENSAÇÃO	1	3	9(03)	341	341
#      nr_cod_lote02DQ;      //CÓDIGO DO LOTE	//"lOTE DE SERVIÇO"	4	7	9(04)	NOTA 1	0001'
#      nr_tp_reg03DQ;        //TIPO DE REGISTRO	//REGISTRO DETALHE	8	8	9(01)	3'	3'
#      nr_nr_reg04DQ;         //N.º DO REGISTRO	 //N.º SEQUENCIAL DO REGISTRO NO LOTE	9	13	9(05)	NOTA 3	00002'
#      st_seg05DQ;          //SEGMENTO	//CÓD. SEGMENTO DO REGISTRO DETALHE	14	14	X(01)	Q'	Q'
#      st_brancos06DQ;      //BRANCOS	//COMPLEMENTO DE REGISTRO	15	15	X(01)	BRANCOS	 '
#      nr_cod_ocor07DQ;      //CÓD. DE OCORRÊNCIA	//IDENTIFICAÇÃO DA OCORRÊNCIA	16	17	9(02)	NOTA 4	01'
#      nr_cod_ins08DQ;       //CÓDIGO DE INSCRIÇÃO	//"TIPO DE INSCRIÇÃO DO PAGADOR"	18	18	9(01)	"1'–CPF '2'–CNPJ"	1'
#      nr_cpf_cnpj_pagador09DQ; //INSCRIÇÃO NÚMERO //"N.º DE INSCRIÇÃO DO PAGADOR"	19	33	9(15)		000031110611838'
#      st_nome10DQ;         //NOME	//"NOME DO PAGADOR"	34	63	X(30)		Mirian da aparecida monzani   '
#      st_brancos11DQ;      //BRANCOS	//COMPLEMENTO DE REGISTRO	64	73	X(10)	NOTA 20	          '
#      st_logr12DQ;         //LOGRADOURO	//"RUA, NÚMERO, E COMPLEMENTO DOPAGADOR  "	74	113	X(40)		Av lacerda franco 1855 apt 113          '
#      st_bairro13DQ;       //BAIRRO	//"BAIRRO DO PAGADOR"	114	128	X(15)		cambuci        '
#      nr_cep14DQ;	        //"CEP DO PAGADOR"	129	133	9(05)		01536'
#      nr_sufixo_cep15DQ;    //SUFIXO DO CEP	//"SUFIXO DO CEP DO PAGADOR"	134	136	9(03)		001'
#      st_cidade16DQ;       //CIDADE	//"CIDADE DO PAGADOR"	137	151	X(15)		saopaulo       '
#      st_UF17DQ;	        //"UNIDADE DA FEDERAÇÃO DO PAGADOR"	152	153	X(02)		sp'
#      nr_cod_ins18DQ;       // CÓDIGO DE INSCRIÇÃO	//TIPO DE INSCRIÇÃO SACADOR/AVALISTA	154	154	9(01)	"1'–CPF '2' –CNPJ"	1'
#      nr_ins_num19DQ;       //INSCRIÇÃO NÚMERO	//NÚMERO DE INSCRIÇÃO DO SACADOR/AVALISTA	155	169	9(15)		000031110611838'
#      st_sac_aval20DQ;      //SACADOR/AVALISTA	//NOME DO SACADOR/AVALISTA	170	199	X(30)		Mirian da aparecida monzani   '
#      st_brancos21_X10DQ;  //BRANCOS	//COMPLEMENTO DE REGISTRO	200	209	X(10)	BRANCOS	          '
#      nr_zeros22_9_03DQ;	//COMPLEMENTO DE REGISTRO	210	212	9(03)		000'
#      st_brancos23_X28DQ; //BRANCOS	//COMPLEMENTO DE REGISTRO	213	240	X(28)	BRANCOS	                            '
#
#    // REGISTRO DETALHE segumento Q; FIM
#


    @staticmethod
    def tamanho_campos():
        return {   'nr_cod_banco01DQ'		    :  3
               ,   'nr_cod_lote02DQ'			:  4
               ,   'nr_tp_reg03DQ'			    :  1
               ,   'nr_nr_reg04DQ'			    :  5
               ,   'st_seg05DQ'			        :  '1'
               ,   'st_brancos06DQ'			    :  '1'
               ,   'nr_cod_ocor07DQ'			:  2
               ,   'nr_cod_ins08DQ'			    :  1
               ,   'nr_cpf_cnpj_pagador09DQ'	:  15
               ,   'st_nome10DQ'			    :  '30'
               ,   'st_brancos11DQ'			    :  '10'
               ,   'st_logr12DQ'			    :  '40'
               ,   'st_bairro13DQ'			    :  '15'
               ,   'nr_cep14DQ'			        :  5
               ,   'nr_sufixo_cep15DQ'			:  3
               ,   'st_cidade16DQ'			    :  '15'
               ,   'st_UF17DQ'				    :  '2'
               ,   'nr_cod_ins18DQ'			    :  1
               ,   'nr_ins_num19DQ'			    :  15
               ,   'st_sac_aval20DQ'			:  '30'
               ,   'st_brancos21_X10DQ'		    :  '10'
               ,   'nr_zeros22_9_03DQ'			:  3
               ,   'st_brancos23_X28DQ'		    :  '28'
                }


    @staticmethod
    def conteudo_fixo():
        return {   'nr_cod_banco01DQ'		    :  '341'
               ,   'nr_cod_lote02DQ'			:  '0001'
               ,   'nr_tp_reg03DQ'			    :  '3'
               ,   'nr_nr_reg04DQ'			    :  'dados_clientePC'
               ,   'st_seg05DQ'			        :  'Q'
               ,   'st_brancos06DQ'			    :  ' '
               ,   'nr_cod_ocor07DQ'			:  '01'
               ,   'nr_cod_ins08DQ'			    :  '1'
               ,   'nr_cpf_cnpj_pagador09DQ'	:  'dados_clientePC'
               ,   'st_nome10DQ'			    :  'dados_clientePC'
               ,   'st_brancos11DQ'			    :  ' '
               ,   'st_logr12DQ'			    :  'dados_clientePC'
               ,   'st_bairro13DQ'			    :  'dados_clientePC'
               ,   'nr_cep14DQ'			        :  'dados_clientePC'
               ,   'nr_sufixo_cep15DQ'			:  'dados_clientePC'
               ,   'st_cidade16DQ'			    :  'dados_clientePC'
               ,   'st_UF17DQ'				    :  'dados_clientePC'
               ,   'nr_cod_ins18DQ'			    :  '1'
               ,   'nr_ins_num19DQ'			    :  'dados_clientePC'
               ,   'st_sac_aval20DQ'			:  'dados_clientePC'
               ,   'st_brancos21_X10DQ'		    :  ' '
               ,   'nr_zeros22_9_03DQ'			:  '0'
               ,   'st_brancos23_X28DQ'		    :  ' '
                   }


#          1         2         3         4         5         6         7         8         9        10        11        12        13        14        15
# 01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234
# 111000031110611838Mirian da aparecida monzani***Av lacerda franco 1855 apt 113**********cambuci********01536001saopaulo*******sp1000031110611838
# 111000031110611838Mirian da aparecida monzani   Av lacerda franco 1855 apt 113          cambuci        01536001saopaulo       sp1000031110611838
#               ,   'nr_cpf_cnpj_pagador09DQ'   :  'dados_clientePC'
#               ,   'st_nome10DQ'			    :  'dados_clientePC'
#               ,   'st_logr12DQ'			    :  'dados_clientePC'
#               ,   'st_bairro13DQ'			    :  'dados_clientePC'
#               ,   'nr_cep14DQ'			    :  'dados_clientePC'
#               ,   'nr_sufixo_cep15DQ'			:  'dados_clientePC'
#               ,   'st_cidade16DQ'			    :  'dados_clientePC'
#               ,   'st_UF17DQ'				    :  'dados_clientePC'
#               ,   'nr_ins_num19DQ'			:  'dados_clientePC'
#               ,   'st_sac_aval20DQ'			:  'dados_clientePC'




    @staticmethod
    def list_campos_head():
        return [   'nr_cod_banco01DQ'
               ,   'nr_cod_lote02DQ'
               ,   'nr_tp_reg03DQ'
               ,   'nr_nr_reg04DQ'
               ,   'st_seg05DQ'
               ,   'st_brancos06DQ'
               ,   'nr_cod_ocor07DQ'
               ,   'nr_cod_ins08DQ'
               ,   'nr_cpf_cnpj_pagador09DQ'
               ,   'st_nome10DQ'
               ,   'st_brancos11DQ'
               ,   'st_logr12DQ'
               ,   'st_bairro13DQ'
               ,   'nr_cep14DQ'
               ,   'nr_sufixo_cep15DQ'
               ,   'st_cidade16DQ'
               ,   'st_UF17DQ'
               ,   'nr_cod_ins18DQ'
               ,   'nr_ins_num19DQ'
               ,   'st_sac_aval20DQ'
               ,   'st_brancos21_X10DQ'
               ,   'nr_zeros22_9_03DQ'
               ,   'st_brancos23_X28DQ'
             ]


