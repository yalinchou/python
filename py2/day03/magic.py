class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return '<%s>' % self.title

    def __call__(self):
        print('<%s> 是%s编著的' % (self.title, self.author))

if __name__ == '__main__':
    pybook = Book('Python核心编程', '韦斯利')
    print(pybook)
    pybook()