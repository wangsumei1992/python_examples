import random, csv
a_1 = list("1"*int((18000*0.7)))
#print(a_1)
a_0 = list("0"*int((18000*0.3)))
#print(a_0)
a = a_0 + a_1
print(len(a))
random.shuffle(a)
with open('data.txt', 'w+') as f:
    # writer = csv.writer(f)
    # csvrow1 = []
    # csvrow1.append('with_tb')
    # csvrow2 = []
    for data in a:
        f.write("with_tb="+data+"\n")
