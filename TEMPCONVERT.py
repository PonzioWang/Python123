#TempConvert.py
TempSter = input("请输入带有符号的温度值：")
if TempStr[-1] in ['F','f']:
    C = (eval(Tempstr[ 0:-1]) - 32)/1.8
    print("准换后的温度是{:.2f}C".format(c))
elif TempStr[-1] in ['c','c']:
    F = 1.8*eval(TempStr[0:-1]) + 32
    print("准换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
