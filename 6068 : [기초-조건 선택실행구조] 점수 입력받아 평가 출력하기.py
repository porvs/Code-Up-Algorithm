input = int(input())
if(input >= 90 and input <= 100):
    print('A')
elif(input >= 70 and input <= 89):
    print('B')
elif(input >= 40 and input <= 69):
    print('C')
elif(input >= 0 and input <= 39):
    print('D')
else:
    print("경로이탈")
