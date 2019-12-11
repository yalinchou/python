import time


t9 = time.strptime('2019-12-09 09:00:00','%Y-%m-%d %H:%M:%S')
t12 = time.strptime('2019-12-09 12:00:00','%Y-%m-%d %H:%M:%S')

with open('mylog.txt') as fobj:
    for line in fobj:
        t = time.strptime(line[:19],'%Y-%m-%d %H:%M:%S')
        if t >= t12:
            break
        if t >= t9:
            print(line)


# with open('mylog.txt') as fobj:
#     for line in fobj:
#         t = time.strptime(line[:19],'%Y-%m-%d %H:%M:%S')
#         if t9 <= t <=12:
#             print(line,end='')