#求最大公约数
def hcf(num1,num2):
    if num1 > num2:
        samller_num = num2
    else:
        samller_num = num1
    for i in range(1,samller_num+1):
        if (num1 % i ==0) and (num2 % i == 0):
            hcf = i
    return hcf

a = int(input('输入第一个数： '))
b = int(input('输入第二个数： '))
print('{},{}的最大公约数是：'.format(a,b),hcf(a,b))