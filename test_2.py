from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import time

import requests


def logincmsadmin():
    profile = webdriver.FirefoxProfile()
    profile.accept_untrusted_certs = True   # bypass un-trusted web cert
    profile.set_preference('network.proxy.type', 0)   # set browswer= No proxy
    driver = webdriver.Firefox(firefox_profile=profile)
    driver.get("https://144.131.216.94/authenticate.html?url=%2findex.html")
    time.sleep(1)  # allow webgage to be fully loaded before reading webgage
    driver.find_element_by_name("0").clear()
    driver.find_element_by_name("0").send_keys('admin')
    driver.find_element_by_name("1").clear()
    driver.find_element_by_name("1").send_keys('admin')
    driver.find_element_by_class_name("button input").click()
    session=driver.get_cookies()
    print(driver.get_cookie('session'))


    time.sleep(1)
    driver.find_element_by_link_text("Status").click()
    driver.find_element_by_link_text("General").click()
    time.sleep(1)
    htmlContent=driver.page_source
    print(htmlContent)

    driver.close()
    print(session[0]['value'])
    url = 'https://{}/index.xml?_={}'.format('144.131.216.94',int(time.time() * 1000))  #
    header = {
        "Cookie": session[0]['value']
    }
    statusResponse = requests.request('GET', url, verify=False, headers=header)
    print(statusResponse.content)


if __name__=='__main__':
    logincmsadmin()
