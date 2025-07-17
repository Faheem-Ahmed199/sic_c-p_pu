def binary_search(array,element):
    left,right=0,len(array)-1

    while left<=right:
        mid=(left+right)//2

        if array[mid]==element:
            return mid
        elif array[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
    return -1
numbers=[1,2,5,4,6,7,9]
numbers.sort()
element=6
result=binary_search(numbers,element)
if result !=-1:
    print("found at index",result)
else:
    print("not found")