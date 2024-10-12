
SECRET_KEY = "YXNrZm9ycGFuZGFz"

# 数据库的配置信息
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'askforpandas'
USERNAME = 'root'
PASSWORD = 'a12345'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


# 邮箱配置
MAIL_SERVER = "smtp.sina.com"
# MAIL_USE_SSL = True
MAIL_USE_SSL = False
MAIL_PORT = 587
MAIL_USERNAME = "assasin0308@sina.com"
MAIL_PASSWORD = "ad43761871818cfb"
MAIL_DEFAULT_SENDER = "assasin0308@sina.com"