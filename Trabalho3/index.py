import pandas as pd
import numpy as np

def binary_search(array, item, begin=0, end=None):
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

vet = [4,5,6];#vetor auxiliar

mydata = pd.read_csv("Municipios.csv")
mydata_array = np.array(mydata)
print(mydata_array[binary_search(vet, 4)])#busca por chave numérica





