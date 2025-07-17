def factorial(number):
    
    if number ==0 or number==1:
        return 1
    else:
        return number*factorial(number-1)
number=int(input("enter the number: "))
print("the factorial of the number is ",factorial(number))