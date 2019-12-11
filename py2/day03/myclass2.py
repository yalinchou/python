class Role:
    def __init__(self, nm, wp):
        self.name = nm
        self.weapon = wp

    def show_me(self):
        print('我是%s,我使用的是%s' % (self.name,self.weapon))

    def speak(self,words):
        print(words)
class Warrior(Role):
    pass

class Mage(Role):
    def fly(self):
        print('I can fly')

if __name__ == '__main__':
    lb = Warrior('吕布', '方天画戟')
    zgl = Mage('诸葛亮', '扇子')
    lb.show_me()
    zgl.show_me()
    zgl.fly()