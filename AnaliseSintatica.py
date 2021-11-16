import sys

try:    
    class Sintatico:
        def __init__(self, tokens):
            
            
            self.pilha = ['$', 'VIN']

            self.tokens = list(tokens)
            self.tokens.append('$') #add ao final pra poder comparar com a pilha

            #mostrar os logs
            self.empilhamento = 0
            self.desempilhamento = 0
            self.reducao_pilha_lista = 0
            self.producoes_aplicadas = []

            self.arquivo = open("log_operacoes.txt",'w')

            self.producoes = {
                0 : ['programInitial', ';' , 'BLOCO', 'programFinish', ';'],
                1 : ['CORPOPROGRAMA', ';', 'BLOCO'],
                2 : [],
                3 : ['VARIAVEIS'],
                4 : ['ESCREVER'],
                5 : ['LER'],
                6 : ['CONDICIONAL'],
                7 : ['REPETICAO'],
                8 : ['EXPRESSIONMAT'],
                9 : ['=', 'VALOREXPRESSAO'],
                10 : ['NUMERO'],
                11 : [],
                12 : ['NUMERO', 'OPERADORESMAT'],
                13 : ['ID', 'OPERADORESMAT'],
                14 : ['(', 'VALOREXPRESSAO', ')', 'OPERADORESMAT'],
                15 : ['varInt', 'ID', 'ATRIBUICAO'],
                16 : ['ID', 'ATRIBUICAO'],
                17 : ['+', 'VALOREXPRESSAO'],
                18 : ['-', 'VALOREXPRESSAO'],
                19 : ['*', 'VALOREXPRESSAO'],
                20 : ['/', 'VALOREXPRESSAO'],
                21 : [],
                22 : ['escrever', '(', 'ID', ')'],  #MINUSCULO
                23 : ['ler', '(', 'ID', ')'],
                24 : ['SE', 'ENTAO', 'SENAO', 'FIMSE'],
                25 : ['se', '(', 'EXPRESSION_LOGICA', ')'],
                26 : ['entao', 'BLOCO'],
                27 : ['ID'],
                28 : ['NUMERO'],
                29 : ['=='],
                30 : ['>'],
                31 : ['LETRANUMBER', 'OPERADORLOGICO', 'LETRANUMBER'],
                32 : ['senao', 'BLOCO'],
                33 : [],
                34 : ['fimse'],
                35 : ['REPITA', 'BLOCO', 'ENQUANTO', '(', 'EXPRESSION_LOGICA', ')'],
                36 : ['repita'],
                37 : ['enquanto']
            }

            self.nao_terminais = {
                'VIN' : [0],
                'BLOCO' : [1, 2],
                'CORPOPROGRAMA' : [3, 4, 5, 6, 7, 8],
                'ATRIBUICAO' : [9, 10, 11],
                'VALOREXPRESSAO' : [12, 13, 14],
                'VARIAVEIS' : [15],
                'EXPRESSIONMAT' : [16],
                'OPERADORESMAT' : [17, 18, 19, 20, 21],
                'ESCREVER' : [22],
                'LER' : [23],
                'CONDICIONAL' : [24],
                'SE' : [25],
                'ENTAO' : [26],
                'LETRANUMBER' : [27, 28],
                'OPERADORLOGICO' : [29, 30],
                'EXPRESSION_LOGICA' : [31],
                'SENAO' : [32,33],
                'FIMSE' : [34],
                'REPETICAO' : [35],
                'DO' : [36],
                'WHILE' : [37]
            }

            self.terminais = {
                ';' : [2, 11, 21, 33],
                '(' : [14],   
                ')' : [2, 21],
                '+' : [17],
                '*' : [19],
                '/' : [20],
                '-' : [18],
                '=' : [9],
                '==' : [29],
                '>' : [30],
                'NUMERO' : [10,12,28,31],
                'ID' : [1, 8, 13, 16, 27, 31],
                'programInitial': [0],
                'programFinish': [2, 11, 21, 33],
                'REPITA': [1, 7, 35,36],
                'ENQUANTO' : [2 ,37],
                'varInt' : [1, 3, 15],
                'escrever' : [1,4,22],
                'ler' : [1,5,23],
                'se' : [1, 6, 24, 25],
                'entao' : [26],
                'senao' : [2, 32,33],
                'fimse' : [2, 11, 21, 33, 34] 
            }

        def verificacao_sintatica(self):      
            while( len(self.tokens) != 0 and len(self.pilha) != 0):
                
                if len(self.tokens) == 1 and len(self.pilha) > 1:
                  
                    print("Erro Sintático: Pilha sintática possui dados e lista sintática  está vazia [erro ao executar análise] ", self.pilha )
                    sys.exit()   
                if len(self.tokens) > 1 and (self.pilha) == 1:   
                    print("Erro Sintático: Lista sintática possui dados e pilha sintatica vazia [erro ao executar análise]", self.tokens)               
                    sys.exit()
                if self.tokens[0][0] == self.pilha[-1]:
                    
                    self.reg_operacoes(3,-1)
                    del self.tokens[0]  
                    self.pilha.pop()  
                    self.reducao_pilha_lista += 1
                    self.desempilhamento += 1    
                else:
                    self.tabela_sintatica()            
            #print("Analise Sintática Executada Corretamente!")
            self.arquivo.close()

        #Método para verificar regras de produção
        def tabela_sintatica(self):
            try:
                producao = self.verifica_producao()
                

            except:
                #print('Erro Sintático: era esperado o valor {0} na linha {1} coluna {2}'.format(self.pilha[-1], self.tokens[0][2], self.tokens[0][3]))
                print("Erro Sintático: não possível encontrar uma producao válida para o valor '{0}' na linha {1} e coluna {2}.[erro ao executar análise]".format(self.tokens[0][1], self.tokens[0][2], self.tokens[0][3]))
                sys.exit()
            else:
                self.aplica_producao(producao)

        #Metodo reponsavel por verificar se existe producao válida
        def verifica_producao (self):
            
            producao = []  

            x, y = self.valor_producao()            

            producao = list(set(x).intersection(y)) 
          
            
            return producao[0]
        
   
        #Método responsabel por retornar a chave dos dicionarios.
        def valor_producao(self):        
            key_stack  = [-1] 
            key_list = [-1]  

            #Procurando na Pilha       
            for i in self.nao_terminais.keys():  
                if i == self.pilha[-1]:           
                    key_stack = self.nao_terminais[i]               
        
            #Procurando na Lista.       
            for j in self.terminais.keys():        
                if j == self.tokens[0][0]:
                    key_list = self.terminais[j]
                    
            return (key_stack,key_list)       
                    
        
        def aplica_producao(self, producao):
            try:
                valor_producao = self.producoes[producao]



                self.producoes_aplicadas.append(producao)            
            
                self.reg_operacoes(1, producao)
                self.pilha.pop()  
                self.desempilhamento += 1

                #producoes vazias 2, 11, 21, 33
                if any([valor_producao != 2, valor_producao != 11, valor_producao != 21, valor_producao != 33]):                     
                    
                    for i in reversed(valor_producao):                    
                        self.pilha.append(i)
                        self.empilhamento += 1
                        self.reg_operacoes(2, producao)
                
            except:
                print("Erro Sintático: nao foi possivel encontrar uma producao valida para o valor  {0} na linha {1} e coluna {2}. [erro ao executar análise]".format(self.tokens[0][1], self.tokens[0][2], self.tokens[0][3]))            
            
        def reg_operacoes(self,n, producao):
        
            #Desempilhamento
            if n == 1:
                self.arquivo.write("DESEMPILHANDO:...... Topo Pilha: {0} ->  producao a ser inserida {1}. \n".format(self.pilha[-1], producao))
            #Empilhamento
            elif n == 2:
                self.arquivo.write("EMPILHANDO:......... Topo Pilha: {0} -> producao aplicada {1}. \n".format(self.pilha[-1], producao))
            #Reducao
            elif n ==3:  
                self.arquivo.write("REDUCAO APLICADA:.... Topo Pilha: {0} First List: {1}\n".format(self.pilha[-1],self.tokens[0][0] ))
        
            
        def log_operacoes (self):
            #self.verificacao_sintatica()
            print(" -=-"*20)
            print("\t\t\t       LOG DE OPERACOES")
            print(" -=-"*20)
            print("Empilhamentos.........................:",self.empilhamento)
            print("Desempilhamento.......................:", self.desempilhamento)
            print("Producoes utilizadas..................:", self.producoes_aplicadas)
            print("Redução de Pilha e Lista..............:", self.reducao_pilha_lista)
            print("Quantidade de producoes utilizadas ...:", len(self.producoes_aplicadas))
            print(" -=-"*20)
            arquivo = open("log_operacoes.txt","r")
            for linha in arquivo:
                linha = linha.rstrip()
                print (linha)
            arquivo.close()
except:
    print('Deu Ruim')


