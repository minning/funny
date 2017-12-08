# coding:utf-8
'''
    Author:minning
    Date:2017/12/8
    代码目的：
    
'''

import json
import sys
import time
import urllib2

import itchat

reload(sys)  # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入
sys.setdefaultencoding('utf-8')  # 这个是解决合成中文文本的时候，Unicode 和 utf-8 编码问题的，可以尝试注释掉会不会报错

newInstance = itchat.new_instance()
newInstance.auto_login(hotReload=True, statusStorageDir='newInstance.pkl')
# itchat.auto_login(hotReload=True)
newInstance.login()
# newInstance.run()

while True:
    # 调用和风天气的 API
    url = 'https://api.heweather.com/x3/weather?cityid=CN101010100&key=12d3f43d4b9c48eb9d1d7e8902795aa2'
    req = urllib2.Request(url)
    resp = urllib2.urlopen(req).read()
    # itchat.send(u'你好　minning', 'filehelper')

    # 将 JSON 转化为 Python 的数据结构
    json_data = json.loads(resp)
    data = json_data['HeWeather data service 3.0'][0]

    # 获取 PM2.5 的值
    pm25 = data['aqi']['city']['pm25']

    # 获取空气质量
    air_quality = data['aqi']['city']['qlty']

    # 获取城市
    city = data['basic']['city']

    # 获取现在的天气、温度、体感温度、风向、风力等级
    now_weather = data['now']['cond']['txt']
    now_tmp = data['now']['tmp']
    now_fl = data['now']['fl']
    now_wind_dir = data['now']['wind']['dir']
    now_wind_sc = data['now']['wind']['sc']

    # 今天的天气
    today = data['daily_forecast'][0]
    weather_day = today['cond']['txt_d']
    weather_night = today['cond']['txt_n']
    tmp_high = today['tmp']['max']
    tmp_low = today['tmp']['min']
    wind_dir = today['wind']['dir']
    wind_sc = today['wind']['sc']
    # 天气建议

    # 舒适度
    comf = data['suggestion']['comf']['brf']
    comf_txt = data['suggestion']['comf']['txt']

    # 流感指数
    flu = data['suggestion']['flu']['brf']
    flu_txt = data['suggestion']['flu']['txt']

    # 穿衣指数
    drsg = data['suggestion']['drsg']['brf']
    drsg_txt = data['suggestion']['drsg']['txt']

    newInstance.send("开始天气预报", 'filehelper')
    time.sleep(1)
    newInstance.send("{}".format(time.strftime('%Y年%m月%d日 %H：%M',time.localtime(time.time()))), 'filehelper')
    time.sleep(1)
    newInstance.send("地址 : {}".format('北京'), 'filehelper')
    newInstance.send("pm25 : {}".format(pm25), 'filehelper')
    newInstance.send("空气质量 : {}".format(air_quality), 'filehelper')
    newInstance.send("天气 : {}".format(now_weather), 'filehelper')
    newInstance.send("温度 : {}摄氏度".format(now_tmp), 'filehelper')
    newInstance.send("气温 : {}".format(drsg), 'filehelper')
    time.sleep(1)
    newInstance.send("本次天气预报报道完毕", 'filehelper')
    time.sleep(3600)

