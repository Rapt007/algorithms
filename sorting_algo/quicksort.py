def quick_sort(array, low, high):
    if (high > low):
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)


def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if (array[j] <= pivot):
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[high], array[i + 1] = array[i + 1], array[high]
    return i + 1


array = [65, 22, 11, 13, 12]
low = 0
high = len(array) - 1
quick_sort(array, low, high)
print array