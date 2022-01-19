game = [list(map(int, input().split()))for _ in range(19)] #2차원 배열 입력
num = int(input()) #몇 번 뒤집을지
for i in range(num):
    a, b = map(int, input().split())
    for j in range(19):
        game[a-1][j] = (1 if game[a-1][j] == 0 else 0)
        game[j][b-1] = (1 if game[j][b-1] == 0 else 0)
for i in game:
    print (" ".join(repr(j) for j in i))