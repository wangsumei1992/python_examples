def wq(*args):
    # l = list(set(list1))
    # print(l)\

    list2 = []
    for i in args:
        if i not in list2:
            list2.append(i)
    print(list2)
    #return list2
#去除列表中的重复元素
if __name__ =='__main__':
    list1 = [1, 2, 3, 4, 5, 8, 2, 3]
    wq(*list1)