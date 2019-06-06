#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json

import requests
from bs4 import BeautifulSoup


# 图灵API
class TuLing:
    key = '2d4888af6be643e18be1703afb9bd659'
    headers = {'User-Agent':
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}

    def tuling(self, message):
        url = 'http://www.tuling123.com/openapi/api?key=%s&info=%s' % (self.key, message)

        content = BeautifulSoup(requests.get(url=url, headers=self.headers).content, "lxml").get_text()

        dic_json = json.loads(content)
        return dic_json['text']


if __name__ == '__main__':
    tuling = TuLing()
    print(tuling.tuling('时间'))
