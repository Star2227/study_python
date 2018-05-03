class Dog():
    """
    一次模拟小狗的尝试
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title()+"现在坐下了")

    def roll_over(self):
        print(self.name.title() + "打滚")

my_dog = Dog("wangcai", 6)
print("我的狗叫" + my_dog.name)
print('我的狗' + str(my_dog.age) + '岁')
my_dog.sit()
my_dog.roll_over()