#! -*- encoding:utf-8 -*-

import requests
import random

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
resp = requests.get(targetUrl, proxies=proxies, headers=headers)

print(resp.status_code)
print(resp.text)