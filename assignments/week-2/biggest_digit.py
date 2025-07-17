number=input("Enter the number: ")
biggest_digit=0
for i in number:
    digit=int(i)
    if digit>biggest_digit:
        biggest_digit=digit
print(biggest_digit,"is the bigest digit in the number")
