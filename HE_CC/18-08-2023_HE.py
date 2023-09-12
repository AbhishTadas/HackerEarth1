#https://www.hackerearth.com/practice/data-structures/disjoint-data-strutures/basics-of-disjoint-data-structures/practice-problems/algorithm/city-and-flood-1/submissions/
from sys import stdin

read = stdin.readline
n = int (read().strip())
data = [i for i in range(1,n+1)]
k = int (read().strip())
for i in range(k):
    a,b = map(int , read().split())
    data.remove(b)

print(len(data))