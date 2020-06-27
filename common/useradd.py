import time,http.client
from common.Login_Background import Log
class user_add:
    def add(self):
        sessionid = Log().login()
        url = '/TinyShop_v1.7/index.php?con=customer&act=customer_save'
        param = 'name=哈哈la&password=123456&repassword=123456&email=1lahjdycbbr2%40tiny.com&' \
                'real_name=121&sex=0&birthday=&province=210000&city=210600&county=210681&' \
                'addr=&phone=&mobile=&point=0'
        header = {'Content-type':'application/x-www-form-urlencoded','Cookie':sessionid}
        conn = http.client.HTTPConnection('192.168.0.188')
        conn.request('POST',url,param.encode(),header)
        response = conn.getresponse().read()
        print(response.decode())
if __name__ == '__main__':
    s = user_add().add()
    print(s)