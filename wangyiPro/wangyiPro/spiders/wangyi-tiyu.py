import os
import re
import requests

if not os.path.exists('网易新闻-体育'): # 生成文件夹
    os.mkdir('网易新闻-体育')

count = 0
for i in ['nba','cba','china']:
    # 获取所有的url
    response = requests.get(f'https://sports.163.com/{i}/')
    data = response.text
    url_res = re.findall('href="(https://sports.163.com/.*?)"', data)
    url_res = set(url_res)

    # 针对单个url
    for url in url_res:
        url_response = requests.get(url)
        url_data = url_response.text

        try:
            title = re.findall('<h1>(.*?)</h1>', url_data, re.S)[0]
            news_res = \
                re.findall('<div class="post_text" id="endText" style="border-top:1px solid #ddd;">(.*?责任编辑：.*?)</span>',
                           url_data, re.S)[0]  #
            news_res = re.sub('<.*?>', '', news_res)
        except:
            continue

        title = re.sub('[!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~，…]|\s', '', title)  # 除掉标题所有的脏字符
        title_path = os.path.join('网易新闻-体育', f'{title}.txt')  # 拼接出新闻的路径
        f = open(title_path, 'w', encoding='utf8')
        f.write(news_res)
        f.flush()
        f.close()
        count += 1

        print(f'完成{count}篇, {title} done...')