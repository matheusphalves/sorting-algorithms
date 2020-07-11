import time


def quickSort(array):  
    n = len(array)
    if(n>1): #deve existir ao menos dois elementos para ordenar
        pivot = array[-1]#pivô escolhido: Elementos à esquerda menores e à direita maiores
        k = -1 #indice mais à direita
        #print(f"Pivot is: {pivot}")
        for i in range(0, n):
            if(array[i]<= pivot):
                 #incremento no indice menor que pivô
                k = k+1
                array[i], array[k] = array[k], array[i]   #swap entre elementos       
                #swap(array, i, k) #é feita troca entre elementos
        #print(array)
        left = quickSort(array[:k])#metades são enviadas para ordenação
        right = quickSort(array[k+1:]) 
        return left + [array[k]] + right
    return array

def swap(arrayList, indexA, indexB):
    aux = arrayList[indexA]
    arrayList[indexA] = arrayList[indexB]
    arrayList[indexB] = aux


list = [4,3,2,10,12,-1,5,-6]
list2 = [1,2,-4,3,2,30,-23]
list3 = [1,2,-4,-25,2, -15,30,-30,-23]
#list4 = [1,2,-4,-25,2, 30,-23]
list5 = [75, 26, 15, 67, 85, 54, 31, 49]

#print(swap(list, 0, -1))

start = time.time()
print(quickSort(list5))
finish = time.time()
print('Regular quick sort time (ms)', str(1000*(finish-start)))

