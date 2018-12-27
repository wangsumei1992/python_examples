#用户选择输出1到n的和还是1到n的积
def sum(n):
    s = 0
    for i in range(n):
        s = s + i
    return(s)
#print(sum(5))
def mutiply(n):
    s = 1
    for i in range(1,n+1):
        s = s * i
    return (s)
#print(mutiply(5))
a = input("用户输入打印1到n的和或者是1到n的积:")
if a in "1到n的积":
    print(mutiply(5))
if a in "1到n的和":
    print(sum(5))


#输入100以内的质数
for i in range(101):
    if i % 2 == 1:
        print(i)

#随机生成数字，直到用户输入正确为止
import random
while True:
    a = random.randint(1,10)
    b = int(input("用户输入1到10的随机整数:"))
    if b < a:
        print("您的输入大于随机整数")
    elif b > a:
        print("您的输入小于随机整数")
    else:
        break

#打印出下个20年内的闰年
for i in range(2018, 2018 + 21):
    if i % 4 == 0:
        print(i)
