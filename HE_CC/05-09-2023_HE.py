t = int(input())
for _ in range(t):
    f, d = map(int, input().split())
    ans = [0]*d
    for i in range(f):
        data = input()
        dl = []
        dl.extend(data)
        if ans.count(1) < d:
            for j in range(d):
                ans[j] = ans[j] | int(dl[j])

        """
        if len(str(bin(ans)))>d+2:
            ans = ans%(2**(d-1))
        """

    print(*ans)
    print(ans.count(1))
