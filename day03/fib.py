# def mk_fib():
#     fib = [0, 1]
#     n = int(input('请输入数列的长度: '))
#     for i in range(n -2):
#         fib.append(fib[-1] + fib[-2])
#     print(fib)
#
# mk_fib()
# mk_fib()

# def mk_fib():
#     fib = [0, 1]
#     n = int(input('请输入数列的长度: '))
#     for i in range(n -2):
#         fib.append(fib[-1] + fib[-2])
#     return fib
#
# a = mk_fib()
# b = [i * 2 for i in a ]
# print(b)
# with open('/tmp/fib.txt','w') as fobj:
#     fobj.write(str(a))

def mk_fib(n):
    fib = [0, 1]

    for i in range(n -2):
        fib.append(fib[-1] + fib[-2])
    return fib

a = mk_fib(8)
b = [i * 2 for i in a ]
print(b)
with open('/tmp/fib.txt','w') as fobj:
    fobj.write(str(a))

n = int(input('请输入数列的长度: '))
c = mk_fib(n)
print(c)