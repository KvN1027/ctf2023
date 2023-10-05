from flask import Flask, redirect, url_for, render_template,request,flash,session
import random
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY']= 'meowmeow'


def checklogin(ac,pw):
    try:
        con = sqlite3.connect('main.db', check_same_thread=False)
        cur=con.cursor()
        cur.execute(f"SELECT * FROM user WHERE (username='{ac}') AND (password='{pw}')")
        res = cur.fetchone()
        con.close()
        return res
    
    except Exception as err:
        return err

@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "POST":
        user = request.form["ac"]
        password = request.form["pw"]
        return render_template("index.html",logininfo=checklogin(user,password))
    else:
        session["iflogin"] = "no"
        return render_template("index.html",logininfo="")


if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0",port=80)