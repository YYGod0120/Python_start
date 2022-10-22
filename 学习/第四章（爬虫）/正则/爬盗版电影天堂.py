import re
import requests

#先爬主页面的内容
url = 'https://www.dy2018.com/'
resp1 = requests.get(url,verify=False) #verify = False叫做去掉安全验证
resp1.encoding = 'gbk'


#编写第一份正则提取全部子页面所需的内容
obj1 = re.compile('欧美电视剧.*?<ul>(?P<url_main>.*?)</ul>',re.S)
result1 = obj1.finditer(resp1.text) #提取到主页面内容



obj2 = re.compile("<li><a href='(?P<url_child>.*?)' ", re.S)  #编写第二份正则,为提取子页面url
result2 = obj2.finditer(result1.__next__().group('url_main').strip()) #提取主页面中子页面的url
obj3 = re.compile("◎译　　名(?P<name>.*?)<br />"
                  '.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S) #编写第三份正则，提取子页面中的电视剧名字和下载地址

for i in result2:
    url_child = url + i.group("url_child").strip("/") #获取子页面url
    resp2 = requests.get(url_child)#获取子页面源代码
    resp2.encoding = "gbk" #改编码
    result3 = obj3.finditer(resp2.text) #获取到子页面的电视剧名字和下载地址


    for it in result3:
        print(it.group('name'))
        print(it.group('download'))

















