# Quick sort implementation with pivot at left most element


def quicksort(arr, left, right):
    if left < right:
        partition_position = partition(arr, left, right)
        quicksort(arr, left, partition_position - 1)
        quicksort(arr, partition_position + 1, right)


def partition(arr, left, right):
    i = left + 1
    j = right
    pivot = arr[left]

    while i < j:
        while i < right and arr[i] < pivot:
            i += 1

        while j > left and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    if arr[i] < pivot:
        arr[left], arr[i] = arr[i], arr[left]

    return i