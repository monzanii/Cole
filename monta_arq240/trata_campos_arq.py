
class Trata_campos_arq:

    def __init__(self, dic_conteudo_fixo_campo, dic_tam_real_campo, dic_nome_campo):
        self.__dic_conteudo_fixo_campo = dic_conteudo_fixo_campo
        self.__dic_tam_real_campo =  dic_tam_real_campo
        self.__dic_nome_campo = dic_nome_campo


    def preenche_conteudo_campos(self, dados_cliente):
        linha_head = []
        cont = 1
        # print( type(self.__dic_nome_campo))

        for linha in self.__dic_nome_campo:

             if self.__dic_conteudo_fixo_campo[linha] == "dados_clientePC":
                #cont += 1
                #print(dados_cliente[cont])
                dados_cliente[cont] = str(dados_cliente[cont])
                tamanho_conteudo = len(dados_cliente[cont])
                #print("dentro do if variavel, conteudo variavel =  {} , campo varivel = {} ".format(tamanho_conteudo , dados_cliente[cont]))
                novo_campo_linha = dados_cliente[cont]
                #print(dados_cliente)
                cont += 1
             else:
                tamanho_conteudo = len(self.__dic_conteudo_fixo_campo[linha])
                novo_campo_linha = (self.__dic_conteudo_fixo_campo[linha])
                # alteracao01 feita 26/05 porque estava montando o headarq errado, nao estava contando o conteudo fixo
                #cont += 1

             tamanho_real_campo = int(self.__dic_tam_real_campo[linha])
             # print("tamanho real= {} , tamanho do conteudo =  {}".format(tamanho_real_campo, tamanho_conteudo))


             if (tamanho_conteudo == tamanho_real_campo):
                # linha_head.append(self.__dic_conteudo_fixo_campo[linha])
                linha_head.append(novo_campo_linha)
                # print(linha_head)


             # elif len(dic_cont_fixo_campo[linha]) < int(dic_tam_real_campo[linha]):
             elif (tamanho_conteudo < tamanho_real_campo):
                diferenca_de_caracteres = abs(len(novo_campo_linha) - int(self.__dic_tam_real_campo[linha]))
                if (type(self.__dic_tam_real_campo[linha]) == str):
                    novo_campo_linha = novo_campo_linha + (" " * diferenca_de_caracteres)
                    # print("else string " + linha, self.__dic_tam_real_campo[linha], len(self.__dic_conteudo_fixo_campo[linha]), self.__dic_conteudo_fixo_campo[linha],
                    #      novo_campo_linha)
                else:
                    novo_campo_linha =  ("0" * diferenca_de_caracteres) + novo_campo_linha
                    # print("else numerico " + linha, self.__dic_tam_real_campo[linha], len(self.__dic_conteudo_fixo_campo[linha]), self.__dic_conteudo_fixo_campo[linha],
                    #     novo_campo_linha)

                linha_head.append(novo_campo_linha)
                # print(linha_head)

        return linha_head