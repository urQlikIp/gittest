# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re




class Setup:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://www.baidu.com')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

Setup()
