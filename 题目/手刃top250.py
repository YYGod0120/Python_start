import requests
import re
import csv
url = 'https://movie.douban.com/top250?start=25&filter='
headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"
}
resp = requests.get(url,headers = headers)

#解析数据
obj = re.compile(

    '<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)'
'</span>.*?</div>.*?<div class="bd">.*?<p class="">(?P<director>.*?)'
    '&nbsp;&nbsp;&nbsp.*?<br>(?P<year>.*?)&nbsp;/&nbsp;', re.S)
#正则要跟着写


#匹配
result = obj.finditer(resp.text)
f = open('data.csv',mode='a',encoding='utf-8')
csvwriter = csv.writer(f)
for it in result:
    print(it.group('year').strip())
    dic = it.groupdict()
    dic['director'] = dic['director'].strip()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())
resp.close()
f.close()
print('over')
