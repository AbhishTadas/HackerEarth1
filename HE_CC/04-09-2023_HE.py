t = int(input())
count = 0
arr=dict()
for _ in range (t):
    s = input()
    if s in arr:
        arr[s] += 1
    else:
        arr[s] = 1

for k,v in arr.items():
    if k[::-1] in arr:
        #if v*arr[k[::-1]]!=1:
        count+= v * arr[k[::-1]]
        print("key = ",k, " : value = ",v ," :: Reverse key = ",k[::-1], " : value = ",arr[k[::-1]])

print(int(count/2))