m=int(input("enter the start range: "))
n=int(input("enter the end range: "))
list=[]
for num in range(m,n):
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
            list.append(num)
            list.sort(reverse=True)
print(list)
