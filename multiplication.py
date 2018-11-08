"""九九乘法表"""
for i in range(1, 10):
    for j in range(1, i+1):
        print("{}*{}={}".format(j, i, i*j))
    print() #指出下一次输出点的位置

"""递归函数输出斐波那契数列"""

def recur_feibo(n):
    if n <= 1:
        return n
    else:
        return(recur_feibo(n-1) + recur_feibo(n-2))

nterms = int(input("您要输出几项?"))
if nterms <= 0:
    print("请您输入正整数")
else:
    print("斐波那契数列:")
    for i in range(nterms):
        print(recur_feibo(i))

"""n的阶乘"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n*factorial(n-1))
a = factorial(5)
print(a)