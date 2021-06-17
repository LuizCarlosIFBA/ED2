class Hash:

     def __init__(self,tam):
          self.tab = {}
          self.tam_max = tam

     def funcaohash(self, chave):
          v = int(chave)
          return v%self.tam_max

     def cheia(self):
          return len(self.tab) == self.tam_max

     #def imprime(self):
      #    for i in self.tab:
       #        print("Hash[%d] = " %i, end="")
        #       print (self.tab[i])/

     def busca(self, chave):
          pos = self.funcaohash(chave)
          if self.tab.get(pos) == None: # se esta posição não existe
               return -1 #saida imediata
          if self.tab[pos] == chave: 
               return pos
          return -1

     def insere(self, item):
          if self.cheia():
               print("-> ATENÇÃO Tabela Hash CHEIA")
               return
          pos = self.funcaohash(item)
          if self.tab.get(pos) == None: # se posicao vazia
               self.tab[pos] = item
               #print("-> Inserido HASH[%d]" %pos)
          else: # se posicao ocupada
               print("-> Ocorreu uma colisao na posicao %d" %pos)             
# fim Classe Hashlinear

tamanhoHash = 4
tab = Hash(tamanhoHash)

tab.insere(3)
tab.insere(2)
tab.insere(1)
tab.insere(0)

#Abrindo e grazando arquivo em uma matriz
arq = open('paises.txt', 'r')  #abre o arquivo
texto = []  #declaro um vetor
matriz = [] #declaro um segundo vetor
texto = arq.readlines() #quebra as linhas do arquivo em vetores 

def gravarMatriz():
    for i in range(len(texto)):          #esse for percorre a posições dp vetor texto
        matriz.append(texto[i].split())  #aqui eu quebro nos espasos das palavras
    arq.close() #comando para fechar o arquivo
gravarMatriz()   
#

def resultBusca(num):
    pos = tab.busca(num)
    if pos == -1:
        print("Item nao encontrado")
    else:
        print("Item encontrado: ",matriz[pos])

qtd = 2
for x in range(qtd):
    resultBusca(x)

print("\nMédia de leitura na busca: ",tamanhoHash/qtd)    
print("\n")
