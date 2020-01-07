
class  Layout_trailer_arq240:

#    // TRAILER DO ARQUIVO

#      nrBanco1TA;                       // CÓDIGO DO BANCO CÓDIGO BANCO NA COMPENSAÇÃO 001 003 9(03) '341'
#      nrCdLote2TA;                      // CÓDIGO DO LOTE LOTE IDENTIFICAÇÃO DE SERVIÇO 004 007 9(04) '9999'
#      nrTpReg3TA;                       // TIPO DE REGISTRO REGISTRO TRAILER DE ARQUIVO 008 008 9(01) '9'
#      stBrancos4_X09TA;                 // BRANCOS COMPLEMENTO DE REGISTRO 009 017 X(09) BRANCOS
#      nrTotQtdLote5TA;                  // TOTAL QTDE DE LOTES QTDE LOTES DO ARQUIVO 018 023 9(06) NOTA 15
#      nrTotQtdArq6TA;                   // TOTAL QTDE REGISTROS QTDE REGISTROS DO ARQUIVO 024 029 9(06) NOTA 15
#      nrZeros7TA;                       // COMPLEMENTO DE REGISTRO	30	35	9(06)		000000'
#      stBrancos8_X205TA;                // COMPLEMENTO DE REGISTRO	36	240	x(205)	BRANCOS

#    // FIM TRAILHER DO ARQUIVO


    @staticmethod
    def tamanho_campos():
        return {           'nrBanco1TA'		    :    3
                         , 'nrCdLote2TA'		:    4
                         , 'nrTpReg3TA'		    :    1
                         , 'stBrancos4_X09TA'	:    '9'
                         , 'nrTotQtdLote5TA'	:    6
                         , 'nrTotQtdArq6TA'	 	:    6
                         , 'nrZeros7TA'		    :    6
                         , 'stBrancos8_X205TA'	:    '205'
                }


    @staticmethod
    def conteudo_fixo():
           return {        'nrBanco1TA'		    :    '341'
                         , 'nrCdLote2TA'		:    '9999'
                         , 'nrTpReg3TA'		    :    '9'
                         , 'stBrancos4_X09TA'	:    ' '
                         , 'nrTotQtdLote5TA'	:    'dados_clientePC'
                         , 'nrTotQtdArq6TA'	 	:    'dados_clientePC'
                         , 'nrZeros7TA'		    :    '0'
                         , 'stBrancos8_X205TA'	:    ' '
                 }


# , 'nrTotQtdLote5T'	:    6
# , 'nrTotQtdArq6TA'	:    6
#


    @staticmethod
    def list_campos_head():
        return [           'nrBanco1TA'
                         , 'nrCdLote2TA'
                         , 'nrTpReg3TA'
                         , 'stBrancos4_X09TA'
                         , 'nrTotQtdLote5TA'
                         , 'nrTotQtdArq6TA'
                         , 'nrZeros7TA'
                         , 'stBrancos8_X205TA'
                ]
