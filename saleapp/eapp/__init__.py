from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'JSDSSKSKDSK$%%KSFSSKSDFK@#KSKS'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['PAGE_SIZE'] = 4 #Mỗi trang chỉ hiện 8 sản phẩm

db = SQLAlchemy(app=app) # db đại diện cho toàn bộ cơ sở dữ liệu
login = LoginManager(app=app)
