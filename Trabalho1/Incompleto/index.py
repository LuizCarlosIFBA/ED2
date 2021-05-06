import hasher     
import hashlib
import csv

#Menu de operações para segundo trabalho da disciplina Estrutura de Dados II - Tabelas Hash
def Menu(funcoes):
    global jump_count

    print('Digite:')
    print('Insert - para inserir um novo registro a tabela')

    print('Exit - Para interromper execução do programa')
    
    option = input('Digite uma opção: ')
    option = option.lower()
    if option == 'exit':
        return 'Sair'
    jump_count =0


    print(funcoes[option]())
    print("Numero de acessos a tabela foi:", jump_count)

    

#Gerenciamento e autenticação de usuarios utilizando tabela hash
funcoes = {'insert':hasher.SetReg, 'catch':hasher.CatchReg,  'weight':hasher.WeightTable}
hasher.n_users = int(input('O numero de registros esperados para o sistema é: '))
hasher.hash_table = hasher.MakeTable()
Count = 2
while Menu(funcoes) != 'Sair':
    hasher.WriteLog(hasher.hash_table)
    Count = Count -1
