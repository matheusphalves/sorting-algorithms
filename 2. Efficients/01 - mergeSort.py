import time
#A cada iteração, o array é dividido em duas metades
def mergeSort(array):
    if(len(array)>1): #deve haver no mínimo dois elementos para dividir
        n = len(array)//2
        leftList =array[0:n] 
        rightList = array[n:]
        return merge(mergeSort(leftList), mergeSort(rightList))
    else:
        return array #retornando único elemento

def merge(array1, array2):
    auxArray = []
    #durante a recursão, listas maiores que 1 estarão ordenadas. Condição para que o algoritmo funcione corretamente.
    while(len(array1)>0 and len(array2)>0): #Encontramos os elementos minimos em cada subsequencia e então os comparamos
        if(array1[0]<array2[0]):
            auxArray.append(array1[0])
            array1.pop(0)
        else:
            auxArray.append(array2[0])
            array2.pop(0)

    for i in array1:
        auxArray.append(i)
    for j in array2:
        auxArray.append(j)

    return auxArray
        
list = [4,3,2,10,12,-1,5,-6]
list2 = [1,2,-4,3,2,30,-23]

start = time.time()
print(mergeSort(list))
finish = time.time()
print('Regular insertion sort time (ms)', str(1000*(finish-start)))

