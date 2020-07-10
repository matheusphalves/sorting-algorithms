import time
def bubbleSort(array):
    size = len(array)
    for i in range(size): #iteração atual
        for j in range(size-1):
            # size-1 -> Dessa forma, podemos efetuar j+i sem ultrapassar array
            #a cada iteração, temos o maior elemento no mais extremo
            if(array[j] > array[j+1]):
                swap(array, j+1, j)
    return array;

def bubbleBetterSort(array):
    size = len(array)
    for i in range(size): #iteração atual
        for j in range(size-1 -i):
            # size-1 -> Dessa forma, podemos efetuar j+i sem ultrapassar array
            #a cada iteração, temos o maior elemento no mais extremo
            if(array[j] > array[j+1]):
                swap(array, j+1, j)
    return array;

def swap(arrayList, indexA, indexB):
    aux = arrayList[indexA]
    arrayList[indexA] = arrayList[indexB]
    arrayList[indexB] = aux       

list = [1,2,-4,3,-24,2,30,-23]
#Regular bubble sort
start = time.time()
print(bubbleSort(list))
finish = time.time()
print('Regular bubble sort time (ms)', str(1000*(finish-start)))
#Fast bubble sort
start = time.time()
print(bubbleBetterSort(list))
finish = time.time()
print('Fast bubble sort time (ms)', str(1000*(finish-start)))