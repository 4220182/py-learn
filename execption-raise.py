"""
如果需要在程序中自行引发异常，则应使用 raise 语句。raise 语句有如下三种常用的用法：
raise：单独一个 raise。该语句引发当前上下文中捕获的异常（比如在 except 块中），或默认引发 RuntimeError 异常。
raise 异常类：raise 后带一个异常类。该语句引发指定异常类的默认实例。
raise 异常对象：引发指定的异常对象。

ValueError：

"""

class MyException(Exception):
    """
    自定义异常
    """
    def __init__(self, message):
        self.message = message

counter = 0
try :
    counter = counter + 1
    raise MyException("the is a raise Exception")
except MyException as e :
    print("MyException: ", e.message)
except Exception as e :
    print("Exception: ", e)
