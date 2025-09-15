X = int(input())
d = 0
cnt = 0

while cnt < X:
    d += 1
    cnt += d

prev_sum = cnt - d
idx = X - prev_sum

if d % 2 == 0:
    num = idx
    den = d - idx + 1
else:
    num = d - idx + 1
    den = idx

print(f"{num}/{den}")
