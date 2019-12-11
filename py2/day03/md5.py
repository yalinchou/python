import sys
import hashlib

def check_md5(fname):
    m = hashlib.md5()
    with open(fname,'rb') as fobj:
        while 1:
            data = fobj.read(4096)
            if not data:
                break
            m.update(data)
    return m.hexgigest()

if __name__ == '__main__':
    print(check_md5(sys.argv[1]))