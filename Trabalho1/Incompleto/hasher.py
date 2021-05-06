import hashlib
import csv

#Quantidade de registros
def CousinValue(n_registros):
    if(n_registros %2) == 0:
        n_registros +=1
    for cousin_verifier in range(3,n_registros,2):
        if(n_registros % cousin_verifier) == 0:
            n_registros +=2
            return CousinValue(n_registros)
    return n_registros
    
#Cria tabelas
def MakeTable():
    #Table Hash -> Dicionario da forma hash_table = {'h_index':('cod_hash', 'nome','continente','subcontinente')}
    hash_table = {}
    n_registros = n_users + (n_users //2)
    n_registros = CousinValue(n_registros)
    print('\nNumero de registros na tabela é: {}\n'.format(n_registros))
    for index in range(n_registros):
        hash_table[index] = (None, None, None, None)
    return hash_table

#Defini rash
def HashIt(nome, continente):
    cod_hash = hashlib.md5((nome + continente).encode())
    cod_hash = cod_hash.hexdigest()
    cod_hash = int(cod_hash, 16)
    return cod_hash

def InsertReg(nome, continente, subcontinente):
    global hash_table
    global jump_count
    cod_hash = HashIt(nome, subcontinente)

    if CheckReg(cod_hash, continente, subcontinente):
        return ('Já existe um registro com essas informações na tabela') 

    jump_count =0
    index = cod_hash % n_users
    jumper = (cod_hash // n_users) % n_users
    if jumper == 0:
        jumper =1
    print('O indice gerado foi - {} - \nO jump para colisao - {} -'.format(index,jumper))
    index = SearchIndex(len(hash_table), index, jumper, index, 'inserção')
        
    #if  CheckIndex(index,'inserção'):
    if  CheckIndex(index,'inserção'):
        #hash_table[index] = (cod_hash, user_login, len(user_pswd) *'*', user_type)
        hash_table[index] = (cod_hash, continente, subcontinente)        
        
        #Debugging
        #return (True, user_login, index, jumper)
        return ('Registro inserido')
    
    else:
        return ('Não existem mais registros vazios na tabela')


def SetReg():
    nome = input('Informe nome do páis: ')
    continente = input('Informe o nome do continente: ')
    subcontinente = input('Informe o subcontinente: ')
    ClScreen()
    return InsertReg(nome, continente, subcontinente)


def DelReg(nome, continente):
    global hash_table
    cod_hash = HashIt(nome, continente)
    index = cod_hash % n_users
    jumper = (cod_hash // n_users) % n_users
    index = SearchIndex(len(hash_table), index, jumper, index, cod_hash)

    if cod_hash and nome in hash_table[index][:2]:
        hash_table[index] = ('Some','None','None','None')
        return True

    return False

def DelIndex(index):
    global hash_table
    if not CheckIndex(index,'inserção'):
        hash_table[index] = ('Some','None','None','None')
        return True

    return False

def CheckIndex(index, arg):
    #A função recebe o indice a ser conferido e um argumento que indica o que deve ser buscado neste indice
    #caso o argumento seja 'inserção' então se busca por um indice vazio para inserção
    #caso contrario se busca pelo proprio argumento como valor contido no indice informado
    global hash_table
    if arg == 'inserção':
        return bool(hash_table[index][0] in [None, 'Some'])
    else:
        return bool(hash_table[index][0] == arg)

def CheckReg(cod_hash, nome, continente):
    #Verifica se os dados inseridos estão contidos na tabela, realizando os saltos necessarios
    global hash_table
    cod_hash = HashIt(nome, continente)
    index = cod_hash % n_users
    jumper = (cod_hash // n_users) % n_users
    index = SearchIndex(len(hash_table), index, jumper, index, cod_hash)

    if cod_hash and nome in hash_table[index][:2]:
        return True
    return False

def SearchIndex(len_table, index, jumper, new_index, arg):
    #print("ACCESS", new_index)
    JumpCounter()
    if CheckIndex(new_index, arg):
        return new_index

    new_index += jumper
    if new_index >= len_table:
        new_index -= len_table
    
    if new_index == index:
        return new_index
    
    return SearchIndex(len_table, index, jumper, new_index, arg)



def CatchReg():
    #Leitura de registros através do seu indice ou dados contidos

    opcao = input('captura por indice ou por registro?\n: ')
    opcao = opcao.lower()

    #leitura de Registro Atraves do indice
    if opcao == 'indice':
        JumpCounter()
        index = int(input('\nIndice do registro a ser capturado é: '))
        return GetByIndex(index)
    
    #Leitura de Registro Atraves de busca dos dados
    else:
        nome = input('Informe o nome do país: ')
        continente = input('Informe o continente: ')
        return GetByReg(nome, continente)

    return None

def GetByIndex(index):
    global hash_table
    if not CheckIndex(index,'inserção'):
            return hash_table[index]

    return 'Indice de Registro Inexistente'

def GetByReg(nome, continente):
    global hash_table
    cod_hash = HashIt(nome, continente)
    index = cod_hash % n_users
    jumper = (cod_hash // n_users) % n_users
    index = SearchIndex(len(hash_table), index, jumper, index, cod_hash)

    if cod_hash and user_login in hash_table[index][:2]:
        return hash_table[index]

    return 'Dados de Registro Inexistente'

#inforamções sobre quantidade de acessos e registros na tabela
def WeightTable():
    #Cálculo do fator de ocupação da tabela hash - n_reg preenchidos / n_reg totais
    global hash_table
    weight = 0.0
    for counter in range(len(hash_table)):
        if hash_table[counter][0] not in ['Some',None]:
            weight += 1
    return ("{:.0%}".format(weight / len(hash_table)))

jump_count =0
def JumpCounter():
    #Contador de acessos a indices da lista numa operação de inserção, remoção ou captura de registros
    global jump_count
    jump_count = jump_count +1

def WriteLog(tabela):
    with open("TabelaHash.csv",'w+', newline ='') as logfile:
        gravar_dados = csv.writer(logfile, delimiter ='\n')
        gravar_dados.writerow([(index,campo) for index,campo in zip(tabela.keys(),tabela.values())])

def ClScreen():
    import os
    pause = input('\nPressione uma tecla para continuar')
    os.system('cls' if os.name == 'nt' else 'clear')
      
