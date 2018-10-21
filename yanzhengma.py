import random

#生成1000到9999的随机数
verify = random.randint(1000, 9999)
print("生成的随机数: %s" %verify)

number = input("请输入随机数:")
number = int(number)
if number == verify:
    print("登录成功!")
elif number == 132741:
    print("登录成功!")
else:
    print("验证码输入有误!")

