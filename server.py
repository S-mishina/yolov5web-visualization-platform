from flask import Flask, render_template #追加
import pymysql #追加
import time
import datetime

app = Flask(__name__)

@app.route('/')
def hello():

    #db setting
    db = pymysql.connect(
            host='127.0.0.1',
            user='test',
            password='',
            db='mask',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )
    day = datetime.date.today()
    today1= day_after_tomorrow = datetime.timedelta(days=1)
    day1=day-today1
    print(str(day1))
    cur = db.cursor()
    cur1 = db.cursor()
    cur2 = db.cursor()
    cur3 = db.cursor()
    sql = "SELECT * FROM `mask`"
    sql1 = "SELECT * FROM `mask` ORDER BY day desc LIMIT 0, 5 ;"
    sql2 = "SELECT * FROM `mask` WHERE `day` = '"+str(day)+"'"+ ";"
    sql3 = "SELECT * FROM `mask` WHERE `day` = '"+str(day1)+"'"+ ";"
    cur.execute(sql)
    cur1.execute(sql1)
    cur2.execute(sql2)
    cur3.execute(sql3)
    members = cur.fetchall()
    members1 = cur1.fetchall()
    members2 = cur2.fetchall()
    members3 = cur3.fetchall()
    print("1")
    print(members)
    print("2")
    print(members1)
    print("3")
    print(members2)
    print("4")
    print(members3)
    cur.close()
    cur1.close()
    cur2.close()
    cur3.close()
    db.close()

    return render_template('hello.html', title='flask test', members=members, members1=members1, members2=members2, members3=members3) #変更

app.run(debug=True)
