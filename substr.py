#给定一个字符串，请你查找出其中不含有重复字符的最长子串的长度

def get_max_sub(str):
    start_index = 0
    max_sub = 0
    dic = {}
    for i in range(len(str)):
        if str[i] in dic:
            start_index = max(dic[str[i]],start_index)

        dic[str[i]] = i+1
        max_sub = max(i-start_index+1,max_sub)

    return max_sub
def panduan(str):
    if len("".join(set(str))) == len(str):
        return True
    else:
        return False

def get_sub_str(str):
    max_sub = get_max_sub(str)
    for i in range(len(str)):
        sub_str = str[i:max_sub+i]
        if panduan(sub_str):
            return sub_str

if __name__ == '__main__':
    s = get_sub_str('abbcdefg')
    print(s)
