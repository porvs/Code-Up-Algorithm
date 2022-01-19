h, w = map(int, input().split()) #세로, 가로 입력받기
game = [[0]*w for i in range(h)] #크기에 맞도록 판 초기화하기
n = int(input()) #막대의 개수 입력받기
for i in range(n):
    l, d, x, y = map(int, input().split()) #막대 정보 입력받기
    for i in range(0,l):
        if d == 0: #가로일 경우
            game[x-1][y+i-1] = 1 # 해당 행부분을 1로 변경
    else:
        game[x+i-1][y-1] = 1 # 해당 열부분을 1로 변경
for i in game:
    print (" ".join(repr(j)for j in i))