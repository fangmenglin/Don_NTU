#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/10 16:37
# @Author  : blvin.Don
# @File    : detection.py
#
# Detecting an URL whether or not accessible
import requests, time
def detector(url):
    time.sleep(1)
    result = ''
    r = requests.get(url=url)
    if r.status_code == 404:
        result = True
    else:
        result = False
    # print("检测结果：", result)
    return  result

# print(detector('https://github.com/kreattang/Don_NTUqweqweyu'))