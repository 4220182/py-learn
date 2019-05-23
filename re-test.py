import re

s = "2019-02-19 23:59:36,573 DEBUG [ITestService] com.test.depositeMoney Arguments:[河路127, 200] Returns: 0cost : 1"
p ='^(\\d{4}-\\d{2}-\\d{2} \\d{2}:\\d{2}:\\d{2},\\d{3}) DEBUG \\[ITestService\\] com.test.depositeMoney Arguments:\\[(.*?), (.*?)\\] Returns: (.*?)cost : .*?'
pattern = re.compile(p, re.IGNORECASE)

m = pattern.match(s)
if m :
  print(m.group(1))
  print(m.group(2))

try :
  print(b)
except :
  print("error")