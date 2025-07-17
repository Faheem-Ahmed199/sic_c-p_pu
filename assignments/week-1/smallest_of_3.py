number_1=int(input("Enter the 1st number: "))
number_2=int(input("Enter the 2nd number: "))
number_3=int(input("Enter the 3rd number: "))
if number_1<number_2 and number_1<number_3:
    print(number_1,"is the smallest")
elif number_2<number_1 and number_2<number_3:
    print(number_2,"is the smallest")
elif number_3<number_1 and number_3<number_2:
    print(number_3,"is the smallest")