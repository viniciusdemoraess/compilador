import os
import sys

try:
    class lexico:
        #Analisador Léxico
        def __init__(self, arquivo_fonte):
            self.cabeca = 0
            self.fita = []
            self.numero_linha = 1
            self.tabela_simbolos = []
            self.lexema = ''
            self.fim_linha = '\n'
            self.especiais = ['+', '-', '*', '/', '(', ')', '=', '==', '>', ';']
            self.arquivo = arquivo_fonte
            if not os.path.exists(self.arquivo):
                print("Erro: Arquivo {0} não foi encontrado.".format(self.arquivo))
                exit()
            else:
                self.arquivo = open(self.arquivo, 'r')

        def avancar_cabeca(self):
            self.cabeca += 1 
        
        def posicao_cabeca(self):
            return self.cabeca
    
        def atualizar_linha(self):
            self.numero_linha += 1
        
        def obter_caracter(self):
            if self.cabeca < len(self.fita):
                self.letra = self.fita[self.cabeca]
                self.avancar_cabeca()
                if self.letra != self.fim_linha or not self.letra.isspace():
                    self.lexema += self.letra
                return self.letra
            else:
                return '\n'
        
        def tabela_tokens(self):
            for self.linha in self.arquivo:
                self.fita  = list(self.linha)
                self.q0()
                self.atualizar_linha()
                self.cabeca = 0
            self.arquivo.close()
            return self.tabela_simbolos
            
        def q0(self):
            self.caracter = self.obter_caracter()
            if 'r' == self.caracter:           
                self.q1()
            elif 'p' == self.caracter:
                self.q5()
            elif 'i' == self.caracter:
                self.q10()
            elif 'f' == self.caracter:
                self.q18()
            elif 't' == self.caracter:
                self.q25()
            elif 'e' == self.caracter:
                self.q29()
            elif 'd' == self.caracter:
                self.q37()
            elif 'w' == self.caracter:
                self.q39()
            elif '+' == self.caracter:
                self.q44()
            elif '-' == self.caracter:
                self.q45()
            elif '*' == self.caracter:
                self.q46()
            elif '/' == self.caracter:
                self.q47()
            elif '(' == self.caracter:
                self.q48()
            elif ')' == self.caracter:
                self.q49()
            elif '=' == self.caracter:
                self.q50()
            elif '==' == self.caracter:
                self.q51()
            elif '>' == self.caracter:
                self.q52()
            elif ';' == self.caracter:
                self.q53()
            elif self.caracter.isdigit(): #NUMEROS
                self.q54()
            elif self.caracter.islower(): #LETRAS OU NUMBERS DEPENDE (ID)
                self.q55()
            elif self.fim_linha == self.caracter:
                pass
            elif self.caracter.isspace():
                self.lexema = ''
                self.q0()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        def q1(self):
            self.caracter = self.obter_caracter()
            if 'e' == self.caracter:
                self.q2()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        def q2(self):
            self.caracter = self.obter_caracter()
            if 'a' == self.caracter:
                self.q3()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        def q3(self):
            self.caracter = self.obter_caracter()
            if 'd' == self.caracter:
                self.q4()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        #ESTADO FINAL
        def q4(self):
            # Comando READ #
            self.caracter = self.obter_caracter()
            if self.fim_linha == self.caracter:
                self.tabela_simbolos.append(["ler", self.lexema, self.numero_linha ,self.cabeca-1]) #ULTIMO NUMERO COLUNA VERIFICAR DPOIS
                self.lexema = ''
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["ler", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.q0()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["ler", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.cabeca -= 1
                self.q0()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        def q5(self):
            self.caracter = self.obter_caracter()
            if 'r' == self.caracter:
                self.q6()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        
        def q6(self):
            self.caracter = self.obter_caracter()
            if 'i' == self.caracter:
                self.q7()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        def q7(self):
            self.caracter = self.obter_caracter()
            if 'n' == self.caracter:
                self.q8()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        
        def q8(self):
            self.caracter = self.obter_caracter()
            if 't' == self.caracter:
                self.q9()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        
        def q9(self):
            # Comando PRINT #
            self.caracter = self.obter_caracter()
            if self.fim_linha == self.caracter:
                self.tabela_simbolos.append(["escrever", self.lexema, self.numero_linha ,self.cabeca-1]) #ULTIMO NUMERO COLUNA VERIFICAR DPOIS
                self.lexema = ''
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["escrever", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.q0()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["escrever", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.cabeca -= 1
                self.q0()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        def q10(self):
            self.caracter = self.obter_caracter()
            if 'n' == self.caracter:
                self.q11()
            elif 'f' == self.caracter:
                self.q24() ##FAZER -- Ja fiz
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()        
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        
        def q11(self):
            self.caracter = self.obter_caracter()
            if 't' == self.caracter:
                self.q12()
            elif 'i' == self.caracter:
                self.q13()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        def q12(self):
            # Comando INT #
            self.caracter = self.obter_caracter()
            if self.fim_linha == self.caracter:
                self.tabela_simbolos.append(["varInt", self.lexema, self.numero_linha ,self.cabeca-1]) #ULTIMO NUMERO COLUNA VERIFICAR DPOIS
                self.lexema = ''
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["varInt", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.q0()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["varInt", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.cabeca -= 1
                self.q0()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        
        ##INI-T
        def q13(self):
            self.caracter = self.obter_caracter()
            if 't' == self.caracter:
                self.q14()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        def q14(self):
            self.caracter = self.obter_caracter()
            if 'i' == self.caracter:
                self.q15()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        def q15(self):
            self.caracter = self.obter_caracter()
            if 'a' == self.caracter:
                self.q16()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        def q16(self):
            self.caracter = self.obter_caracter()
            if 'l' == self.caracter:
                self.q17()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        
        def q17(self):
            # Comando INITIAL #
            self.caracter = self.obter_caracter()
            if self.fim_linha == self.caracter:
                self.tabela_simbolos.append(["programInitial", self.lexema, self.numero_linha ,self.cabeca-1]) #ULTIMO NUMERO COLUNA VERIFICAR DPOIS
                self.lexema = ''
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["programInitial", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.q0()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["programInitial", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.cabeca -= 1
                self.q0()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            else:
               print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
               exit()


            
        def q18(self):
            self.caracter = self.obter_caracter()
            if 'i' == self.caracter:
                self.q19()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        
        def q19(self):
            self.caracter = self.obter_caracter()
            if 'n' == self.caracter:
                self.q20()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        def q20(self):
            self.caracter = self.obter_caracter()
            if 'i' == self.caracter:
                self.q21()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        def q21(self):
            self.caracter = self.obter_caracter()
            if 's' == self.caracter:
                self.q22()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        
        def q22(self):
            self.caracter = self.obter_caracter()
            if 'h' == self.caracter:
                self.q23()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        def q23(self):
            # Comando FINISH #
            self.caracter = self.obter_caracter()
            if self.fim_linha == self.caracter:
                self.tabela_simbolos.append(["programFinish", self.lexema, self.numero_linha ,self.cabeca-1]) #ULTIMO NUMERO COLUNA VERIFICAR DPOIS
                self.lexema = ''
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["programFinish", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.q0()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["programFinish", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.cabeca -= 1
                self.q0()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        def q24(self):
            # Comando IF - SE #
            self.caracter = self.obter_caracter()
            if self.fim_linha == self.caracter:
                self.tabela_simbolos.append(["se", self.lexema, self.numero_linha ,self.cabeca-1]) #ULTIMO NUMERO COLUNA VERIFICAR DPOIS
                self.lexema = ''
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["se", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.q0()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["se", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.cabeca -= 1
                self.q0()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        
        def q25(self):
            self.caracter = self.obter_caracter()
            if 'h' == self.caracter:
                self.q26()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        def q26(self):
            self.caracter = self.obter_caracter()
            if 'e' == self.caracter:
                self.q27()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()
        
        def q27(self):
            self.caracter = self.obter_caracter()
            if 'n' == self.caracter:
                self.q28()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        
        def q28(self):
            # Comando then - entao #
            self.caracter = self.obter_caracter()
            if self.fim_linha == self.caracter:
                self.tabela_simbolos.append(["entao", self.lexema, self.numero_linha ,self.cabeca-1]) #ULTIMO NUMERO COLUNA VERIFICAR DPOIS
                self.lexema = ''
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["entao", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.q0()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["entao", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.cabeca -= 1
                self.q0()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        
        def q29(self):
            self.caracter = self.obter_caracter()
            if 'l' == self.caracter:
                self.q30()
            elif 'n' == self.caracter:
                self.q33()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        def q30(self):
            self.caracter = self.obter_caracter()
            if 's' == self.caracter:
                self.q31()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        
        def q31(self):
            self.caracter = self.obter_caracter()
            if 'e' == self.caracter:
                self.q32()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        def q32(self):
            # Comando else - senao #
            self.caracter = self.obter_caracter()
            if self.fim_linha == self.caracter:
                self.tabela_simbolos.append(["senao", self.lexema, self.numero_linha ,self.cabeca-1]) #ULTIMO NUMERO COLUNA VERIFICAR DPOIS
                self.lexema = ''
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["senao", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.q0()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["senao", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.cabeca -= 1
                self.q0()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        
        def q33(self):
            self.caracter = self.obter_caracter()
            if 'd' == self.caracter:
                self.q34()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        
        def q34(self):
            self.caracter = self.obter_caracter()
            if 'i' == self.caracter:
                self.q35()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        def q35(self):
            self.caracter = self.obter_caracter()
            if 'f' == self.caracter:
                self.q36()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        def q36(self):
            # Comando endif - fimse #
            self.caracter = self.obter_caracter()
            if self.fim_linha == self.caracter:
                self.tabela_simbolos.append(["fimse", self.lexema, self.numero_linha ,self.cabeca-1]) #ULTIMO NUMERO COLUNA VERIFICAR DPOIS
                self.lexema = ''
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["fimse", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.q0()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["fimse", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.cabeca -= 1
                self.q0()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        def q37(self):
            self.caracter = self.obter_caracter()
            if 'o' == self.caracter:
                self.q38()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        def q38(self):
            # Comando do - REPITA #
            self.caracter = self.obter_caracter()
            if self.fim_linha == self.caracter:
                self.tabela_simbolos.append(["REPITA", self.lexema, self.numero_linha ,self.cabeca-1]) #ULTIMO NUMERO COLUNA VERIFICAR DPOIS
                self.lexema = ''
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["REPITA", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.q0()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["REPITA", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.cabeca -= 1
                self.q0()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            else:
               print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
               exit()


        def q39(self):
            self.caracter = self.obter_caracter()
            if 'h' == self.caracter:
                self.q40()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        
        def q40(self):
            self.caracter = self.obter_caracter()
            if 'i' == self.caracter:
                self.q41()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        
        def q41(self):
            self.caracter = self.obter_caracter()
            if 'l' == self.caracter:
                self.q42()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        
        def q42(self):
            self.caracter = self.obter_caracter()
            if 'e' == self.caracter:
                self.q43()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        def q43(self):
            # Comando while - ENQUANTO #
            self.caracter = self.obter_caracter()
            if self.fim_linha == self.caracter:
                self.tabela_simbolos.append(["ENQUANTO", self.lexema, self.numero_linha ,self.cabeca-1]) #ULTIMO NUMERO COLUNA VERIFICAR DPOIS
                self.lexema = ''
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["ENQUANTO", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.q0()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["ENQUANTO", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.cabeca -= 1
                self.q0()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()


        def q44(self):
            '''Reconhece o MAIS +'''
            self.tabela_simbolos.append(["+", self.lexema, self.numero_linha ,self.cabeca])
            self.lexema = ''
            self.q0()
        
        def q45(self):
            '''Reconhece o MENOS -'''
            self.tabela_simbolos.append(["-", self.lexema, self.numero_linha ,self.cabeca])
            self.lexema = ''
            self.q0()
        
        def q46(self):
            '''Reconhece a MULTIPLICACAO *'''
            self.tabela_simbolos.append(["*", self.lexema, self.numero_linha ,self.cabeca])
            self.lexema = ''
            self.q0()

        def q47(self):
            '''Reconhece a DIVISAO /'''
            self.tabela_simbolos.append(["/", self.lexema, self.numero_linha ,self.cabeca])
            self.lexema = ''
            self.q0()

        def q48(self):
            '''Reconhece o ABRE PARENTESES ( '''
            self.tabela_simbolos.append(["(", self.lexema, self.numero_linha ,self.cabeca])
            self.lexema = ''
            self.q0() 

        def q49(self):
            '''Reconhece o FECHA PARENTESES ) '''
            self.tabela_simbolos.append([")", self.lexema, self.numero_linha ,self.cabeca])
            self.lexema = ''
            self.q0() 
        
        def q50(self):
            self.caracter = self.obter_caracter()
            if '=' == self.caracter:
                self.q51()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q56()
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.cabeca -= 1
                self.q56()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        
        def q51(self):
            # Comando IGUAL - == #
            self.tabela_simbolos.append(["==", self.lexema, self.numero_linha ,self.cabeca])
            self.lexema = ''
            self.q0() 
        
        def q52(self):
            '''Reconhece o MAIOR > '''
            self.tabela_simbolos.append([">", self.lexema, self.numero_linha ,self.cabeca])
            self.lexema = ''
            self.q0() 
        
        def q53(self):
            '''Reconhece o PONTO E VIRGULA ; '''
            self.tabela_simbolos.append([";", self.lexema, self.numero_linha ,self.cabeca])
            self.lexema = ''
            self.q0() 
        
        def q54(self):
            '''Reconhece Numeros'''
            self.caracter = self.obter_caracter()
            while self.caracter.isdigit():
                self.caracter = self.obter_caracter()
            if self.fim_linha == self.caracter:
                self.tabela_simbolos.append(["NUMERO", self.lexema, self.numero_linha ,self.cabeca-1])
                self.lexema = ''
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["NUMERO", self.lexema, self.numero_linha ,self.cabeca-1])
                self.lexema = ''
                self.q0()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["NUMERO", self.lexema, self.numero_linha ,self.cabeca-1])
                self.lexema = ''
                self.cabeca -= 1
                self.q0()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,))
                exit()


        def q55(self):
            ''' Reconhece IDs'''
            self.caracter = self.obter_caracter()
            while self.caracter.isdigit() or self.caracter.islower():
                self.caracter = self.obter_caracter()
            if self.fim_linha == self.caracter:
                self.tabela_simbolos.append(["ID", self.lexema, self.numero_linha ,self.cabeca-1])
                self.lexema = ''
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["ID", self.lexema, self.numero_linha ,self.cabeca-1])
                self.lexema = ''
                self.q0()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["ID", self.lexema, self.numero_linha ,self.cabeca-1])
                self.lexema = ''
                self.cabeca -= 1
                self.q0()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

        def q56(self):
            # Comando ATRIBUICAO - = #
            self.caracter = self.obter_caracter()
            if self.fim_linha == self.caracter:
                self.tabela_simbolos.append(["=", self.lexema, self.numero_linha ,self.cabeca-1]) #ULTIMO NUMERO COLUNA VERIFICAR DPOIS
                self.lexema = ''
            elif self.caracter.isspace():
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["=", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.q0()
            elif self.caracter in self.especiais:
                self.lexema = self.lexema[:len(self.lexema)-1]
                self.tabela_simbolos.append(["=", self.lexema, self.numero_linha ,self.cabeca-1])           
                self.lexema = ''
                self.cabeca -= 1
                self.q0()
            elif self.caracter.isdigit() or self.caracter.islower():
                self.q55()
            else:
                print("Erro Léxico [{0},{1}]: Caracter {2} inesperado".format(self.numero_linha,self.cabeca,self.caracter))
                exit()

    '''tabela_tokens = lexico(sys.argv[2]).tabela_tokens()

    if(sys.argv[1] == '-lt'):
        print("\n[TOKENS,LEXEMA,LINHA,COLUNA]")
        for token in range(len(tabela_tokens)):
            print(tabela_tokens[token])'''
except:
    print()