#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Author  ：程序员晚枫，B站/抖音/微博/小红书/公众号
@WeChat     ：CoderWanFeng
@Blog      ：www.python-office.com
@Date    ：2022/12/25 22:07
@Description     ：
'''

from abc import ABC, abstractmethod


class ExcelParser(ABC):
    """
    解析Excel数据的接口，返回一个字典，给pyecharts填充数据用
    """
    @abstractmethod
    def getExcelData(self):
        pass