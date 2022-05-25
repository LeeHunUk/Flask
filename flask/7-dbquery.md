# Flask SQlAlchemy Query

> 아래의 공식문서를 참고해주세요.
 * https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/

```sh
# db 내용 추가
from yourapp import User
>>> me = User('admin', 'admin@example.com')
>>> db.session.add(me)
>>> db.session.commit()

# id 확인
>>> me.id

# 기록 삭제
>>> db.session.delete(me)
>>> db.session.commit()

# 이름으로 검색
>>> peter = User.query.filter_by(username='peter').first()
>>> peter.id
2
>>> peter.email
```
