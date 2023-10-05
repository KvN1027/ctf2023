from flask import Flask, redirect, url_for, render_template, request, flash, session, make_response
import random
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'meowmeow'

@app.route('/panel',methods=["GET"])
def panel():
    if session.get("iflogin") != "yes" :
        return redirect("/")
    role = request.cookies.get('role')
    if role == "admin":
        if request.headers.get('X-Forwarded-For') == 'localhost' or request.headers.get('X-Forwarded-For') == '127.0.0.1':
            return render_template("index.html", info=r"歡迎回來，admin",role=role,admin=1)
        else:
            return render_template("index.html", info="警告! admin IP並非來自於localhost，故無法查看帳務資訊 !!!",role=role)

    else:
        role=request.cookies.get('role')
        if role == None :
            resp = make_response(render_template("index.html", info="只有admin可以查看帳務資訊",role="guest"))
            resp.set_cookie(key='role', value='guest')
            return resp
        else :
            return render_template("index.html", info="只有admin可以查看帳務",role=role)

@app.route('/logout')
def logout():
    session["iflogin"] = "no"
    return redirect("/")


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        ac = request.form["account"]
        pw = request.form["password"]
        if ac == "guest" and pw == "1234":
            session["iflogin"] = "yes"
            return redirect("/panel")
        else :
            return render_template("login.html",msg="帳號/密碼有誤")
    else :
        session["iflogin"] = "no"
        return render_template("login.html")
    

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)