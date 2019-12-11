import random
choices = ['石头','剪刀','布']
computer = random.choice(choices)
player = input('请出拳(石头/剪刀/布): ')
print('你出的是: %s ,电脑出的是: %s' % (player,computer))
if player == '石头':
    if computer == '石头':
        print('平局')
    elif computer == '剪刀':
        print('你赢了')
    else :
        print('你输了')
elif player == '剪刀':
    if computer == '石头':
        print('你输了')
    elif computer == '剪刀':
        print('平局')
    else :
        print('你赢了')
else:
    if computer == '石头':
        print('你赢了')
    elif computer == '剪刀':
        print('你输了')
    else :
        print('平局')