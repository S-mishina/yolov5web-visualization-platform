from flask import Flask, render_template #追加
import pymysql #追加

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

    cur = db.cursor()
    cur1 = db.cursor()
    sql = "SELECT * FROM `mask`"
    cur.execute(sql)
    members = cur.fetchall()
    sql1 = "SELECT * FROM `mask` WHERE 1 ORDER BY day LIMIT 0, 1"
    cur.execute(sql1)
    members1 = cur.fetchall()
    print(members1)


    cur.close()
    db.close()

    return render_template('hello.html', title='flask test', members=members) #変更

if __name__ == "__main__":
    app.run(debug=True)