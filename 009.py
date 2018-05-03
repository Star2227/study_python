with open('pi.txt') as file_object:
    lines = file_object.readlines()
    pi_string = ''
    for line in lines:
        pi_string += line.strip()

birthday = input('请输入你的生日（mmddyy）:')
if birthday in pi_string:
    print('你的生日出现在圆周率的中')
else:
    print("没有")
