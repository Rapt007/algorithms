def insertion_sort(array):
    for i in range(1,len(array)):
        for j in range(i):
            if(array[i]<array[j]):
                temp=array[j]
                array[j]=array[i]
                array[i]=temp
    return array
array=[64,25,12,22,28]
sorted_array=insertion_sort(array)
print sorted_array