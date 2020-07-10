import time
def insertionSort(array):
    size = len(array)
    if(size>1):
        for i in range(1,size):#existe ao menos 2 elementos para ordenar!
            j = i-1 #índice dos elementos a serem comparados à esquerda
            actualKey = array[i] #elemento atual que será comparado

            while(j>=0 and actualKey < array[j]):
                array[j+1] = array[j] #cópia de elemento para a direita
                #o nosso elemento está salvo em actualKey
                j -= 1 #indo para próximo elemento à esquerda
                #j+1 pois elemento foi decrementado -1 antes de sair do while
            array[j+1] = actualKey #elemento é inserido na posição correta]
    return array

#Example
#list = [1,2,-4,3,2,30,-23]
list = [4,3,2,10,12,-1,5,-6]
start = time.time()
print(insertionSort(list))
finish = time.time()
print('Regular insertion sort time (ms)', str(1000*(finish-start)))


