#!/usr/bin/python
# !coding=utf-8


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys



from selenium.webdriver.support.select import Select





sys.path.append("/usr/lib/python3.6/")

user = "201604040222"
passw = "272577"

netType = ["@cmcc", "@edu", "@jift", "@oa", "@telecom", "@unicom"]

browser = webdriver.Firefox()
browser.get("http://192.168.27.190/srun_portal_pc?ac_id=1&srun_wait=1&theme=basic1")

username = browser.find_element_by_id("username")
password = browser.find_element_by_id("password")

username.send_keys(user)
password.send_keys(passw)

selectNet = browser.find_element_by_id("domain")
Select(selectNet).select_by_value(netType[1])

browser.find_element_by_id("login").click()
