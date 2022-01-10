h,b,c,s = map(int, input().split())
Sum = float(h*b*c*s)
print(format(Sum/8/1024/1024, ".1f"), "MB")