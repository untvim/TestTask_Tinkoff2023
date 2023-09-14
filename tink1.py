n, s = map(int, input().split())
a = list(map(int, input().split()))

max_price = 0

for i in range(n):
    if a[i] <= s and a[i] > max_price:
        max_price = a[i]

print(max_price)