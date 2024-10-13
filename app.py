# 熊猫解惑 Ask For Pandas
from flask import Flask,session,g
import config
from exts import db
from exts import mail
from models import UserModel
from blueprints.qa import bp as qa_bp
from blueprints.auth import bp as auth_bp
from flask_migrate import Migrate



app = Flask(__name__)

#导入配置
app.config.from_object(config)

db.init_app(app)
mail.init_app(app)

# 数据库迁移
migrate = Migrate(app,db)

#注册蓝图
app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)


# before_request/before_first_request/after_request
# hook 钩子函数的使用

@app.before_request
def app_before_request():
    user_id = session.get("user_id")
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g,"user",user)
    else:
        setattr(g, "user", None)

@app.context_processor
def app_context_processor():
    return {"user": g.user}


if __name__ == '__main__':
    # 路由列表
    print(app.url_map)
    app.run(host='0.0.0.0',port=5000,debug=True)



