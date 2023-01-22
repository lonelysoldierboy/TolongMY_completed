# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 03:00:46 2022

@author: 60122
"""

from selenium import webdriver


driver = webdriver.Chrome(r'C:\Users\60122\Documents\webdriver\chromedriver.exe')
url = "https://whatmylocation.com/"
driver.get(url)
latitude = driver.find_element("xpath" , '//*[@id="latitude"]')
longitude = driver.find_element("xpath", '//*[@id="longitude"]')
Address = driver.find_element("xpath", '//*[@id="address"]')
print(latitude.text,longitude.text)
print(Address.text)

