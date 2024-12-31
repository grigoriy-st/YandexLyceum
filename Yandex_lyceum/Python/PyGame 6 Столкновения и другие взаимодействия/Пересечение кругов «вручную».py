x1, y1, r1 = list(map(int, input().split()))
x2, y2, r2 = list(map(int, input().split()))

c_sum = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
r_sum = r1 + r2

print("YES" if c_sum <= r_sum else "NO")