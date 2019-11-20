import random
import requests
from lxml import etree
import time
import json
import pymysql
import datetime

my_headers =[
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    '''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36''',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 GTB6 (.NET CLR 3.5.30729)',
    'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.125 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; rv:44.0) Gecko/20100101 Firefox/44.0',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1229.79 Safari/537.4',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.813.0 Safari/535.1',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0',
    'Mozilla/5.0 (Windows NT 6.1; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:28.0) Gecko/20100101 Firefox/28.0',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.34 (KHTML, like Gecko) Qt/4.8.2',
    'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
    'Mozilla/3.0 (compatible; Indy Library)',
    'Mozilla/5.0 (Windows NT 5.1; rv:32.0) Gecko/20100101 Firefox/32.0',
    'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.813.0 Safari/535.1',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; ReadSharp/6.3.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1736.2 Safari/537.36 OPR/20.0.1380.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; MRA 4.4 (build 01334); .NET CLR 1.1.4322)',
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; ru; rv:1.9.0.1) Gecko/2008070208',
    'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/29.0.1547.76 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.27+ (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27',
    'Mozilla/5.0 (Windows NT 5.2; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0/puffin',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; MSN OptimizedIE8;NLNL)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.3 GD',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C; .NET CLR 3.5.30729; .NET CLR 2.0.50727; .NET CLR 3.0.30729; InfoPath.3 GD',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3'
]

def getHeader():
    #  设置IP切换头
    tunnel = random.randint(1, 10000)
    head = {
            'user-agent': random.choice(my_headers),
            'Cookie': 'bid=6MigHW5BotY; __utmc=30149280; __utmz=30149280.1571619407.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmc=223695111; __utmz=223695111.1571619407.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ll="118172"; _vwo_uuid_v2=DB3045C396C5D709046E1049F5F07FA34|f54de1bf7231171f795ae603cdc606cd; ap_v=0,6.0; _pk_id.100001.4cf6=435ba26303742682.1571619407.3.1571628963.1571627092.; _pk_ses.100001.4cf6=*; __utma=30149280.530360927.1571619407.1571624474.1571628963.3; __utmb=30149280.0.10.1571628963; __utma=223695111.1843168291.1571619407.1571624474.1571628963.3; __utmb=223695111.0.10.1571628963',
            'Host':'movie.douban.com',
            "Proxy-Tunnel": str(tunnel),
            "Referer":'https://movie.douban.com/tag/#/?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&qq-pf-to=pcqq.c2c'
            }
    return head

def getJson(url):
    # 要访问的目标页面
    targetUrl = "http://httpbin.org/ip"

    # 代理服务器
    proxyHost = "u3748.5.tn.16yun.cn"
    proxyPort = "6441"

    # 代理隧道验证信息
    proxyUser = "16XDDLKP"
    proxyPass = "185276"

    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }

    # 设置 http和https访问都是用HTTP代理
    proxies = {
        "http": proxyMeta,
        "https": proxyMeta,
    }

    #  设置IP切换头
    tunnel = random.randint(1, 10000)
    headers = {"Proxy-Tunnel": str(tunnel)}

    # requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
    # s = requests.session()
    # s.keep_alive = False # 关闭多余连接
    # resp = requests.get(targetUrl, proxies=proxies, headers=headers)

    # s = requests.session()
    # s.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
    # result = s.get(url)
    try:
        result = requests.get(url, headers=getHeader(),allow_redirects=False,proxies=proxies)
    except:
        print("代理网站出现了错误。")
        time.sleep(round(random.uniform(28, 33)))
        try:
            result = requests.get(url, headers=getHeader(), allow_redirects=False, proxies=proxies)
        except:
            print("代理网站出现了错误。")
            time.sleep(round(random.uniform(28, 33)))
            result = requests.get(url, headers=getHeader(), allow_redirects=False, proxies=proxies)

    # result = requests.get(url, headers=getHeader(),allow_redirects=False,proxies=proxies,)
    result.encoding = 'utf-8'
    time.sleep(round(random.uniform(1, 3),2))
    return result

def getHtml(url):
    result = requests.get(url, headers=getHeader())
    result.encoding = 'utf-8'
    html = etree.HTML(result.text)
    time.sleep(round(random.uniform(1, 3),2))
    return html

detailUrlPart = 'https://movie.douban.com/j/subject_abstract?subject_id='
url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=';
i = 105
while i*20 < 10000:
    pageUrl = url+str(i*20)
    print("当前页为第"+str(i)+"页，找"+str(i*20) +"至"+str(i*20+20)+"的数据")
    print(pageUrl)
    i=i+1
    result = getJson(pageUrl)
    jsonData = json.loads(result.text)
    pageDataList = jsonData['data']
    if len(pageDataList):
        pageInfos = []
        for data in pageDataList:
            detailUrl = detailUrlPart + data['id']
            pageResult = getJson(detailUrl)
            pageJsonData = json.loads(pageResult.text)['subject']
            pageInfo = {}
            pageInfo['time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            pageInfo['url'] = detailUrl
            pageInfo['id'] = data['id']
            pageInfo['name'] = str(pageJsonData['title']).replace('"','\\"')
            pageInfo['area'] = pageJsonData['region']
            pageInfo['year'] = pageJsonData['release_year']
            pageInfo['score'] = pageJsonData['rate']
            pageInfoType = '暂无数据'
            if len(pageJsonData['types']):
                pageInfoType = ','.join(pageJsonData['types'])
            pageInfo['type'] = pageInfoType
            pageInfos.append(pageInfo)
            print("******************")
            print("爬取时间:" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            print("详情信息获取的url为：" + detailUrl)
            print("id:" + data['id'])
            print("名称：" + pageJsonData['title'])
            print("地区：" + pageJsonData['region'])
            print("年份：" + pageJsonData['release_year'])
            print("评分：" + pageJsonData['rate'])
            print("标签：" + pageInfoType)
            print("******************")
            print("")
            print("")
            print("")
        if pageInfos:
            db = pymysql.connect("10.10.1.209", "root", "Hxpti123", "ywtest")
            cursor = db.cursor()
            for data in pageInfos:
                try:
                    sql = 'insert into movie_from_db_copy1 (id, url, name, area, year, score, type, time ) values' + \
                           ' ({id:s},"{url:s}","{name:s}","{area:s}","{year:s}","{score:s}","{type:s}","{time:s}")' \
                               .format(id=data['id'], url=data['url'], name=data['name'],
                                       area=data['area'], year=data['year'],
                                       score=data['score'],type=data['type'],time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

                    cursor.execute(sql)
                    db.commit()
                except:
                    print("sql出错:" + sql)
                    print("出错url为："+pageUrl)
                    print("出错时i为："+i)
            cursor.close()
            db.close()
    else:
        print("此页面没找到数据，检查吧")
        print(pageUrl)
        exit(0)
