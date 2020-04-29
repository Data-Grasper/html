from urllib.parse import urlencode
import requests
from lxml import etree

url = "https://movie.douban.com/"
ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240"

with requests.request('GET', url, headers={'User-agent': ua}) as res:
    content = res.text  # 获取HTML的内容
    html = etree.HTML(content)  # 分析HTML，返回DOM根节点
    # path = //div[@class='billboard-bd']//td//a/text()
    orders = html.xpath("//div[@class='billboard-bd']//tr/td[@class='order']/text()")
    titles = html.xpath("//div[@class='billboard-bd']//td//a/text()")  # 使用xpath函数，返回文本列表
    print(orders)
    print(titles)
    ans = dict(zip(orders, titles))  # 豆瓣电影之本周排行榜
    for k, v in ans.items():
        print(k, v)
