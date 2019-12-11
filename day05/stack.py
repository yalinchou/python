stack = []


def push_it():
    data = input('数据: ').strip()
    if data:
        stack.append(data)
    else:
        print('输入为空')


def pop_it():
    if stack:
        print('从栈中弹出了: %s' % stack.pop())
    else:
        print('空栈')


def view_it():
    print('%s' % stack)


def show_menu():
    prompt = '''(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择(0/1/2/3): '''
    while 1:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('无效的输入,请重试.')
            continue

        if choice == '0':
            push_it()
        elif choice == '1':
            pop_it()
        elif choice == '2':
            view_it()
        else:
            print('Bye-bye')
            break


if __name__ == '__main__':
    show_menu()
