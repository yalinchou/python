# num = input('grade: ')
# a = int(num)
# if 60 <= a <= 70:
#     print('及格')
# elif 70 < a <= 80:
#     print('良')
# elif 80 < a <= 90:
#     print('好')
# elif 90 < a <= 100 :
#     print('优秀')
# elif a < 60 :
#     print('你要加油了')
score = int(input('分数: '))
if score >= 90:
    print('优秀')
elif score >= 80:
    print('好')
elif score >= 70:
    print('良')
elif score >= 60:
    print('及格')
else:
    print('你要加油了')