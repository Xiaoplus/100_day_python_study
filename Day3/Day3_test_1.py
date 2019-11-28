print('求分段案函数值')
X = float(input('请输入X的值:'))
if X > 1  :
    y = 3*X - 5
elif X >= -1 and X <= 1 :
    y = X + 2
else :
    y = 5 * X + 3

print("分段函数的值为%d"%(y))
