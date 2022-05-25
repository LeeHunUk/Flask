# Flask

## 1. Flask란?
> Python 기반 micro 프레임워크

## 2. Coding Convention

> 여러사람이 협업을 해도 모두가 읽기 편한 코드를 작성하기 위한 기본 규칙   
> But Local Rule이 더 중요!!

```
 * 한 줄의 문자열은 79자, Django는 119자 추천
 * DocString은 72자
 * snake_case 사용
 * 모듈 레벨 상수는 모두 대문자
 * ClassName은 Capitalized Word
 * 한 줄로 된, if, try...except, for, while 구문은 사용하지 않는다.
```

## 3. 개발 환경

> 해당 환경은 window의 wsl2를 기반으로 사용되었습니다.
```sh
 # pip 안될 시
 User $ sudo apt-get install python3-pip

 # 가상환경 생성 및 실행
 User $ sudo pip3 install virtualenv virtualenvwrapper
 User $ virtualenv --python=python3 가상환경명
 User $ source 환경명/bin/activate
 (venv) User $ 필요한 모듈 설치
```
