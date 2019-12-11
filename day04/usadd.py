import randpass2
import sys
import subprocess


def add_user(user, passwd, fname):
    result = subprocess.run(
        'id %s &> /dev/null' % user, shell=True
    )
    if result.returncode == 0:
        print('用户已存在.')
        return
    subprocess.run(
        'useradd %s' % user, shell=True
    )
    subprocess.run(
        'echo %s | passwd --stdin %s' % (passwd, user),
        shell=True
    )

    info = '''用户信息:
用户名: %s
密码: %s
''' % (user, passwd)
    with open(fname, 'a') as fobj:
        fobj.write(info)


if __name__ == '__main__':
    user = sys.argv[1]
    passwd = randpass2.randpass()
    fname = sys.argv[2]
    add_user(user, passwd, fname)
