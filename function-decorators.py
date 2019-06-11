"""
参考：https://www.runoob.com/python3/python3-function.html

Python 函数装饰器(Decorators) :
'@' 用做函数的修饰符，一个修饰符就是一个函数，它将被修饰的函数作为参数，并返回修饰后的同名函数或其他可调用的东西；
python装饰器本质上就是一个函数，它可以让其他函数在不需要做任何代码变动的前提下增加额外的功能，装饰器的返回值也是一个函数对象（函数的指针）
参考：
https://www.cnblogs.com/wangjian1226/p/10531702.html
https://www.cnblogs.com/xiaojianliu/articles/10025587.html

"""

# 原函数没有参数,修饰器可以看作是一个接收函数的函数，内部再定义局部函数用来修饰传进来的函数参数
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"

    return wrapped


def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"

    return wrapped


@makebold
@makeitalic
def hello():
    return "hello world"


print(hello())  ## 返回 <b><i>hello world</i></b>

# 原函数有参数,修饰函数还是传函数参数，修饰函数里面的局部函数传入原函数的参数
def w2(fun):
    def wrapper(*args,**kwargs):
        print('call %s():' % fun.__name__)
        fun(*args,**kwargs)
        print(args,kwargs)
    return wrapper

@w2
def hello2(name,name2):
    print("hello"+name+name2)

hello2("world","!!!")