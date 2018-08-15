import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

# 연결설정하기
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE.URL') or \
    #     'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = 'mysql://master:password0000@rds-mysql.cmbehnf2vcrh.ap-northeast-2.rds.amazonaws.com/app'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    print(' * SQL Type : ',SQLALCHEMY_DATABASE_URI)
    # 관리자 이메일 설정
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['brightscannon@gmail.com']

    POSTS_PER_PAGE = 10

    LANGUAGES = ['en','es']

    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    print("config info : ",ELASTICSEARCH_URL)
