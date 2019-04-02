#! /usr/bin/python
# coding=utf-8

import os
import sys
import requests


def getHtml():
    responseU = requests.request("get", "http://www.baidu.com");
    print(responseU.content)

    contentUrl = responseU.content;

    file = open("baidu.html", "w", 1);

    contentStr = str(contentUrl);

    file.write(contentStr);
    pass


def getImage():
    responseImg = requests. \
        request("get", "https://sp3.baidu.com/-0U_dTmfKgQFm2e88IuM_a/ps_fp.htm?pid" \
                       "=superman&fp=undefined&im=undefined&wf=undefined&br=" \
                       "3&qid=0xddd34d30000193a2&bi=EEC3C5F040C47119E9C991FDF2C6667F:FG=1")
    contentImg = responseImg.content;

    file = open("fang.img", "w", 1)

    contentStr = str(contentImg);

    file.write(contentStr)
    pass


reqParam = {
    "_cr1": 35329,
    "_ss": 1,
    "bs": "百度",
    "clist": "",
    "csor": 0,
    "f": 8,
    "f4s": 1,
    "hsug": "",
    "ie": {
        0: "urf-8",
        1: "utf-8"
    },
    "isid": "e6b4a76400026ec6",
    "issp": 1,
    "mod": 1,
    "newi": 1,
    "oq": "%E7%99%BE%E5%BA%A6",
    "rqlang": "cn",
    "rsv_bp": 1,
    "rsv_enter": 0,
    "rsv_idx": 2,
    "rsv_iqid": "0xddd34d30000193a2",
    "rsv_pq": "e6b4a76400026ec6",
    "rsv_sid": "1424_21096_26350",
    "rsv_spt": 1,
    "rsv_sug1": 19,
    "rsv_sug3": 10,
    "rsv_sug4": 3766,
    "rsv_sug7": 100,
    "rsv_t": "c35fYYnTfx6v9DJzvZ5rrO1dfCvR7nYzEP8v+Ajaqc7ULNuUkdy8YxYbxM022Rm5jX5a",
    "tn	": "baiduhome_pg",
    "wd": "百度"
}


# def Search():
#     # with open() as file:
#     #     file.write();
#     # dictoryReq = {
#     #     "_cr1": "35329"
#     #
#     # }
#     response = requests.get("http://www.baidu.com", Any=reqParam);
#     print(str(response.content))
#     file = open("two.html", "w", 1)
#     file.write(str(response.content))
#     pass


# getHtml();

# getImage();

# Search();




