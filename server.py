from flask import Flask, render_template #追加
import pymysql #追加
import time
import datetime
from flask import render_template, url_for
from flask import request
import numpy 
import json

app = Flask(__name__)

@app.route('/')
def hello():

    #db setting
    db = pymysql.connect(
            host='127.0.0.1',
            user='mask',
            password='',
            db='mask',
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
        )
    day = datetime.date.today()
    today1= datetime.timedelta(days=1)
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
    sql4= "SELECT day, COUNT( day ) as count1 FROM mask WHERE day="+"'"+str(day)+"'"+"and okorng='ok' GROUP BY day;"
    sql5= "SELECT day, COUNT( day ) as count1 FROM  mask WHERE day="+"'"+str(day)+"'"+"and okorng='ng' GROUP BY day;"
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
    if str(members4) == '()':
        members4="null"
    else:
        print(str(members4))
    print("配列")
    day="day"
    count1="count1"
    if members4=='null':
        print("0")
        members7="null"
    else:
            for member4 in members4:
             print(str(member4[day])+":マスクをしている人数"+str(member4[count1])+"人")
             members7=str(member4[count1])
    print("6")
    if str(members5)=='()':
        members5="null"
        print("0")
        members8="null"
    else:
            for member5 in members5:
             print(str(member5[day])+":マスクをしていない人数"+str(member5[count1])+"人")
             members8=str(member5[count1])
    cur.close()
    cur1.close()
    cur2.close()
    cur3.close()
    cur4.close()
    cur5.close()
    db.close()

    return render_template('hello.html', title='flask test', members=members, members1=members1, members2=members2, members3=members3,members4=members4, members5=members5,members7=json.dumps(members7),members8=json.dumps(members8)) #変更

app.run(port="80")
