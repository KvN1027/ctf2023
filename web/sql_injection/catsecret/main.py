from flask import Flask, redirect, url_for, render_template,request,flash,session
import random
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY']= 'meowmeow'


def checklogin(ac,pw):
    try:
        con = sqlite3.connect('main.db', check_same_thread=False)
        cur=con.cursor()
        cur.execute(f"SELECT * FROM user WHERE (user='{ac}') AND (password='{pw}')")
        res = cur.fetchone()
        
        if res :
            con.close()
            return True
        else :
            con.close()
            return False
    except Exception as err:
        con.rollback()
        con.close()
        return False

@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "POST":
        user = request.form["ac"]
        password = request.form["pw"]
        if checklogin(user,password):
            return r"flag{i_said_so_secrettttttt}"
        else :
            return render_template("index.html",logininfo="somthing must error")
    else:
        session["iflogin"] = "no"
        return render_template("index.html",logininfo="")


@app.route("/<user>") 
def user(user): 
    if session.get("iflogin") == "yes" : #如果iflogin這個session是yes的話，執行渲染出正確的頁面
        return render_template("user.html",user=user)
    else : #否則就跳轉回index.html，不可以壞壞
        return redirect("/")

@app.route('/all',methods=["POST","GET"])
def posts():
    if request.method == "POST":
        content = request.form["content"]
        account = session["user"]
        try:
            con = sqlite3.connect('info.db', check_same_thread=False)
            cur=con.cursor()
            cur.execute("INSERT INTO allpost(account, post) VALUES('{}','{}');".format(
                account, content))
            con.commit()
            con.close()
            return redirect("/all")
        except Exception as err:
            con.rollback()
            con.close()
            print(err)
    else:
        if session.get("iflogin") == "yes" :
            con = sqlite3.connect('info.db', check_same_thread=False)
            cur=con.cursor()
            cur.execute("SELECT account,post FROM allpost")
            allpostlist = cur.fetchall()
            con.close()
            return render_template("all.html",posts=allpostlist)
        else :
            return redirect("/")


if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0",port=80)