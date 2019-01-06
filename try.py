# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
import datetime
from flask import render_template
import requests
import json

app = Flask(__name__)

@app.route('/dianying' , methods=['GET','POST'])
def signin():
    try:
    # if True:
        if request.method == 'GET':
            return render_template(
                # 渲染模板语言
                'dianying.html',
                chaxun_list='',
            )
        else:
            apikey = 'FtN450TyUVCzWwF2bheo0Sg2xuvC5grFK8cwI1Kh8FQgcbjxLLYronJsizNIXESW'
            url = 'http://api01.idataapi.cn:8000/movie/douban'
            s = requests.session()
            datas = request.form
            r = s.get(url,params={'apikey':apikey,
                                'kw':datas['name'],
                                'catid':'',})

            try:
                d = json.loads(r.text)['data']
            except:
                return render_template(  # 渲染模板语言
                    'dianying.html',
                    chaxun_list=[])
            chaxun = []
            for i in d:
                chaxun.append({'img':i['coverUrl'],
                               'title':i['title'],
                               'rating':i['rating'],
                               'ratingCount':i['ratingCount'],

                    'directors':[[] if i['directors'] is None else i['directors']],
                               'actors':[[] if i['actors'] is None else i['actors']],
                               'tags':[[] if i['tags'] is None else i['tags']],
                    'durationMin':i['durationMin'],
                               'releaseDates':[[] if i['releaseDates'] is None else i['releaseDates']],
                               'countries': [[] if i['countries'] is None else i['countries']]
                               })

            return render_template(# 渲染模板语言
                    'dianying.html',
                    chaxun_list=chaxun,
                    )
    except Exception as e:
        print (e)
        return '0'

@app.route('/shuji' , methods=['GET','POST'])
def shuji():
    try:
    # if True:
        if request.method == 'GET':
            return render_template(
                # 渲染模板语言
                'shuji.html',
                chaxun_list='',
            )
        else:
            apikey = 'FtN450TyUVCzWwF2bheo0Sg2xuvC5grFK8cwI1Kh8FQgcbjxLLYronJsizNIXESW'
            url = 'http://api01.idataapi.cn:8000/book/douban'
            s = requests.session()
            datas = request.form
            r = s.get(url,params={'apikey':apikey,
                                'kw':datas['name'],
                                'catid':'',})
                                # 'id':1})

            try:
                d = json.loads(r.text)['data']
            except:
                return render_template(  # 渲染模板语言
                    'shuji.html',
                    chaxun_list=[])
            chaxun = []
            for i in d:
                chaxun.append({'img':i['coverUrl'],
                               'title':i['title'],
                               'rating':i['rating'],
                               'ratingCount':i['ratingCount'],
                                'writers':[[] if i['writers'] is None else i['writers']],
                               'publishOrg':i['publishOrg'],
                               'pageNum':['' if i['pageNum'] is None else int(i['pageNum'])],
                                'pressDate':i['pressDate'],
                               'price':i['price'],
                               })

            return render_template(# 渲染模板语言
                    'shuji.html',
                    chaxun_list=chaxun,
                    )
    except Exception as e:
        print (e)
        return '0'


if __name__=='__main__':
    app.run(
	host='0.0.0.0',
        port=8000,
        debug=True
    )
