def selectionSort(arrayList):
    size = len(arrayList)
    if(size>0):
        for i in range(0, size):
            minIndex = i
            for j in range(i+1, size):
                if(arrayList[j]<arrayList[minIndex]):
                    swap(arrayList, j, i)

    return arrayList #there is one element!

def swap(arrayList, indexA, indexB):
    aux = arrayList[indexA]
    arrayList[indexA] = arrayList[indexB]
    arrayList[indexB] = aux
    
#Example
list = [1,2,-4,3,2,30,-23]
print(selectionSort(list))
