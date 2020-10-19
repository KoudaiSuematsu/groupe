# flaskからFlaskをインポートしてきて使えるようにする
from flask import Flask, render_template, request, redirect
import sqlite3

# appという名前でFlaskを使いますよ
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/childcare")
def childcare():
    return render_template("childcare.html")


@app.route("/business")
def business():
    return render_template("business.html")


@app.route("/funny")
def funny():
    return render_template("funny.html")


@app.route("/edit", methods=["POST"])
def comment():
    # 入力フォームから値を取得
    age = request.form.get("age")
    sx_code = request.form.get("sx_code")
    comment = request.form.get("comment")
    # DB接続する
    conn = sqlite3.connect("comment.db")
    # データベースの中身が見れるようにする
    c = conn.cursor()
    # SQL文 IDを取得してくる、条件に名前とパスワードを用いる
    c.execute("insert into users values(null,?,?,?)", (age, sx_code, comment))
    conn.commit()
    # 接続終了
    c.close()
    return render_template("edit.html")


# # @app.route("/")
# # def helloworld():
# #     return "Hello World!"


# @app.route("/")
# def helloworld():
#     return render_template("base.html")


# @app.route("/name/<name>")
# def greet(name):
#     return name + "さん、こんにちは"


# @app.route("/template")
# def template():
#     py_name = "すなぶん"
#     return render_template("index.html", name=py_name)


# @app.route("/sunabaco")
# def sunabaco():
#     return render_template("sunabaco.html")


# @app.route("/mypage")
# def mypage():
#     return render_template("mypage.html")


# @app.route("/address")
# def address():
#     name = "koudai"
#     age = 25
#     address = "uki"
#     return render_template("address.html", name=name, age=age, address=address)


# @app.route("/weather")
# def weather():
#     now_weather = "晴れ"
#     return render_template("weather.html", now_weather=now_weather)


# @app.route("/dbtest")
# def dbtest():
#     # dbtest.dbに接続
#     conn = sqlite3.connect("dbtest.db")
#     # データベースの中身が見れるようにする
#     c = conn.cursor()
#     # SQL文を実行する
#     c.execute("select name,age,address from users where id =1")
#     # 取ってきたレコードを格納する
#     user_info = c.fetchone()
#     # 接続終了
#     c.close()
#     # 取ってきたデータを確認
#     print(user_info)

#     return render_template("dbtest.html", user_info=user_info)


# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'), 404


# @app.route("/add", methods=["GET"])
# def add_get():
#     return render_template("add.html")


# @app.route("/add", methods=["POST"])
# def add_post():
#     # htmlからデータを取ってくる
#     task = request.form.get("task")
#     # dbtest.dbに接続
#     conn = sqlite3.connect("dbtest.db")
#     # データベースの中身が見れるようにする
#     c = conn.cursor()
#     # SQL文を実行する
#     c.execute("insert into task values(null,?)", (task,))
#     # 変更を加える
#     conn.commit()
#     # 取ってきたレコードを格納する
#     user_info = c.fetchone()
#     # 接続終了
#     c.close()

#     # return task_list()
#     return redirect("/list")


# @app.route("/list")
# def task_list():
#     # htmlからデータを取ってくる
#     task = request.form.get("task")
#     # dbtest.dbに接続
#     conn = sqlite3.connect("dbtest.db")
#     # データベースの中身が見れるようにする
#     c = conn.cursor()
#     # SQL文を実行する
#     c.execute("select * from task")
#     # 取ってきたレコードを格納する
#     task_list = []
#     for row in c.fetchall():
#         task_list.append({"id": row[0], "task": row[1]})

#     # 接続終了
#     c.close()
#     print(task_list)
#     return render_template("task_list.html", task_list=task_list)


# @app.route("/edit/<int:id>")
# def edit(id):
#     # dbtest.dbに接続
#     conn = sqlite3.connect("dbtest.db")
#     # データベースの中身が見れるようにする
#     c = conn.cursor()
#     # SQL文を実行する
#     c.execute("select task from task where id = ?", (id,))
#     # 取ってきたレコードを格納する
#     task = c.fetchone()
#     # print(task)
#     # task = task[0]
#     # 接続終了
#     c.close()

#     # タスクが存在したらページ遷移、存在しなかったらテキスト表示
#     if task is not None:
#         # タスクがタプル型で入ってくるので型変換をする
#         task = task[0]
#     else:
#         return "タスクがないよ"

#     item = {"id": id, "task": task}

#     return render_template("edit.html", task=item)


# @app.route("/edit", methods=["POST"])
# def edit_post():
#     # 入力フォームから値を取得
#     item_id = request.form.get("task_id")
#     task = request.form.get("task")
#     # dbtest.dbに接続
#     conn = sqlite3.connect("dbtest.db")
#     # データベースの中身が見れるようにする
#     c = conn.cursor()
#     # SQL文を実行する
#     c.execute("update task set task = ? where id = ?", (task, item_id))
#     # 変更を適用する
#     conn.commit()
#     # 接続終了
#     c.close()

#     return redirect("/list")

#     # 削除機能を作ろう　ルーティング作成　db接続　SQL文を書く　変更適用　リターン文でリストへ


# @app.route("/del/<int:id>")
# def delete(id):
#     # dbtest.dbに接続
#     conn = sqlite3.connect("dbtest.db")
#     # データベースの中身が見れるようにする
#     c = conn.cursor()
#     # SQL文を実行する
#     c.execute("delete from task where id = ?", (id,))
#     # 変更を適用する
#     conn.commit()
#     # 接続終了
#     c.close()

#     return redirect("/list")


# # 登録機能
# @app.route("/regist", methods=["GET"])
# def regist_get():
#     return render_template("regist.html")


# @app.route("/regist", methods=["POST"])
# def regist_post():
#     # 入力フォームから値を取得
#     name = request.form.get("name")
#     password = request.form.get("password")
#     # db接続
#     conn = sqlite3.connect("dbtest.db")
#     # データベースの中身が見れるようにする
#     c = conn.cursor()
#     # SQL文を実行する
#     c.execute("insert into user values(null,?,?)", (name, password))
#     # 変更を適用する
#     conn.commit()
#     # 接続終了
#     c.close()
#     return "登録完了"


# # ログイン
# # このルーティングに接続したらlogin.htmlが開く様にする
# @app.route("/login", methods=["GET"])
# def login_get():
#     return render_template("login.html")


# @app.route("/login", methods=["POST"])
# def login_post():
#     # 入力フォームから値を取得
#     name = request.form.get("name")
#     password = request.form.get("password")
#     # DB接続する
#     conn = sqlite3.connect("dbtest.db")
#     # データベースの中身が見れるようにする
#     c = conn.cursor()
#     # SQL文 IDを取得してくる、条件に名前とパスワードを用いる
#     c.execute("select id from user where name = ? and password = ?",
#               (name, password))
#     user_id = c.fetchone()
#     # IDが取得できているのかを確認
#     print(user_id)
#     # 接続終了
#     c.close()

#     if user_id is None:
#         return redirect("/login")
#     else:
#         return redirect("/list")
#     # ログイン完了と表示
#     # return "ログイン完了"


if __name__ == "__main__":
    # Flaskの開発用サーバーを使ってアプリを実行
    app.run(debug=True)

# debug=True 開発サーバー
