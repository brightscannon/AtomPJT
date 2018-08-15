from flask import *
from passlib.hash import sha256_crypt
import pymysql
# from flask_bootstrap import Bootstrap

app = Flask(__name__)

# Bootstrap(app) #요렇게 해줘야 적용된다.
# @app.route('/bootstrap') #접속할 URL
# def bootstrap():
# 	return render_template('bootstrap.html') #예제 템플릿

@app.route("/")
def index():
    # return "hello world! This is Bright's page."
    return render_template("template.html")


@app.route("/dashboard")
def dashboard():
    # return "hello world! This is Bright's page."
    return render_template("dashboard.html")


# @app.route("/login")
# def login():
#     # return "hello world! This is Bright's page."
#     return render_template("login.html")

# @app.route("/idpwcheck",methods=["POST"])
# def check():
#     conn = pymysql.connect(host='localhost', user='root', password='082308', db='web_data', charset='utf8')
#     curs = conn.cursor()
#     query = "SELECT ID, PW FROM user_info"
#     curs.execute(query)
#     rows = curs.fetchall()
#
#     username = request.form.get("ID")
#     password1 = request.form.get("PW")
#
#     password = sha256_crypt.hash(password1)
#     # password2 = sha256_crypt.hash("password")
#     # print("SQL_DB : ",rows[0][0],rows[0][1])
#     # print("input : ",username,password)
#     # print(password2)
#
#     DBname = rows[0][0]
#     DBPW = sha256_crypt.hash(rows[0][1]) # 원래는 이렇게 하는게 아니고 DB에 이미 암호화가 되어있어야 한다. 지금은 비교해야되기때문에 이렇게 한다
#     verify = sha256_crypt.verify("01234", password)
#
#     conn.close()
#     # return "hello world! This is Bright's page."
#     return render_template("idpwcheck.html", Name = username, PW = password , verify = verify, DBname=DBname, DBPW=DBPW)
#
# # def slack():
# #
# #     if "날씨" in text:
# #         msg = forecast()
# #         send_slack(msg)

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
