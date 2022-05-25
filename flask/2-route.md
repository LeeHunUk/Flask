# Flask_Route 시작하기

> 기본값은 string을 반환합니다.   
> 자세한 사항은 아래 사이트를 참고하시기 바랍니다.   
 * https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application

```python
from flask import jsonify, redirect, url_for
from markupsafe import escape

@app.route('/test/name/<name>')
def name(name):
    return f'Name is {name}, {escape(type(name))}'

@app.route('/test/id/<int:id>')
def id(id):
    return 'Id: %d' % id

@app.route('/test/path/<path:subpath>')
def path(subpath):
    return subpath

@app.route('/test/json')
def json():
    return jsonify({'hello': 'world'})

@app.route('/test/redirect/<path:subpath>')
def redirect_url(subpath):
    return redirect(subpath)

@app.route('/test/urlfor/<path:subpath>')
def urlfor(subpath):
    return redirect(url_for('path', subpath=subpath))
```

## 2. Blueprint

```python
from flask import Blueprint, render_template

NAME = "base"
bp = Blueprint(NAME, __name__)


@bp.route("/")
def index():
    
    return render_template("index.html")
```
```python
# __init__.py

""" Routes Init """
from project.routes import base_route

app.register_blueprint(base_route.bp)
```