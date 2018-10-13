import random
b_0 = (("18 " * int(18000 * 0.5)).split(' '))[:-1]
#print(b_0)
b_1 = (("19 " * int(18000 * 0.1)).split(' '))[:-1]
b_2 = (("20 " * int(18000 * 0.1)).split(' '))[:-1]
b_3 = (("21 " * int(18000 * 0.1)).split(' '))[:-1]
b_4 = (("22 " * int(18000 * 0.1)).split(' '))[:-1]
b_5 = (("24 " * int(18000 * 0.1)).split(' '))[:-1]
b = b_0 + b_1 + b_2 + b_3 + b_4 + b_5
random.shuffle(b)
#print(len(b))
with open('data1.txt', 'w+') as f:
    for data in b:
        f.write("sub_id="+data+"\n")