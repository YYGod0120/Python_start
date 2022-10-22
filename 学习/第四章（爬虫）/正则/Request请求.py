import requests
url = 'https://www.zhihu.com/'
use_agent = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36'
}
resp = requests.get(url,headers = use_agent)

print(resp)
print(resp.text)#拿到页面源代码
resp.close()