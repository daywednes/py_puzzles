import sys
n = int(sys.stdin.readline())
for test in range(n):
    s = " " + sys.stdin.readline().strip().lower() + " "
    l, r = 1, len(s) - 2
    while l < r:
        if s[l] == s[r]:
            l, r = l + 1, r - 1
        elif s[l:r] == s[r-1:l-1:-1]:
            print(r-1)
            break
        elif s[l+1:r+1] == s[r:l:-1]:
            print(l-1)
            break
        else:
            pass
    if l >= r:
        print(-1)
