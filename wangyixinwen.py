import requests
import json
url='http://c.3g.163.com/nc/article/list/T1348648517839/0-20.html'
#url = 'http://c.m.163.com/nc/article/headline/T1348647853363/0-100.html'
header = {
        'User-Agent': 'Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1)',
        'Connection': 'keep - alive',
        }
wbdata = requests.get(url,headers=header).text
data = json.loads(wbdata)
news=data['T1348648517839']
#news = data['T1348647853363']
for item in news:
    digest = item['digest']
    mtime = item['mtime']
    title = item['title']
    source = item['source']
    try:
        url = item['url']
    except:
        url = ''
    newes_data ={
        'title': title,
         '内容': digest,
               '时间': mtime,
                '来源': source,
                '链接': url,

    }
    print(newes_data)
input()

