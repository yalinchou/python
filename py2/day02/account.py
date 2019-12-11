from time import strftime
import pickle
import os


def save(fname):
    date = strftime('%Y-%m-%d')
    try:
        amount = int(input('金额:'))
        comment = input('备注:')
    except ValueError:
        print('输入的金额无效.')
        return
    except (KeyboardInterrupt, EOFError):
        print('\n Bye-bye')
        exit(1)
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    balance = records[-1][-2] + amount

    record = [date, amount, 0, balance, comment]
    records.append(record)
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)


def cost(fname):
    date = strftime('%Y-%m-%d')
    try:
        amount = int(input('金额:'))
        comment = input('备注:')
    except ValueError:
        print('输入的金额无效.')
        return
    except (KeyboardInterrupt, EOFError):
        print('\n Bye-bye')
        exit(1)
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)

    balance = records[-1][-2] - amount

    record = [date, 0, amount, balance, comment]
    records.append(record)
    with open(fname, 'wb') as fobj:
        pickle.dump(records, fobj)


def query(fname):
    print('%-12s%-8s%-8s%-12s%-20s' % ('date', 'save', 'cost', 'balance', 'comment'))
    with open(fname, 'rb') as fobj:
        records = pickle.load(fobj)
    for record in records:
        print('%-12s%-8s%-8s%-12s%-20s' % tuple(record))


def show_menu():
    cmds = {'0': save, '1': cost, '2': query}
    prompt = '''(0) 收入
(1) 支出
(2) 查询
(3) 退出
请选择(0/1/2/3): '''
    fname = 'account.data'
    init_data = [
        ['2019-12-10', 0, 0, 10000, 'init data']
    ]
    if not os.path.exists(fname):
        with open(fname, 'wb') as fobj:
            pickle.dump(init_data, fobj)

    while 1:
        try:
            choice = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            choice = '3'

        if choice not in ['0', '1', '2', '3']:
            print('无效的输入,请重试.')
            continue

        if choice == '3':
            print('\n Bye-bye')
            break

        cmds[choice](fname)


if __name__ == '__main__':
    show_menu()
