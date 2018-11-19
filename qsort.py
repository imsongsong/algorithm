def partition(array, p, r):
    if p >= r:
        return
    pivot = array[r]
    i = p
    for j in range(p, r):
        if array[j] < pivot:
            tmp = array[i]
            array[i] = array[j]
            array[j] = tmp
            i = i + 1
    tmp = array[i]
    array[i] = array[r]
    array[r] = tmp

    partition(array, p, i-1)
    partition(array, i+1, r)


if __name__ == "__main__":
    array = [3, 1, 9, 7, 2, 5, 8, 0, 4]
    partition(array, 0, len(array)-1)
    print(array)
