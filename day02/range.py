# result = 0
# for i in range(1,10000001):
#     result += i
# print(result)
# fib = [0, 1]
# for i in range(8):
#     fib.append(fib[-1] + fib[-2])
# print(fib)

fib = [0, 1]
n = int(input('请输入长度: '))
for i in range(n - 2):
    fib.append(fib[-1] + fib[-2])
print(fib)