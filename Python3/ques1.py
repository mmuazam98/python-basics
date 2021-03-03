import sys
t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    count = 0
    for time in a:
        if time <= 0:
            count += 1
        if count >= k:
            print("NO")
            break
        if time > 0:
            print("YES")
            break