import time,http.client
from selenium import webdriver
from common.Login_Background import Log
class recharge:
    def userRecharge(self):
        wb = webdriver.Firefox()
        time.sleep(1)
        wb.get('http://192.168.0.188/TinyShop_v1.7/index.php?con=admin&act=login')
        time.sleep(1)
        wb.find_element_by_xpath('/html/body/div/div/form/ul/li[1]/input').send_keys('admin')
        wb.find_element_by_xpath('/html/body/div/div/form/ul/li[2]/input').send_keys('123456')
        wb.find_element_by_xpath('/html/body/div/div/form/ul/li[3]/input').send_keys('aaaa')
        wb.find_element_by_xpath('/html/body/div/div/form/ul/li[4]/input[1]').click()
        time.sleep(1)
        wb.find_element_by_xpath('/html/body/div[1]/ul/li[3]/a').click()
        time.sleep(1)
        wb.find_element_by_xpath('/html/body/div[3]/div[2]/form/table/tbody/tr[3]/td[2]/div/a').click()
        time.sleep(1)
        wb.find_element_by_xpath('/html/body/div[3]/div[2]/form/table/tbody/tr[3]/td[2]/div/div/ul/li[1]/a').click()
        time.sleep(2)
        a = '/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/div/div/form/dl/dd/input'
        wb.find_element_by_xpath(a).send_keys('1')
        time.sleep(2)
        b = '/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[2]/td[2]/div/div/div/form/div/button'
        wb.find_element_by_xpath(b).click()
        # conn = http.client.HTTPConnection('192.168.0.188')
        # conn.request('GET','/TinyShop_v1.7/index.php?con=customer&act=balance_op&user_id=72&type=2&amount=1')
        # setcookie = conn.getresponse().getheader('Set-Cookie')
        # sessionid = setcookie.split(';')[0]
        # header = {'Content-type':'application/x-www-form-urlencoded','Cookie':sessionid}
        # conn = http.client.HTTPConnection('192.168.0.188')
        # conn.request('GET','/TinyShop_v1.7/index.php?con=customer&act=customer_list',"",header)
        # response = conn.getresponse().read()
        # print(response.decode())
if __name__ == '__main__':
    recharge().userRecharge()