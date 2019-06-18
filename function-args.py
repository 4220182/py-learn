"""
参考：https://www.runoob.com/python3/python3-function.html

global 使用函数外的变量
"""
# 加了星号 * 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。

counter = 1
def test(team,*members) :
    global counter
    print(team,members)
    for members in members:
        counter = counter + 1
        print(members, counter)

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


# if __name__ == "__main__":
#     main()