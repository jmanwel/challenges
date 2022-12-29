def bubbleSort(l):
    n = len(l)
    for i in range(n):
        for j in range(n -i -1):
            if l[j] > l[j + 1]:
                temp = l[j]
                l[j] = l[j + 1]
                l[j + 1] = temp
    return l



