#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

import requests
from bs4 import BeautifulSoup


# 图灵机器人
def tuling(message):
    headers = {'User-Agent':
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
    key = '2d4888af6be643e18be1703afb9bd659'
    url = 'http://www.tuling123.com/openapi/api?key=%s&info=%s' % (key, message)

    content = BeautifulSoup(requests.get(url=url, headers=headers).content, "lxml").get_text()

    dic_json = json.loads(content)
    return dic_json['text']


if __name__ == '__main__':
    print(tuling('时间'))
