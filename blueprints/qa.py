from flask import Blueprint,render_template,request,g,redirect,url_for
from .forms import QuestionForm,AnswerForm
from models import QuestionModel,AnswerModel
from exts import db
from decorators import login_required





bp = Blueprint("qa",__name__,url_prefix="/")


@bp.route("/")
def index():
    questions = QuestionModel.query.order_by(QuestionModel.create_time.desc()).all()
    return render_template("index.html",questions=questions)

@bp.route("/qa/publish",methods = ['GET','POST'])
@login_required
def publish_question():
    # 判断登录状态 -> 登录装饰器
    # if not g.user:
    #     return redirect(url_for("auth.login"))


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



@bp.route("/qa/detail/<qa_id>")
def question_detail(qa_id):
    question = QuestionModel.query.get(qa_id)
    return render_template("detail.html",question=question)


# @bp.route("/answer/publish",methods=['POST'])
@bp.post("/answer/publish") # 直接使用post路由
@login_required
def publish_answer():
    form = AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        question_id = form.question_id.data
        answer = AnswerModel(content=content,question_id=question_id,author_id=g.user.id)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for("qa.question_detail",qa_id=question_id))

    else:
        print(form.errors)
        return  redirect(url_for("qa.question_detail",qa_id=request.form.get("question_id")))



# 关键字搜索问题标题
@bp.route("/search")
def search():
    q = request.args.get("q")
    questions = QuestionModel.query.filter(QuestionModel.title.contains(q)).all()
    return render_template("index.html",questions=questions)