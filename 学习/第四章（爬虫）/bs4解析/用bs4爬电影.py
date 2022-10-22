import requests
from bs4 import BeautifulSoup

#拿到源代码
url_main = 'http://www.xinfadi.com.cn/priceDetail.html'
resp = requests.get(url_main)
print(resp.text)

#用bs4处理页面
page = BeautifulSoup(resp.text,'html.parser') #指定html解析器
#从bs对象中找到数据
#find_all(标签，属性=值)
a = page.find_all('li', class_="lis")

print(a)




