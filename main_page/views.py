from flask import render_template, abort, request, jsonify
from app import app, db
from . import main
from .models import SumDb
from .forms import SumForm


@main.route('/', methods=['POST', 'GET'])
def index():
    form = SumForm()
    if request.method == 'POST':
        if form.validate_on_submit:
            answer = float(form.a.data) + float(form.b.data)
            newdata = SumDb()
            newdata.first_number = form.a.data
            newdata.second_number = form.b.data
            newdata.sum = answer
            db.session.add(newdata)
            db.session.commit()
            return render_template('main.html', form=form, answer=answer)
    return render_template('main.html', form=form)


@main.route('/inputing')
def inputing():
    form = SumForm()
    return render_template('main_get.html', form=form)


@main.route('/sum')
def sum():
    print(request.url)
    answer = float(request.args.get('a')) + float(request.args.get('b'))
    newdata = SumDb()
    newdata.first_number = request.args.get('a')
    newdata.second_number = request.args.get('b')
    newdata.sum = answer
    db.session.add(newdata)
    db.session.commit()
    return f'{answer}'
