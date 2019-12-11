def func1(x):
    if x == 1:
        return 1
    else:
        return x * func1(x - 1)
if __name__ == '__main__':
    print(func1(5))