# -*- coding:utf-8 -*- #
#!/usr/bin/env python3

from urllib import request, parse
import gzip
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/43.0.2357.81 Chrome/43.0.2357.81 Safari/537.36'
mycookie = '__cfduid=d153c0bc92db181d19b6b324c3f4608011444920557; u2=5459a00bae846eeee64ed0764be95dbf; CNZZDATA1254027205=1637341038-1444915444-%7C1445165802'

def ungzip(data):
    try:
# 尝试解压
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data

def sign(host = 'www.miaoss.net',UA = None,mycookie = None):
    url = 'http://' + host + '/api.php?cmd=gift500mb'
    req = request.Request(url)
    req.add_header('User-Agent', UA)
    req.add_header('Cookie',mycookie)
    req.add_header('Host',host)
    req.add_header('Referer','http://' + host + '/panel.php')
    req.add_header('X-Requested-With','XMLHttpRequest')
    req.add_header('Connection','keep-alive')
    req.add_header('Accept','*/*')
    req.add_header('Accept-Encoding','gzip,deflate, sdch')
    req.add_header('Accept-Language','zh-CN,zh;q=0.8')
    with request.urlopen(req) as f:
        f = ungzip(f.read())
        print(f.decode()+"\n主人，已经为您完成签到了")
if __name__ == "__main__":
      sign('www.miaoss.net',UA,mycookie)
