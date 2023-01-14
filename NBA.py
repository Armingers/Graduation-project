import requests
from lxml import etree
url = 'https://china.nba.cn/playerindex/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

resp = requests.get(url,headers=headers)

e = etree.HTML(resp.text)
names = e.xpath('//table[@class=""]//tr/td[1]/a/span/text()')

print(names)

