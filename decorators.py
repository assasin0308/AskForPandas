from functools import wraps
from flask import g,redirect,url_for
def login_required(func):
    # 保留func的信息
    @wraps(func)
    def inner(*args,**kwargs):
        if hasattr(g,"user") and g.user:
            return func(*args,**kwargs)  # ! return
        else:
            return redirect(url_for("auth.login"))


    return inner
