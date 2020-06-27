import http.client,requests
from TestTinyShopDDT.TestTinyShopDDT.common.login import Login

'''
1. 建立连接
2. 构建正文和header
3. 发起请求
4. 读取页面
'''

#添加到购物车
conn = http.client.HTTPConnection('192.168.0.188')

sessionid = Login().login()
print(sessionid)
param = 'id=84&num=1'
header = {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8', 'Cookie': sessionid,'X-Requested-With': 'XMLHttpRequest'}

conn.request('POST','/TinyShop_v1.7/index.php?con=index&act=cart_add',param,header)

response = conn.getresponse().read()
print(response.decode())

