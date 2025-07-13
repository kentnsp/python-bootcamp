#import whole module
import hello
hello.say_hello()

#import specific (multiple) def / function
from hello import say_goodbye,var2
say_goodbye()
print(var2)

#alias / nickname for long names~
import hello as ho
ho.say_hello()