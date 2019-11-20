import random
import requests
from lxml import etree
import time
my_headers =[
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    '''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36''',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)'
]

def getHeader():
    head = {
            'user-agent': random.choice(my_headers),
            'Cookie': 'bid=6MigHW5BotY; __utmc=30149280; __utmz=30149280.1571619407.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=223695111; __utmz=223695111.1571619407.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ll="118172"; _vwo_uuid_v2=DB3045C396C5D709046E1049F5F07FA34|f54de1bf7231171f795ae603cdc606cd; ap_v=0,6.0; _pk_id.100001.4cf6=435ba26303742682.1571619407.3.1571628963.1571627092.; _pk_ses.100001.4cf6=*; __utma=30149280.530360927.1571619407.1571624474.1571628963.3; __utmb=30149280.0.10.1571628963; __utma=223695111.1843168291.1571619407.1571624474.1571628963.3; __utmb=223695111.0.10.1571628963',
            }
    return head

def getHtml(url):
    result = requests.get(url, headers=getHeader())
    result.encoding = 'utf-8'
    html = etree.HTML(result.text)
    time.sleep(0.5)
    return html

def strToInt(str):
    resultArray = []
    for s in str:
        if s.isdigit():
            resultArray.append(s)
    return int(''.join(resultArray))

def get58Page(url):
    try:
        result = requests.get(url, headers=getHeader())
        result.encoding = 'utf-8'
        pageInfo = result.text.split('totalPage = ')[1][0:3]
        return strToInt(pageInfo)
    except:
        exit('读取页面数量的时候出了错误，链接:'+url)