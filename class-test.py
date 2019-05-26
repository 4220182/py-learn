class users :
    name = ''
    age = 0
    __weight = 0 #私有变量
    def __init__(self,name,age,w):
        self.name = name
        self.age = age
        self.__weight = w

    def speak(self):
        self.__do()
        print(self.name)

    def __do(self): #私有函数
        print(self.age)

user =  users('zyh',11,20)
user.speak()

