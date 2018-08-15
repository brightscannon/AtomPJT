from flask import Blueprint

bp = Blueprint('errors',__name__)

# 순환종속을 피하기 위해 아래에 위치시킨다.
from app.errors import handlers
