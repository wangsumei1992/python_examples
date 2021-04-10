#统计字符串中每个字符出现的次数最高的前三个
str = "wwqqqssssaaaaddfff"
dict = {}
for i in str:
    dict[i] = str.count(i)
print(dict)
sort_ls = sorted(dict.items(), key=lambda x: x[1], reverse=True)
print(sort_ls[0:3])
# for key in dict:
#     print(f'{key}:{dict[key]}')

