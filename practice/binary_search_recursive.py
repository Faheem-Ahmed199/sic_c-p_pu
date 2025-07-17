def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1  

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


numbers=[1,2,5,4,6,7,9]
target = 9

result = binary_search_recursive(numbers, target, 0, len(numbers) - 1)
if result !=-1:
    print("found at index",result)
else:
    print("not found")
