#aws s3

def test(team,*members) :
    print(team,members)

test('my','test1')
test('my','test1','test2','test3')

def test2(team,**members) :
    print(team,members)

test2('my',test1=1)
test2('my',test1=1,test2=2)