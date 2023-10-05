import os
import pathlib
import re
import requests
import time
from flask import Flask, render_template, session, abort, redirect, request, flash, url_for, jsonify

from flask_wtf import FlaskForm

#####
#  app init
#####
app = Flask("__name__")
app.secret_key = "312312435342654363@#@!#%@%#4"

#####
# app start
#####
def testurl(url):
    command = r'curl --connect-timeout 2 -sIL -w "%{http_code}\n" -o /dev/null ' + "" + url
    result = os.popen(command)
    context = result.read()
    result.close()
    return context

@app.route("/",methods=["POST","GET"])
def index():
    if request.method == "POST" :
        url = request.form["url"]
        blocklist = [" ","&",";","@","%","^","~","`","<",">",",","ls","cat","less","tail","more","whoami","pwd","echo"]
        for item in blocklist:
            if item in url:
                return render_template('index.html',msg="command injection keyword detected!!!")
        return render_template('index.html',msg="status code:"+testurl(url))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(threaded=True)
