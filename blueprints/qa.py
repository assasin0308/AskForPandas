from flask import Blueprint,render_template,request,g,redirect,url_for
from .forms import QuestionForm
from models import QuestionModel
from exts import db




bp = Blueprint("qa",__name__,url_prefix="/")



@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/qa/publish",methods = ['GET','POST'])
def publish_question():
    if request.method == 'GET':
        return render_template('public_question.html')
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(title=title,content=content,author=g.user)
            db.session.add(question)
            db.session.commit()
            # TODO 跳转到这篇问答详情页

            return redirect("/")
        else:
            print(form.errors)
            return redirect(url_for("qa.publish_question"))

