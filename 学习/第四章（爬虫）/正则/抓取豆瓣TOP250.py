import re
import requests
import csv
url = 'https://movie.douban.com/top250'
headers = {
    "user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54"
}
resp = requests.get(url,headers = headers)

print(resp.text)

#解析数据


