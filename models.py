from exts import db
from datetime import datetime
class UserModel(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(120),nullable=False)
    password = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(100),nullable=False,unique=True)
    join_time = db.Column(db.DateTime,default=datetime.now)


class EmailCaptchaModel(db.Model):
    __tablename__ = 'email_captcha'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    captcha = db.Column(db.String(100), nullable=False)
    # is_use = db.Column(db.Boolean,default=False)
