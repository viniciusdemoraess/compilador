import argparse
from AnaliseLexica import lexico
from AnaliseSintatica import Sintatico
from AnaliseSemantica import Semantico

def analise_lexica(args):
    tabela_tokens = lexico(args).tabela_tokens()
    return tabela_tokens

def analise_sintatica(args):
    tokens = analise_lexica(args)
    analisador_sintatico = Sintatico(tokens)
    analisador_sintatico.verificacao_sintatica()
    return analisador_sintatico

def analise_semantica(args):
    tokens = analise_lexica(args)
    analise_sintatica(args)
    analisador_semantico = Semantico(tokens)
    analisador_semantico.analysis()
    return analisador_semantico 

def tabela_simbolos_semantico(args):
    analisador_semantico = analise_semantica(args)
    analisador_semantico.table_symbol()


def log_lexico(args):
    tabela_tokens = analise_lexica(args)
    print(" -=-"*20)
    print("\t\t\t       Análise Lexica")
    print(" -=-"*20)
    print("\n[TOKENS,LEXEMA,LINHA,COLUNA]")
    for token in range(len(tabela_tokens)):
        print(tabela_tokens[token])
    print('Termino Execução da Análise Léxica.......')

def log_sintatico(args):
    print(" -=-"*20)
    print("\t\t\t       Análise Sintática")
    print(" -=-"*20)
    analisador_sintatico = analise_sintatica(args)
    analisador_sintatico.log_operacoes()
    print('Termino da Execução da Análise Sintática.....')

def log_semantico(args):
    print(" -=-"*20)
    print("\t\t\t       Análise Semantica")
    print(" -=-"*20)
    analisador_semantico = analise_semantica(args)
    analisador_semantico.log_operacoes()
    print('Termino da Execução da Análise Semantica.....')



def log_tudo(args):
    log_lexico(args)
    log_sintatico(args)
    log_semantico(args)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=" Compilador em Fase de Construção")

    parser.add_argument('-ls', '--ls', help="Mostra o log do analisador sintático")
    parser.add_argument('-tudo', '--tudo', help="Mostra todas as listagens do Compilador")
    parser.add_argument('-lt', '--lt', help="Mostra a lista de tokens do analisador lexico")
    parser.add_argument('-lse', '--lse', help="Mostra o log do analisador semantico")
    parser.add_argument('-ts', '--ts', help="Exibe a tabela de simbolos")

    
args = parser.parse_args()

if args.ls:
    log_sintatico(args.ls)
elif args.tudo:
    log_tudo(args.tudo)
elif args.lt:
    log_lexico(args.lt)
elif args.lse:
    log_semantico(args.lse)
elif args.ts:
    tabela_simbolos_semantico(args.ts)


