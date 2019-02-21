from timeit import timeit
import itertools as it


def insertionSort(arr): 
      for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
  
listapermuta = list(it.permutations([1,2,3,4,5,6],6))
permutimes=[]

for i in listapermuta:
  inicio = list(i)
  permutimes.append(timeit("insertionSort({})".format(inicio),setup="from __main__ import insertionSort",number=1))

menortempo = min(permutimes)
maiortempo = max(permutimes)

menortempoindex = permutimes.index(menortempo)
maiortempoindex = permutimes.index(maiortempo)

print("Menor tempo:",permutimes[menortempoindex])
print("Maior tempo:",permutimes[maiortempoindex])



from timeit import timeit
import itertools as it


def insertionSort(arr): 
      for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
  
listapermuta = list(it.permutations([1,2,3,4,5,6],6))
permutimes=[]

for i in listapermuta:
  inicio = list(i)
  permutimes.append(timeit("insertionSort({})".format(inicio),setup="from __main__ import insertionSort",number=1))

menortempo = min(permutimes)
maiortempo = max(permutimes)

menortempoindex = permutimes.index(menortempo)
maiortempoindex = permutimes.index(maiortempo)

print("Menor tempo:",permutimes[menortempoindex])
print("Maior tempo:",permutimes[maiortempoindex])



