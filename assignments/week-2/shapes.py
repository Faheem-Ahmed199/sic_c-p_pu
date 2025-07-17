# right angled triangle
n=5
for i in range(n):
    for j in range(i+1):
        print("* ",end=" ")
    print()
print("-------------------------------")
#equilateral triangle
for i in range(n):
    for j in range(i,n):
        print(' ',end=" ")
    for j in range(i):
        print('*',end=" ")
    for j in range(i+1):
        print('*',end=" ")
    print()
print("----------------------------------------------")

#hollow square
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or  j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

print("-------------------------------------------")
# X IN HOLLOW SQUARE

for i in range(n):
    for j in range(n):
            # Borders
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end=" ")
            # Diagonals (X shape)
        
        elif i == j or i+j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("----------------------------------------------------")
# X SHAPE
for i in range(n):
    for j in range(n):
            # Borders
        
        if i == j or i+j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

