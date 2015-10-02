import sys
n, K = map(int, raw_input().split(" "))
myset = set(map(int, raw_input().split(" ")))
print sum([(int((s+K) in myset) + int((s-K) in myset)) for s in myset])/2

