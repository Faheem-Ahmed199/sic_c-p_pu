
n = int(input())
oranges = list(map(int, input().split()))

k = 0
last = oranges[n-1]

for i in range(n-1):
    if oranges[i] <= last:
        oranges[i], oranges[k] = oranges[k], oranges[i]
        k += 1

oranges[k], oranges[n-1] = oranges[n-1], oranges[k]


print(' '.join(map(str, oranges)))
