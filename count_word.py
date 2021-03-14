#一个文件中有许多单词，每个词之间以空格分隔，统计下这个文件中出现频率最高的三个单词
# from parameterized import parameterized
# import unittest
# import requests
#
# class Test(unittest.TestCase):
#     @parameterized.expand([('hell','oo','helloo'),(1,2,3)])
#     def test(self, test1, test2, test3):
#         self.assertEqual((test1+test2),test3)
# if __name__ == '__main__':
#     unittest.main()

with open(filename, 'r') as f:
    counts = f.read().split(' ')
    dict = {}
    for c in counts:
        dict[c] = c.count()
l = sorted(dict.items(),key=lambda x:x[1],reverse=True)
print(l[0:3])





