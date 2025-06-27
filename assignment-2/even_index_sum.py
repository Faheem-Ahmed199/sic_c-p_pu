number = input("Enter a number: ")

even_sum = 0


for index in range(len(number)):

    if (index + 1) % 2 == 0:
        even_sum += int(number[index])

print(f"The sum of the even-placed digits is: {even_sum}")
