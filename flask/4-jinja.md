# Jinja

## 1. 화면 구조
> {{ }}를 사용하여 상속받는 구조로 작성한다.   

```html
<!-- layout.html -->
<!DOCTYPE html>

<html lang="ko">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no, maximum-scale=1" />
        <title>{% block title %}{% endblock %}</title>
        {% block head %}
            <!--APP CSS-->
            <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}" type="text/css"/>
        {% endblock %}
    
    </head>

    <body>
      {% block body %}
      {% endblock %}
    </body>
</html>

<!-- index.html -->
{% extends "/layout.html" %}

{% block title -%}
    Project
{%- endblock %}

{% block head -%}
    {{ super() }}
{%- endblock %}

{% block body -%}
    <h1>Hello My Site!</h1>
{%- endblock %}

```