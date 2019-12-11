class Role:
    def __init__(self, nm, wp):
        self.name = nm
        self.weapon = wp

    def show_me(self):
        print('我是%s,我使用的是%s' % (self.name,self.weapon))

    def speak(self,words):
        print(words)

if __name__ == '__main__':
    lb = Role('吕布', '方天画戟')
    print(lb.name)
    print(lb.weapon)
    lb.show_me()
    lb.speak('马中赤兔,人中吕布')