import http.client
class Log:
    def login(self):
        conn = http.client.HTTPConnection('192.168.0.188')
        conn.request('GET','/TinyShop_v1.7/index.php?con=admin&act=login')
        setcookie = conn.getresponse().getheader('Set-Cookie')
        sessionid = setcookie.split(';')[0]
        param = 'name=admin&password=123456&verifycode=aaaa'
        url = '/TinyShop_v1.7/index.php?con=admin&act=check'
        header = {'Content-type':'application/x-www-form-urlencoded','Cookie':sessionid}
        conn = http.client.HTTPConnection('192.168.0.188')
        conn.request('POST',url,param,header)
        conn = http.client.HTTPConnection('192.168.0.188')
        conn.request('GET','/TinyShop_v1.7/index.php?con=admin&act=index')
        response = conn.getresponse().read()
        print(response.decode())
        if response.decode() == "":
            print("successful ！")
        else:
            print("fail ！")

        return sessionid
# s = Log().login()
# print(s)