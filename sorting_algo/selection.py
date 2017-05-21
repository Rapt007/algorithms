def selectionsort(unsorted):
    sort=[]
    while(len(unsorted)>=1):
        index=unsorted.index(min(unsorted))
        temp=unsorted[0]
        unsorted[0]=unsorted[index]
        unsorted[index]=temp
        sort.append(unsorted[0])
        unsorted.remove(unsorted[0])
    return sort
unsorted=[64,25,12,22,11]
sorted_array=selectionsort(unsorted)
print sorted_array