#生成斐波那契数列的前20个数。

print('Program on')
current_num = 2
pre_num = 1
print(1)
print(1)
for i in range(0,17) :
    resutlt_value = current_num + pre_num
    pre_num = current_num
    current_num = resutlt_value
    print(resutlt_value)
