# Flask WTF

## 1. pip install

```sh
# Flask-wtf install
(venv) User $ pip install flask-wtf

# 의존성 기록
(venv) User $ pip freeze > requirements.txt
```

## 2. Flask Config Security 설정

```python
from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

def create_app():
    app.config['SECRET_KEY'] = '원하는 문자열'

    """ === CSRF Init === """
    csrf.init_app(app)
```

## 3. Fields
> 자세한 사항은 아래 사이트를 참고해주세요.   
 * https://wtforms.readthedocs.io/en/2.3.x/
 * https://flask.palletsprojects.com/en/1.1.x/patterns/wtforms/

## 4. werkzeug로 패스워드 암호화

```python
from werkzeug import security

password = security.generate_password_hash(data)
```
