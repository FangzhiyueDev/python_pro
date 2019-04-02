# !usr/bin/python
# coding=UTF-8

import subprocess

child = subprocess.Popen(["ping", "-c", "5", "www.baidu.com"]);

