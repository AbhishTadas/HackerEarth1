# https://www.hackerearth.com/problem/algorithm/the-blessing-1/?utm_source=new_practice
t = int(input())
for _ in range (t):
    p, m = map(int, input().split())
    print(2*p + m*2)
