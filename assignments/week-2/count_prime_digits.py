number=input("Enter the number")
prime_digits=[2,3,5,7]
count=0
for digit in number:
    digit=int(digit)
    if digit in prime_digits:
        count+=1
print("total number of prime digits in the number are",count)