#nested with alias
import package.module_01 as pm1
pm1.say_hello()
print(pm1.message)

#from ~ import
from package.module_01 import say_goodbye
say_goodbye()