from flask import render_template, request, session, flash, redirect, url_for
from app import db, redis_client
from . import main
from .models import SumDb
from .forms import SumForm
import time

'''constant  variables.(times are in seconds) '''
PERMITED_WRONG_REQUEST = 15

BAN_TIME = 10

PERMITED_REQUEST = 100

PERMITED_TIME = 3600

'''this view is for inputting data in form with using GET method '''


@main.route('/inputting')
def inputting_data():
    form = SumForm()
    return render_template('main_get.html', form=form)


'''this view would add to number with using GET method.'''


@main.route('/sum')
def sum():
    ''' check user connection time. '''
    if session.get("user") is None:
        session["user"] = 1
        start_time = time.time()
        redis_client.mset(
            {"request_no": 0, "start_time": start_time, "wrong_request": 0, "start_ban_time": 0})
    else:
        start_time = redis_client.get("start_time")
        request_no = int(redis_client.get("request_no")) + 1
        redis_client.mset({"request_no": request_no})
        wrong_request = int(redis_client.get("wrong_request"))
        now = time.time()
        duration = now - float(start_time)

        ''' check connection time '''
        if duration > PERMITED_TIME:
            redis_client.mset({"start_time": now})
            session.clear()
            return redirect(url_for('main.sum'))

        ''' check the number of request by user'''
        if request_no > PERMITED_REQUEST:
            start_ban_time = float(redis_client.get("start_ban_time"))
            if start_ban_time == 0:
                start_ban_time = time.time()
                redis_client.mset({'start_ban_time': start_ban_time})
            if time.time() - start_ban_time < BAN_TIME:
                flash(
                    f'you have more than {PERMITED_REQUEST} request in less than one hour.you are ban for {BAN_TIME} seconds. ')
                return render_template('response.html')
            else:
                session.clear()
                return redirect(url_for('main.sum'))

        ''' check the number of wrong request by user. '''
        if wrong_request > PERMITED_WRONG_REQUEST:
            start_ban_time = float(redis_client.get("start_ban_time"))
            if start_ban_time == 0:
                start_ban_time = time.time()
                redis_client.mset({'start_ban_time': start_ban_time})
            if time.time() - start_ban_time < BAN_TIME:
                flash(f'you request more than {PERMITED_WRONG_REQUEST} wrong.you are ban for {BAN_TIME} seconds.')
                return render_template('response.html')
            else:
                session.clear()
                return redirect(url_for('main.sum'))
    try:
        answer = float(request.args.get('a')) + float(request.args.get('b'))
        newdata = SumDb()
        newdata.first_number = request.args.get('a')
        newdata.second_number = request.args.get('b')
        newdata.sum = answer
        db.session.add(newdata)
        db.session.commit()
        flash(f'answer = {answer}')
        return render_template('response.html')
    except (ValueError, TypeError):
        wrong_request = int(redis_client.get("wrong_request")) + 1
        redis_client.mset({"wrong_request": wrong_request})
        flash('wrong input.')
        return render_template('response.html')


'''this view would add to number with using POST method and a form.'''


@main.route('/', methods=['POST', 'GET'])
def index():
    form = SumForm()

    ''' check user connection time. '''
    if session.get("user") is None:
        session["user"] = 1
        start_time = time.time()
        redis_client.mset(
            {"request_no": 0, "start_time": start_time, "wrong_request": 0, "start_ban_time": 0})
    else:
        start_time = redis_client.get("start_time")
        request_no = int(redis_client.get("request_no")) + 1
        redis_client.mset({"request_no": request_no})
        wrong_request = int(redis_client.get("wrong_request"))
        now = time.time()
        duration = now - float(start_time)

        ''' check connection time '''
        if duration > PERMITED_TIME:
            redis_client.mset({"start_time": now})
            session.clear()
            return redirect(url_for('main.index'))

        ''' check the number of request by user'''
        if request_no > PERMITED_REQUEST:
            start_ban_time = float(redis_client.get("start_ban_time"))
            if start_ban_time == 0:
                start_ban_time = time.time()
                redis_client.mset({'start_ban_time': start_ban_time})
            if time.time() - start_ban_time < BAN_TIME:
                flash(
                    f'you have more than {PERMITED_REQUEST} request in less than one hour.you are ban {BAN_TIME} seconds. ')
                return render_template('response.html')
            else:
                session.clear()
                return redirect(url_for('main.index'))

        ''' check the number of wrong request by user. '''
        if wrong_request > PERMITED_WRONG_REQUEST:
            start_ban_time = float(redis_client.get("start_ban_time"))
            if start_ban_time == 0:
                start_ban_time = time.time()
                redis_client.mset({'start_ban_time': start_ban_time})
            if time.time() - start_ban_time < BAN_TIME:
                flash(f'you request more than {PERMITED_WRONG_REQUEST} wrong.you are ban for {BAN_TIME} seconds.')
                return render_template('response.html')
            else:
                session.clear()
                return redirect(url_for('main.index'))

        if request.method == 'POST':
            try:
                answer = float(form.a.data) + float(form.b.data)
                newdata = SumDb()
                newdata.first_number = form.a.data
                newdata.second_number = form.b.data
                newdata.sum = answer
                db.session.add(newdata)
                db.session.commit()
                return render_template('main.html', form=form, answer=answer)
            except (ValueError, TypeError):
                wrong_request = int(redis_client.get("wrong_request")) + 1
                redis_client.mset({"wrong_request": wrong_request})
                flash('wrong input.')

    return render_template('main.html', form=form)
