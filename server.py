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
    cur4 = db.cursor()
    cur5 = db.cursor()
    sql = "SELECT * FROM `mask`"
    sql1 = "SELECT * FROM `mask` ORDER BY day desc LIMIT 0, 5 ;"
    sql2 = "SELECT * FROM `mask` WHERE `day` = '"+str(day)+"'"+ ";"
    sql3 = "SELECT * FROM `mask` WHERE `day` = '"+str(day1)+"'"+ ";"
    sql4= "SELECT COUNT(test) FROM mask WHERE test ='ok' and day ='"+str(day)+"'"
    sql5= "SELECT COUNT(test) FROM mask WHERE test ='ng' and day ='"+str(day)+"'"
    cur.execute(sql)
    cur1.execute(sql1)
    cur2.execute(sql2)
    cur3.execute(sql3)
    cur4.execute(sql4)
    cur5.execute(sql5)
    members = cur.fetchall()
    members1 = cur1.fetchall()
    members2 = cur2.fetchall()
    members3 = cur3.fetchall()
    members4 = cur4.fetchall()
    members5 = cur5.fetchall()
    print("1")
    print(members)
    print("2")
    print(members1)
    print("3")
    print(members2)
    print("4")
    print(members3)
    print("5")
    print(members4)
    print("6")
    print(members5)
    cur.close()
    cur1.close()
    cur2.close()
    cur3.close()
    cur4.close()
    cur4.close()
    db.close()

    return render_template('hello.html', title='flask test', members=members, members1=members1, members2=members2, members3=members3,members4=members4,members5=members5) #変更

app.run(debug=True)
