def heapbuild(a, n, i):
    root = i
    left = 2 * i + 1
    right = 2 * i + 2
    if (left < n and a[left] > a[root]):
        a[left], a[root] = a[root], a[left]
        root = left
        heapbuild(a, n, root)
    elif (right < n and a[right] > a[root]):
        a[right], a[root] = a[root], a[right]
        root = right
        heapbuild(a, n, root)


def heapsort(a):
    for i in range(n - 1, 0, -1):
        a[i], a[0] = a[0], a[i]
        heapbuild(a, i, 0)


a = [4, 10, 3, 5, 1]
n = len(a)
for i in range(n - 1, -1, -1):
    heapbuild(a, n, i)
heapsort(a)
print a