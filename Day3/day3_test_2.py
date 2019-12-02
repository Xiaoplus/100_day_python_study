"""
百分制成绩转换为等级制成绩

Version: 0.1
Author: Stone
"""

score = float(input('请输入分数:'))
if score > 100 :
    print('Please input valid data')
elif score >= 90 :
    print('Class A')
elif score >= 80 :
    print('Class B')
elif score >= 70 :
    print('Class C')
elif score >= 60 :
    print('Class D')
else :
    print('Class E')

tmp = score * 1000000
print(tmp)

for i in range(0,101) :
    print(i)
