f = open("logs/users.log",mode="r")

for line in f.readlines():
    print(line)
