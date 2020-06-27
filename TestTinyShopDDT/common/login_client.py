import http.client

'''
1. 请求连接
2. 拼装发送内容
3. 发送请求
4. 获取响应
'''

class Login():
    def login(self):
        conn = http.client.HTTPConnection('192.168.0.188')

        para = 'redirectURL=%2FTinyShop_v1.7%2Findex.php%3Fcon%3Dindex%26act%3Dproduct%26id%3D20&email=eiyo1314%40163.com&password=123456'
        header = {'Content-Type': 'application/x-www-form-urlencoded','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}

        conn.request('POST','/TinyShop_v1.7/index.php?con=simple&act=login_act',para,header)
        response = conn.getresponse().read().decode()
        if '不正确' in response:
            print('Client log in failed!')
        else:
            print('Client log in successfully!')

        conn.request('POST','/TinyShop_v1.7/index.php?con=simple&act=login_act',para,header)
        setcookie = conn.getresponse().getheader('Set-Cookie')
        sessionid = setcookie.split(';')[0]

        return sessionid

if __name__ == '__main__':
    s = Login().login()
    print(s)

