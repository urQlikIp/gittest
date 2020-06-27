import pymysql

def exeSql(sql):
    host = 'localhost'
    user = 'root'
    passwd = ''
    database = 'chat'
    db = pymysql.connect(host, user, passwd, database,charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        db.commit() #提交到数据库执行
        results = cursor.fetchall() #取得所有数据
        print(results)
        return results
    except:
        db.rollback()       #发生错误数据回滚
    db.close()


if __name__ == '__main__':
    import time
    addr = '127.0.0.1'
    d = '测'
    sql = 'INSERT INTO conversation(addr, time, content) VALUES (\''+str(addr)+'\' , \''+time.ctime()+'\', \''+d+'\')'
    print(sql)
    exeSql(sql)