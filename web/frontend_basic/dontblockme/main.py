from flask import Flask, redirect, url_for, render_template,request,flash,session,make_response,render_template_string

app = Flask(__name__)


@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "POST" :
            return r"flag{wanna_ser_ser}"
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=80)