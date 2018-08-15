# 이 문서는 보통 DB의 모델을 구축하는데 쓰인다.

from datetime import datetime
from time import time
import jwt
from app import app, db, login
#패스워드 해싱
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from hashlib import md5


#유저 팔로잉 팔로워용 테이블 설정
followers = db.Table('followers',
    db.Column('follower_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('followed_id', db.Integer, db.ForeignKey('user.id'))
)

# 현재 모델은 SQLite3를 사용하고 있다. 나중에 MySQL로 사용하자
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    # 비밀번호 열에 들어갈 내용
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    #유저용 아이콘 생성
    def avatar(self,size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return "https://www.gravatar.com/avatar/{}?d=identicon&s={}".format(digest, size)

    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    # 유저 팔로잉 팔로워 설정-------------------
    followed = db.relationship(
        'User', secondary=followers,
        primaryjoin=(followers.c.follower_id == id),
        secondaryjoin=(followers.c.followed_id == id),
        backref = db.backref('followers', lazy='dynamic'), lazy='dynamic')
    def follow(self, user):
        if not self.is_following(user):
            self.followed.append(user)
    def unfollow(self, user):
        if self.is_following(user):
            self.followed.remove(user)
    def is_following(self, user):
        return self.followed.filter(
            followers.c.followed_id == user.id).count() > 0
    def followed_posts(self):
        followed = Post.query.join(
            followers, (followers.c.followed_id == Post.user_id)).filter(
                followers.c.follower_id == self.id)
        own = Post.query.filter_by(user_id=self.id)
        return followed.union(own).order_by(Post.timestamp.desc())

    # 유저 비밀번호 재발급용 이메일
    def get_reset_password_token(self, expires_in=600):
        return jwt.encode(
        {'reset_password':self.id, 'exp':time()+expires_in},
        app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

    @staticmethod
    def verity_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'],
                algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    language = db.Column(db.String(5))

    def __repr__(self):
        return '<Post {}>'.format(self.body)


# 유저정보 로더(id값으로)
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
