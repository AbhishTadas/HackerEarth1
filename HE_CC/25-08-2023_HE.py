
n = int(input())
narr = set(x for x in range(2, n // 2 + 1) if n % x == 0)
t = int(input())
arr = list(map(int, input().split()))
count = 0

for i in arr:
    test = set(x for x in range(2, i // 2 + 1) if i % x == 0)
    if test & narr:
        count = count + 1

print(count)