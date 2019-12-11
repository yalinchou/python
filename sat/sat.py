# username = input('username: ')
# print(username)


# username = input('username: ')
# print('hello %s' % (username))
# print('welcome ' + username)

# n = input('number: ')
# a = int(n) + 10
# b = n + str(10)
# print(a)
# print(b)

#
# s = 'nihaoshenzhen'
# for ch in s:
#     print(ch)


# print('*' * 30)


# users = ['tom', 'jim','john']
# for name in users:
#     print(name)
#
# print('*' * 50)


# nums = (10,20,12,34)
# for i in nums:
#     print(i)
#
# print('#' * 50)


# adict = {'name':'tom','age':30}
# for key in adict:
#     print(key,adict[key])
#
# print('$' * 50)
# result = 0
# counter = 0
#
# while counter < 100:
#     counter += 1
#     if counter % 2 == 1:
#         continue
#     else:
#         result += counter
# print(result)


# result = 0
# counter = 0
# while counter < 100:
#     counter += 1
#     if counter % 2 == 1:
#         result += counter
#     else:
#         continue
# print(result)

# import random
#
# num = random.randint(1,100)
# counter = 0
# while counter < 5:
#     counter += 1
#     answer = int(input('guess: '))
#
#     if answer == num:
#         print('猜对了')
#     elif answer > num:
#         print('猜大了')
#     else:
#         print('猜小了')
# else:
#     print('正确答案是%s' % num)


# import getpass
# uname = input('username: ')
# upass = getpass.getpass('password: ')
#
# if uname == 'bob' and upass == '123456':
#     print('Login successful')
# else:
#     print('Login incorrect')


# import time
# sentence = "Dear, I love you forever!"
# for char in sentence.split():
#    allChar = []
#    for y in range(12, -12, -1):
#        lst = []
#        lst_con = ''
#        for x in range(-30, 30):
#             formula = ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3
#             if formula <= 0:
#                 lst_con += char[(x) % len(char)]
#             else:
#                 lst_con += ' '
#        lst.append(lst_con)
#        allChar += lst
#    print('\n'.join(allChar))
#    time.sleep(1)

# result = 0
# counter = 0
# while counter < 20000:
#     result += counter
#     counter += 1
# print(result)

# hi = 'hello world'
# def pstar(n=30):
#     print('*' * n)
# if __name__ == '__main__':
#     print(hi)
#     print(50)