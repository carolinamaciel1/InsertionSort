from random import randint
from timeit import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
import itertools as it


def geraLista(lista):
    newlista = []
    for i in range(lista):
        while len(newlista) != lista:
            n = randint(1,1*lista)
            if n not in newlista: newlista.append(n)
    return newlista

def desenhaGrafico(x,y,z,k,xl = "Elementos", yl = "Tempo"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Caso Medio")
    ax.plot(x,z, label = "Melhor Caso")
    plt.plot(x,k, label="Pior Caso")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()
    fig.savefig('InsertionSort.png')


def insertionSort(arr): 
      for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
  
CasoMedio=[]
MelhorCaso=[]
PiorCaso=[]

lista = list(it.permutations([1,2,3,4,5,6],6))
permutimes=[]

for i in range lista:
    permutimes.append(timeit("insertionSort({})".format(i),setup="from __main__ import insertionSort",number=1))

menortempo = max(permutimes)
maiortempo = min(permutimes)

menortempoindex = permutimes.index(menortempo)
maiortempoindex = permutines.index(maiortempo)


lista=[1000,2000,3000,4000,5000]

for i in lista:
    lista_gerada=geraLista(i)
    lista_ordenada_cres = sorted(lista_gerada)
    lista_ordenada_dec = sorted(lista_gerada,reverse=True)
    CasoMedio.append(timeit("insertionSort({})".format(lista_gerada),setup="from __main__ import insertionSort",number=1))
    MelhorCaso.append(timeit("insertionSort({})".format(lista_ordenada_cres),setup="from __main__ import insertionSort",number=1))
    PiorCaso.append(timeit("insertionSort({})".format(lista_ordenada_dec),setup="from __main__ import insertionSort",number=1))

#PARTE 1
desenhaGrafico(lista,CasoMedio,MelhorCaso,PiorCaso)




