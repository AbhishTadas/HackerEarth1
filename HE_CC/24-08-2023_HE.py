num = input()
count = 0
arr = [int(x) for x in num]
for x in range(len(arr)-1, -1, -1):
    if int(arr[x]) % 2 == 0:
        count = count + 1
    arr[x] = count

print(*arr, sep=" ")
