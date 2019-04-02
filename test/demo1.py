# ! /usr/bin/python
# ! coding=utf-8


import urllib.request
import json


def parse_weather_with_set(value):
    for data in value:
        if isinstance(data, dict):  # 代表的是字典的实例
            for dictKey, dictValue in data:
                print(dictKey, ":\t", dictValue)
    pass


def parse_json_with_string(dicts={}):
    info = dicts.get("message")
    if info == "success":
        print("执行成功，取得数据")
        data = dicts.get("data")
        weather_dict = data.get("weather")
        for key, value in weather_dict.items():
            if isinstance(value, set):
                parse_weather_with_set(value)

            else:
                print(key, ":\t", value)
    else:
        print("没有取得正常数据")


param = "北京".encode("utf-8")

response = urllib.request. \
    urlopen("https://www.toutiao.com/stream/widget/local_weather/data/?city={}".format(param))

responseObj = response.read().decode("utf-8")

jsonObj = json.loads(responseObj)

parse_json_with_string(jsonObj)


