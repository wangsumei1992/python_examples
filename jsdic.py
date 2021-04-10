# import json
# """dumps:将python中的字典转换为字符串"""
# def json_dumps():
#     dict = {'name': 'joe', 'age': 20, 'job': 'driver'}
#     info_json = json.dumps(dict)
#     print(type(info_json))
#     print(info_json)
#     c = json.loads(info_json)
#     print(c)
# json_dumps()
from selenium import webdriver

dr = webdriver.Chrome()
dr.get("https://renrendai.com/disclosure/information/filing")
s = dr.find_element_by_class_name("fund-deposit-title").text
print(s)