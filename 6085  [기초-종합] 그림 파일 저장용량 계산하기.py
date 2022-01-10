r,g,b = map(int, input().split())
Sum = float(r*g*b)
print(format(Sum/8/1024/1024, ".2f"), "MB")