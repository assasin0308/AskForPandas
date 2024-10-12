# 熊猫解惑 Ask For Pandas
from flask import Flask
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


@app.route('/')
def hello_world():
    return "Hello 熊猫问答!"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)