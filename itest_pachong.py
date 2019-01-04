import requests
from bs4 import BeautifulSoup

class ItestVideoWebCrawler:

    def __init__(self):
        self.url = 'http://www.itest.info/videos'
        self.html_doc = requests.get(self.url).text #拿到页面的html
        self.soup = BeautifulSoup(self.html_doc,  "html.parser") #初始化soup,传两个参数分别是html、解析引擎

    def get_all_titles(self):
        res = []
        '''soup的两个核心方法,soup.find/soup.find_all'''
        for a in self.soup.find_all('a', class_='video-link'):
            res.append(a.get_text())
        return res

if __name__ == '__main__':
    titles = ItestVideoWebCrawler().get_all_titles()
    print(titles)