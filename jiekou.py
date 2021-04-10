import requests

r = requests.get("https://www.douban.com/",  headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
print(r.url)
print(r.status_code)
print(r.text)
print(r.cookies)
s = requests.post('https://accounts.douban.com/login', data={'form_email': 'abc@example.com', 'form_password': '123456'})
print(s.headers)
print(s.headers['Date'])
cs = {'token': '12345', 'status': 'working'}
# h= requests.get(url, cookies=cs)

