n=int(input("Enter the number: "))
m=int(input("Enter the range: "))
sum=0
for i in range(m):
    numerator=n ** 2 ** i
    denominator=2 *i+1
    sign= -1 ** i
    term=numerator/denominator *sign
    sum+=term
print(sum)