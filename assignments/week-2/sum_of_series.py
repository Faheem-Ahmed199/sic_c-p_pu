n = int(input("Enter the number: "))
m = int(input("Enter the range: "))
total_sum = 0
sign = -1

for i in range(m):
    numerator = n ** (2 ** i)
    denominator = 2 * i + 1
    sign = -1 * sign
    term = numerator / denominator * sign
    total_sum += term

print(total_sum)
