def steal_money(n, m, denominations):
    denominations.sort(reverse=True)
    stolen = []
    for denom in denominations:
        while n >= denom:
            n -= denom
            stolen.append(denom)
    if n == 0:
        return len(stolen), stolen
    else:
        return -1
n, m = map(int, input().split())
denominations = list(map(int, input().split()))
result = steal_money(n, m, denominations)
if result == -1:
    print(-1)
else:
    k, stolen = result
    print(k)
    print(*sorted(stolen))