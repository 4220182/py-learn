"""
参考：https://www.runoob.com/python3/python3-function.html


参考：
https://blog.51cto.com/3945465/2384795
https://blog.csdn.net/qq_33733970/article/details/77196239

"""

class users:
    def __init__(self, username):
        self.__username = username

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @username.deleter
    def username(self):
        del self.__username

u =  users("test")
u.username = "test2"
#del u.name
print(u.username)
