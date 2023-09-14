def can_get_winning_sequence(n, a, b):
    l = 0
    r = n - 1
    while l < n and a[l] == b[l]:
        l += 1
    while r >= 0 and a[r] == b[r]:
        r -= 1
    if l > r:
        return "YES"
    sorted_a = sorted(a[l:r+1])
    sorted_b = sorted(b[l:r+1])
    if sorted_a == sorted_b and a[:l] + sorted_a + a[r+1:] == b:
        return "YES"
    else:
        return "NO"

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = can_get_winning_sequence(n, a, b)

print(result)