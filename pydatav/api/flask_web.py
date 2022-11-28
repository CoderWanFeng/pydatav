#!/usr/bin/env python
# -*- coding:utf-8 -*-

#############################################
# File Name: flask_web.py
# 公众号/B站/小红书/抖音: 程序员晚枫
# Mail: 1957875073@qq.com
# Created Time:  2022-11-25 10:17:34
# Description: 有关flask的datav操作
#############################################

from flask import Flask, render_template

# import config

app = Flask(__name__)


# app.config.from_object(config)


@app.route('/flask_demo')
def index():
    return render_template('../resources/templates/index.html')


if __name__ == '__main__':
    app.run()
