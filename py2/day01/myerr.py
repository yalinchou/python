# def set_age(name,age):
#     if not 0 < age < 120:
#         print('年龄超出范围')
#     print('%s is %s years old' % (name, age))
#
# if __name__ == '__main__':
#     set_age('xxx',200)


# def set_age(name,age):
#     if not 0 < age < 120:
#         raise ValueError('年龄超出范围')
#     print('%s is %s years old' % (name, age))
#
# if __name__ == '__main__':
#     set_age('xxx',200)


# def set_age(name,age):
#     if not 0 < age < 120:
#         raise ValueError('年龄超出范围')
#     print('%s is %s years old' % (name, age))
#
# if __name__ == '__main__':
#     try:
#         age = int(input('请输入你的年龄: '))
#         set_age('xxx', age)
#     except ValueError:
#         print('请输入0～120之间的数字')
#     except (KeyboardInterrupt, EOFError):
#         print('\n Bye-bye')

# def set_age(name,age):
#     assert 0 < age < 120,'年龄超出范围'
#
#     print('%s is %s years old' % (name, age))
#
# if __name__ == '__main__':
#     set_age('xxx',20)


def set_age(name,age):
    assert 0 < age < 120,'年龄超出范围'

    print('%s is %s years old' % (name, age))

if __name__ == '__main__':
    try:
        age = int(input('请输入你的年龄: '))
        set_age('xxx', age)
    except (ValueError,AssertionError) as e:
        print('错误: ', e)
    except (KeyboardInterrupt, EOFError):
        print('\n Bye-bye')