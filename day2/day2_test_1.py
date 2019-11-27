a = 321
b = 123
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

a = 100
b = 12.345
j = 1
c = 1 + 5j
print(c)
d = 'hello, world'
e = True
print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'complex'>
print(type(d)) # <class 'str'>
print(type(e)) # <class 'bool'>


a = 10
b = 3
a += b # 相当于：a = a + b
a *= a + 2 # 相当于：a = a * (a + 2)
print(a) # 想想这里会输出什么

flag0 = 1 == 1   #true
flag1 = 3 > 2    #true
flag2 = 2 < 1    #false
flag3 = flag1 and flag2 #false
flag4 = flag1 or flag2  #true
flag5 = not (1 != 2)    #false
print('flag0 =', flag0) # flag0 = True
print('flag1 =', flag1) # flag1 = True
print('flag2 =', flag2) # flag2 = False
print('flag3 =', flag3) # flag3 = False
print('flag4 =', flag4) # flag4 = True
print('flag5 =', flag5) # flag5 = False
print(flag1 is True) # True
print(flag2 is not False) # False

#print('Test 1,计算华氏摄氏度')
#f = float ( input ('Please input the temp'))
#c = (f-32) / 1.8
#print('%.1f华氏度 = %.1f摄氏度' % (f, c))
#print('current temp is %.2f'%(c))

#print('Test 2,计算元的周长和面积')
#pai = 3.1415926
#r = float ( input ('请输入圆的半径 = ') )
#s = pai * r ** 2
#l = 2 * pai * r
#print ('已知园的周长为%.2f，其面积为%.2f，周长为%.2f'%(r,s,l))
#import math
#radius = r
#perimeter = 2 * math.pi * radius
#area = math.pi * radius * radius
#print('周长: %.2f' % perimeter)
#print('面积: %.2f' % area)


print ('Test 3,判断输入年份是不是闰年')
year = int (input('请输入想要测验的年份'))
#普通闰年:公历年份是4的倍数的，且不是100的倍数，为闰年。（如2004年就是闰年）；
#世纪闰年:公历年份是整百数的，必须是400的倍数才是闰年（如1900年不是世纪闰年，2000年是世纪闰年）；
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 :
    print('输入的年份%d是闰年'%(year))
else :
    print('输入的年份%d不是闰年'%(year))
