for i in range(100//5 + 1):  # //表示只留商，不要小数，舍弃余数
    for j in range(100//3 + 1):
        for k in range(100 + 1):
            if i + j + k == 100 and i * 5 + j * 3 + k / 3 == 100:
                print('公鸡:%s, 母鸡:%s,小鸡:%s' % (i, j, k))