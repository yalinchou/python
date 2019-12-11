from random import choice, randint


def game():
    nums = [randint(1, 100) for i in range(2)]
    nums.sort(reverse=True)

    op = choice('+-')

    if op == '+':
        result = nums[0] + nums[1]
    else:
        result = nums[0] - nums[1]

    counter = 0
    prompt = '%s %s %s= ' % (nums[0], op, nums[1])

    while counter < 3:
        try:
            answer = int(input(prompt))
        except:
            print()
            continue
        if answer == result:
            print('Good')
            break
        else:
            print('Wrong Answer')
        counter += 1
    else:
        print('%s%s' % (prompt, result))

def main():
    while 1:
        game()

        try:
            yn = input('Continue(y/n)?').strip()[0]
        except IndexError:
            continue
        except (KeyboardInterrupt,EOFError):
            yn = 'n'
        if yn in 'Nn':
            print('\n Bye-bye')
            break


if __name__ == '__main__':
    main()
