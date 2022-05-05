import sys
n=sorted(sys.stdin.readline().rstrip())
n.reverse()
print("".join(map(str,n)))
