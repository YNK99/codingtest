X = int(input())
N = int(input())
S = 0

for _ in range(N):
    a, b = map(int, input().split())
    S += a * b

if X == S:
    print("Yes")
else:
    print("No")