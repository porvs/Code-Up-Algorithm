r,g,b = map(int, input().split())
for a in range(0, r):
    for n in range(0, g):
        for m in range(0, b):
            print(a, n, m)
        
print(r*g*b)
