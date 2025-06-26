N = int(input("Enter the term number (N): "))

if N == 1:
    result = 1
elif N == 2:
    result = 2
else:
    a, b = 1, 2
    for i in range(3, N + 1):
        a, b = b, a + b
    result = b

print(f"The {N}th term in the HemaChandra Fibonacci sequence is: {result}")
