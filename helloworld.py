
#my first python program

print ('hello!please input your  name:')

name = input()

print ('hello ,',name,', welcome to the world of python!')

print (12*12-21)

print('I\'m \"OK\"!')

print('I\'m learning\nPython.')

print('\\\n\\')

print('\\\t\\')
#如果字符串里面有很多字符都需要转义，就需要加很多\，
#为了简化，Python还允许用r''表示''内部的字符串默认不转义
print(r'\\\t\\')


print('''line1
line2
line3''')


#空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值
#在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量


#所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量：
#PI = 3.14159265359


#注意：Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在-2147483648-2147483647。

#Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。



#在Python中，有两种除法，一种除法是/
#还有一种除法是//，称为地板除，两个整数的除法仍然是整数：
#你没有看错，整数的地板除//永远是整数，即使除不尽。要做精确的除法，使用/就可以。

#因为//除法只取结果的整数部分，所以Python还提供一个余数运算，可以得到两个整数相除的余数：
#无论整数做//除法还是取余数，结果永远是整数，所以，整数运算结果永远是精确的。




