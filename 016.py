n = int(input('您要斐波那契数列的前几项？请输入'))
count = 1
a=0
b=1
while count <= n:
    a,b = b,a+b
    print(a,end=",")
    count += 1

