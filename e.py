def ok(mid, h):
    cur = mid
    for elem in h:
        cur += cur - elem
        if cur < 0:
            return False
    return True
n = int(raw_input())
h = map(int, raw_input().split(" ")
l, r = 1, 100000
while l < r:
    mid = (l + r) / 2
    if ok(mid, h):
        r = mid
    else:
        l = mid + 1
print l
