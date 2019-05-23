import re

s = "1332667986,56196,-639, 爱就在一起,39369,-639, 654lgx,949363,1161"
p ='(| )(\S+),(\d+),(-*\d+)(,|)'

ps = re.compile(p, re.IGNORECASE)
results = ps.findall(s)

print(results,len(results))
