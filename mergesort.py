from __future__ import division


def merge(a, low, mid, high):
    n = mid - low + 1
    m = high - mid
    left = []
    right = []
    for i in range(n):
        left.append(a[low + i])
    for j in range(m):
        right.append(a[mid + 1 + j])
    i = 0
    j = 0
    k = low
    while (i < n and j < m):
        if (left[i] >= right[j]):
            a[k] = right[j]
            j = j + 1

        else:
            a[k] = left[i]
            i = i + 1

        k = k + 1

    while (i < n):
        a[k] = left[i]
        i = i + 1
        k = k + 1

    while (j < m):
        a[k] = right[j]
        j = j + 1
        k = k + 1


def mergesort(a, low, high):
    if (high > low):
        mid = low + (high - low) // 2
        mergesort(a, low, mid)
        mergesort(a, mid + 1, high)
        merge(a, low, mid, high)


a = [65, 22, 12, 11, 25]
low = 0
high = len(a) - 1
mergesort(a, low, high)
print a
