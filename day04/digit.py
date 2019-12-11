s = '1,238@456asd3434355'

for ch in s:
    if ch not in '0123456789':
        print('Flase')
        break
else:
    print('True')
