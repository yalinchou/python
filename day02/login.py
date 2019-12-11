# #导入名为getpass的模块
# import getpass
#
# uname = input('username: ')
# #调用getpass模块中的getpassh函数
# upass = getpass.getpass('password: ')
#
# if uname == 'bob' and upass == '123456' :
#     print('login sucessful')
# else :
#     print('login incorrect')
#
uname = input('username: ')
upass = input('password: ')
if uname == 'tom' and upass == '123456':
    print('login successful')
else:
    print('login incorrect')
