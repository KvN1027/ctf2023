from flask import Flask, redirect, url_for, render_template, request, flash, session
import random
import sqlite3
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

flag = r'flag{sql_injection1}'

BLACKLIST = ['alter', 'begin', 'cast', 'create', 'cursor','distinct', 'declare', 'delete', 'drop', 'end',
            'exec', 'execute', 'fetch', 'insert', 'kill', 'sys', 'sysobjects',
            'syscolumns', 'table', 'update']

@app.before_first_request
def sqlite_generate():
    con = sqlite3.connect('main.db')
    cursor = con.cursor()


    cursor.execute('''CREATE TABLE IF NOT EXISTS user 
    (id INT PRIMARY KEY NOT NULL,
    username TEST NOT NULL,
    password TEST NOT NULL);''')
    con.commit()
    try:
        cursor.execute(f"SELECT * FROM user WHERE (username='admin')")
        res = cursor.fetchone()
        con.commit()
    except Exception as err:
        print(err)
    print("res===>", res)
    if (not res):
        cursor.execute(f'''INSERT INTO user (id,username,password)
        VALUES (0, 'admin', '{os.urandom(10).hex()}' );''')
        con.commit()

    cursor.close()
    con.close()


def checklogin(ac, pw):
    try:
        if any(blacklisted_word in ac.lower() for blacklisted_word in BLACKLIST):
            return 3
        if any(blacklisted_word in pw.lower() for blacklisted_word in BLACKLIST):
            return 3
        con = sqlite3.connect('main.db', check_same_thread=False)
        cur = con.cursor()
        cur.execute(
            f"SELECT * FROM user WHERE (username='{ac}') AND (password='{pw}')")
        res = cur.fetchone()

        if res:
            con.close()
            return True
        else:
            con.close()
            return False
    except Exception as err:
        con.rollback()
        con.close()
        return False


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        user = request.form["ac"]
        password = request.form["pw"]
        if checklogin(user, password) == 3:
            return "WARNING: DO NOT TRY TO CHANGE OR REWRITE THE FLAG"
            
        if checklogin(user, password):
            return flag
        else:
            return render_template("index.html", logininfo="somthing must error")
    else:
        session["iflogin"] = "no"
        return render_template("index.html", logininfo="")


if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=80)
