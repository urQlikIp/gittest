from selenium import webdriver
import time,xlrd,xlwt
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class Excel:
    #   读取excel的方法, 返回sheet对象
    def read_it(self, file_path, index = 0):
        #   打开指定路径的excel
        data = xlrd.open_workbook(file_path)
        #   获取整个sheet对象
        sheet = data.sheets()[index]
        return sheet

    def fast_read(self):
        table = self.read_it('C:\\Users\\Administrator\\PycharmProjects\\oaDemo\\data\\testPara.xlsx')
        return table

    def fast_write(self):
        wb = xlwt.Workbook()
        ws = wb.add_sheet('testsheet')
        ws.write(0,0,'test')
        wb.save('testPara.xls')
