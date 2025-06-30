def sum_list(numbers):
    if not numbers:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])

numbers = [2, 4, 6]
total = sum_list(numbers)
print("The sum of the list elements is:", total)
