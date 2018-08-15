# 입력폼들의 기본 형상 및 작동방법등의 함수를 만들어놓는곳.

from flask_wtf import FlaskForm
from wtforms import * #StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import * #ValidationError, DataRequired, Email, EqualTo
from app.models import User
from flask_babel import lazy_gettext as _l
from flask_babel import _


class LoginForm(FlaskForm):
    username = StringField(_l('Username (사용자 ID)'),validators=[DataRequired()])
    password = PasswordField(_l('Password (비밀번호)'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember Me (아이디 기억)'))
    submit = SubmitField(_l('Sign In (로그인)'))

class RegistrationForm(FlaskForm):
    username = StringField(_l('Username (아이디)'), validators=[DataRequired()])
    email = StringField(_l('Email'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    password2 = PasswordField(_l('Repead Password'), validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField(_l('Register'))

    def validate_username(self, username): # 중복아이디 검사
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise validationError('Please use a different username.')

    def validate_email(self, email): # 중복이메일 검사
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class ResetPasswordRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Request Password Reset')
