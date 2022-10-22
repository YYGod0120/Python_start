from urllib.request import urlopen
url = 'https://www.sogou.com/'

b = urlopen(url)
#print(b.read().decode('utf-8'))
with open('baidu.html', mode='w', encoding='utf-8') as file:
    file.write(b.read().decode('utf-8'))
print('ok')


