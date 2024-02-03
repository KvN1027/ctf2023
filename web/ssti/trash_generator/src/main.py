from flask import Flask, redirect, url_for, render_template,request,flash,session,render_template_string
import random
def trunk(ip):
    a=  random.randint(0,4)
    if a== 0 :
        return "你说的对，但是《{}》是由米哈游自主研发的一款全新开放世界冒险游戏。游戏发生在一个被称作「提瓦特」的幻想世界，在这里，被神选中的人将被授予「神之眼」，导引元素之力。你将扮演一位名为「旅行者」的神秘角色在自由的旅行中邂逅性格各异、能力独特的同伴们，和他们一起击败强敌，找回失散的亲人——同时，逐步发掘「原神」的真相。".format(ip)
    if a== 1 : 
        return "網路很美好，但下載不了{}。鳥要脫出殼，但這就是世界".format(ip)
    if a== 2 :
        return "睡眠的拼音是shui mian，失眠的拼音是shi mian，你看，少了{}，整個字都變得不一樣了。".format(ip)
    if a== 3 : 
        return "昨天坐捷運上班，看到捷運站外面有{}在賣餅乾，想說跟他買一包當下午茶，結果走上前的時候他，看了我一下就說，誒 你怎麼賣這麼快，都賣完了喔?".format(ip)
    if a== 4 :
        return "店員：「請問末三碼及貴姓？」顧客：「123 {}」，店員：「啊 ～ 天亮啦 下雨啦 出門吧 騎在平常載你的路邊小狗互相追逐 我騎著破車走在柳暗花遮的建國路 平常沒差但現在看不順眼的行道樹 或許我就是你口中發情的灰兔 」".format(ip)
app = Flask(__name__)
app.config['SECRET_KEY']= 'meowmeow'

@app.route('/',methods=["POST","GET"])
def index():
    if request.method == "POST":
        msg = request.form["msg"]
        msg = trunk(msg)
        html = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>廢文產生器</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.2.1/css/all.min.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.3/css/bulma.min.css">
    <script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
    
</head>

<body>  
    <section class="section"  >
        <div class="container">
            <div class="column is-6 is-offset-3">
                <div class="box has-text-centered">
                    <br>
                    <h1 class="title">廢文產生器</h1>
                    <h1 class="subtitle"></h1>
                    <br>
                    <form action="/" method="POST">
                        <div class="field">
                            <div class="control">
                              <input class="input" type="text" name="msg" placeholder="e.x 貓咪">
                            </div>
                          </div>
                          <div class="field">
                            <div class="control">
                                <button class="button is-primary">Submit</button>
                              </div>
                          </div>
                    </form>
                    <p class="has-text-danger">{} </p>
                </div>
            </div>
            <div class="column is-6 is-offset-3">
                
            </div>
        </div>
    </section>
</body>
</html>
'''.format(msg)
        return render_template_string(html)
    else:
        return render_template("index.html")



if __name__ == "__main__":

    app.run(threaded=True)