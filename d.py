from operator import mul

n = int(raw_input())
ap = [tuple(map(int, raw_input().split(" "))) for _ in range(n)]
ap.insert(0, ())
q = int(raw_input())
N = 20
for _ in range(q):
    query = map(int, raw_input().split(" "))
    if query[0] == 1:
        for i in range(query[1], query[2]+1):
            ap[i] = (ap[i][0], ap[i][1], ap[i][2] + query[3])
    else:
        i, j = query[1], query[2]
        c = [ reduce(mul, [(ap[k][0] + e * ap[k][1]) ** ap[k][2] for k in range(i, j+1)], 1) for e in range(N)]
        t = 0
        while not all([e == c[0] for e in c]):
            c_len = len(c)
            f = [c[i+1] - c[i] for i in range(c_len-1)]
            c = f
            t += 1
        print str(t) + " " + str(c[0])
