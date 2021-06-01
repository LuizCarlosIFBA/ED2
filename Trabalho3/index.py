import pandas as pd
import numpy as np

#busca por indice numérico
def binary_search(array, item, begin=0, end=None):
    if item<4 or item>6:
            print("Não encontrado")
            sys.exit()  
    if end is None:
        end = len(array)-1
    if begin <= end:
        m = (begin + end)//2
        if array[m] == item:
            return m
        if item < array[m]:
            return binary_search(array, item, begin, m-1)
        else: 
            return binary_search(array, item, m+1, end)     
    return None       

#busca por indice alfabético

def binary_search_city(name):
    item = 0
    if name =="Cerejeiras":
            item = 4
    else: 
        if name == "Colorado do Oeste":
                item = 5      
        else: 
            if name == "Corumbiara":
                    item = 6                
            else:
                 print("Não encontrado")
                 sys.exit()      
    return item       


vet = [4,5,6];#vetor auxiliar

mydata = pd.read_csv("Municipios.csv")
mydata_array = np.array(mydata)

print("\nBusca por chave numérica:\n")
print(mydata_array[binary_search(vet, 5)])#busca por chave numérica
print("\nBusca por chave alfabética:\n")
print(mydata_array[binary_search(vet, binary_search_city("Cerejeiras"))])#busca por chave alfabética
print("\nBusca por letra:\n")
print(mydata.query('"S" <= Municipio <= "S~"'))#busca por letra


