def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  

    return arr

numbers = [234,43,213,3245,5256,231]
sorted_numbers = bubble_sort(numbers)

print("Sorted list:", sorted_numbers)
