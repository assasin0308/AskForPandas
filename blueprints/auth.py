import json

from flask import Blueprint,render_template,jsonify,Response
from flask import request
from exts import mail,db
from flask_mail import Message
import string
import random
from models import EmailCaptchaModel

# /auth
bp = Blueprint("auth",__name__,url_prefix="/auth")

@bp.route("/login")
def login():
    return "/"


@bp.route("/register",methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        # 验证用户提交的邮箱和验证码是否对应且正确
        # 表单验证：flask-wtf: wtforms
        pass





@bp.route('/captcha/email')
def get_email_captcha():
    email = request.args.get('email')
    print('接收到的邮箱账号: ' + email)
    captcha = random.sample(string.digits*6,6)
    captcha = "".join(captcha)
    print('发送的邮箱验证码: ' + captcha)
    # message = Message(subject="熊猫问答社区", recipients=[email], body=f"您好! 您的验证码是: {captcha}")
    message = Message(subject="熊猫问答社区", recipients=[email])
    body = f"您好！欢迎进入熊猫问答社区，您的验证码是：  "
    message.html = render_template('captcha_email.html',subject='熊猫问答社区',body=body,captcha=captcha)
    mail.send(message)

    # 存储邮箱验证码
    email_captcha = EmailCaptchaModel(email=email,captcha=captcha)
    db.session.add(email_captcha)
    db.session.commit()
    data = {'email': email,'captcha': captcha}
    return jsonify({"code":200,"msg":"success","data":data})


@bp.route('/mail/test')
def mail_test():
    message = Message(subject="邮箱测试",recipients=["839203143@qq.com"],body="这是一条测试邮件")
    print(mail)
    mail.send(message)
    return "邮件发送成功!"





