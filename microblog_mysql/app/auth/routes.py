from flask import render_template, flash, redirect, url_for, request
from werkzeug.urls import url_parse
from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
from app.auth.email import send_password_reset_email
from flask_login import login_required, current_user, login_user, logout_user
from app.models import User, Post
from datetime import datetime

from flask_babel import get_locale
from guess_language import guess_language

from flask import jsonify


# 로그인 페이지
@bp.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated: # 이미 로그인 된 경우
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit(): # 로그인 버튼을 눌른상황일 경우
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username of password (유저 id 혹은 pw가 잘못되었습니다)')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        # 리다이렉팅 - /를 해석못하는 문제가 있어서 강제로 /제거함
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(url_for(next_page[1:])) # error : /index로 입력되는데 /를 해석못하는 문제가 있음. 강제로 /제거함
    return render_template('auth/login.html', title='Sign In', form=form) #지정된 form을 받는다.

#로그아웃하기
@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))

# 회원가입 페이지
@bp.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(_('Congratulations! You are now registerd user! Log in your account!'))
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title=_('Register'), form=form)

#비밀번호 재설정
@bp.route('/reset_password_request', methods=['GET','POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password_request.html', title='Reset Password', form=form)

@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('main.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form)


# 포스트 Ajax번역
@bp.route('/translate', methods=['POST'])
@login_required
def translate_text():
    return jsonify({'text': translate(request.form['text'],
                                      request.form['source_language'],
                                      request.form['dest_language'])})
# 구글로그인관련
from app import oauth2
@bp.route('/needs_credentials')
@oauth2.required
def needs_credentials():
    # http is authorized with the user's credentials and can be used
    # to make http calls.
    http = oauth2.http()

    # Or, you can access the credentials directly
    # credentials = oauth2.credentials
# 구글로그인정보
@bp.route('/info')
@oauth2.required
def info():
    return "Hello, {} ({})".format(oauth2.email, oauth2.user_id)
