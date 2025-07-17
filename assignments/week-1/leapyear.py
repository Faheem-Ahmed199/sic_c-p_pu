year=int(input("Enter the year to check if is leap year: "))
if (year%4==0 and year%100!=0) or year%400==0:
    print(year," is a leap year")