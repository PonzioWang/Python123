def getNum():   #获取用户不定长度的输入
    nums = []
    iNumstr = input("请输入数字（回车退出）：")
    while iNumstr != '':
        nums.append(eval(iNumstr))
        iNumstr = input("请输入数字（回车退出）：")
    return nums

def mean(numbers):    #计算平均数
    s = 0.0
    for num in numbers:
        s =  num + s
    return s / len(numbers)

def dev(numbers,mean):
    sdev = 0.0
    for num in numbers:
        sdev = sdev + (num - mean)**2
    return pow(sdev / (len(numbers) - 1),0.5)    

def median(numbers):
    sorted(numbers)
    size = len(numbers)
    if size % 2 == 0:
        med = (numbers[size//2-1] + numbers[size//2])/2
    else:
        med = numbers[size//2]
    return med

n = getNum()
m = mean(n)

print("平均数:{},方差:{},中位数:{}".format(m,dev(n,m),median(n)))
