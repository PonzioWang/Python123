from time import perf_counter
from 
shart = perf_counter()
pi = 0
n = 100
for k in range(n):
    pi += 1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*+5)-1/(8*k+6))
end = perf_counter()    
print("圆周率值是:{}".format(pi))
print("运行时间是:{}".format(end-shart))
