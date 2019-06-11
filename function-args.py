"""
参考：https://www.runoob.com/python3/python3-function.html

Python 函数装饰器 :
'@' 用做函数的修饰符，一个修饰符就是一个函数，它将被修饰的函数作为参数，并返回修饰后的同名函数或其他可调用的东西；
参考：https://www.runoob.com/w3cnote/python-func-decorators.html

"""
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。
def test(team,*members) :
    print(team,members)
    for members in members:
        print(members)

test('my')
test('my','test1')
test('my','test1','test2','test3')

# 加了两个星号 ** 的参数会以字典的形式导入。
def test2(team,**members) :
    print(team,members)
    for member in members.keys():
        print(members[member])

test2('my2',test1=1)
test2('my2',test1=1,test2=2)
