import requests
from bs4 import BeautifulSoup

class QiuBaiWebCrawler:

    def __init__(self):
        self.url = "https://www.qiushibaike.com/"
        self.html_doc = requests.get(self.url).text
        self.soup = BeautifulSoup(self.html_doc, "html.parser")
        #print(self.soup)

    def get_contents(self):
        res = []
        for content in self.soup.find_all('li', class_="typs_video"):
            res.append(content.get_text())
        return res

if __name__ == "__main__":
    contents = QiuBaiWebCrawler().get_contents()
    print(contents)
