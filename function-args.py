"""
参考：https://www.runoob.com/python3/python3-function.html

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
