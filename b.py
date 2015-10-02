import sys
m, n = map(int, raw_input().split(","))
a = []
for i in range(m):
    a.append(map(int, raw_input().split(",")))
res = []
i1, j1, i2, j2 = 0, 0, m-1, n-1
while i1 <= i2 and j1 <= j2:
    if i1 <= i2 and j1 <= j2:
        res.extend(a[i1][j] for j in range(j1,j2+1))
        i1 += 1
    if i1 <= i2 and j1 <= j2:
        res.extend(a[i][j2] for i in range(i1,i2+1))
        j2 -= 1
    if i1 <= i2 and j1 <= j2:
        res.extend(a[i2][j] for j in range(j2,j1-1,-1))
        i2 -= 1
    if i1 <= i2 and j1 <= j2:
        res.extend(a[i][j1] for i in range(i2,i1-1,-1))
        j1 += 1
print ",".join(map(str,res))

