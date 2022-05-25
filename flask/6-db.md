# Flask SQlAlchemy

## 1. ORM이란?
> ORM은 Object Relational Mapping 즉, 객체-관계 매핑의 줄임말이며,   
> 데이터베이스와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법   
> 자세한 사항은 다음을 참고하여 주세요.
 * https://flask-sqlalchemy.palletsprojects.com/en/2.x/quickstart/
 * https://flask-migrate.readthedocs.io/en/latest/

## 2. pip install

```sh
(venv) User $ pip install flask-migrate
(venv) User $ pip install pymysql

# 의존성 기록
(venv) User $ pip freeze > requirements.txt
```

## 3. __init__.py

```python
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 
        'mysql+pymysql://id:pw@localhost/schema?charset=utf8'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    """ === Database Init === """
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith('sqlite'):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    ...
    return app    
```

## 4. 시작하기

```sh
# 마이그레이션 명령어
(venv) User $ flask db init

# 현재 나의 db 형상이 어디인지
(venv) User $ flask db current

# db migrate
(venv) User $ flask db migrate -m 'Init database'

# 변경사항 적용
(venv) User $ flask db upgrade
```