fields = {
    'custname': 'test-name',
    'test-name': 'hello',
    'custtel': '13888888888',
    'data': {'context': 'just a test'},
    'custemail': '13888888888@gmail.com'
}


for a,b in fields.items() :
    print(type(b))
    if a=="custname" :
        print("Y: " ,b)
    elif a>"138" :
        print ("N: " , b)
    print(a,b)

def users(name,age=20):
    print (name,age)

users("zyh")
users("hello",30)


