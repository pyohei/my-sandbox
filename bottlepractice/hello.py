#!/usr/local/bin/python
#-*- coding: utf-8 -*-
# Created: 2014-08-03

from bottle import route, run, template, request, get, post, error, response

@route('/helloWorld/<name>')
def hello(name):
    a = fetchComment()
    b = """
        <h1>Hello World!</h1><button>test</button>
        % if name == 'test':
            <p>test</p>
        % end
        構文のテスト
        """
    return template(b, name = name)

def fetchComment():
    return "aaaa"

@route('/')
def init_page():
    return "not found!!<br>Go to http://localhost:8080/hello/test"

@route('/forum')
def display_forum():
    forum_id = request.query.id
    page = request.query.page or '1'
    return template('Forum ID: {{id}} (page {{page}})', id=forum_id, page=page)

@route('/', method='POST')
@route('/hello/<name>')
def greet(name):
    source = '''
        <html><head><title>test</title></head>
          <body><h1>時間</h1><br> {{nowTime}} <br> {{name}}
            <form action="/" method="post">
              文字<input name="test_word" type="text" />
              <input value="comment" type="submit" />
            </form>
            {{comment}}
          </body>
        </html>
    '''
    m = request.forms.get("test_word")
    if not m:
        m = ""
    import datetime
    nowTime = datetime.datetime.now()
    #return template('Hello {{name}}, how are you?', name=name)
    return template(source, nowTime=nowTime, name=name,
        comment = m)

@route('/object/<id:int>')
def callback(id):
    return "ok"
    assert isinstance(id, int)

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login') # or @route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"

def check_login(u, p):
    return u == "mukai"

@route('/tpl')
def tpl_output():
    base_dict = {"test":"TEST","テスト":"てすと"}
    response.set_cookie('bottle_cookie', 'hello_world')
    return template('/Users/mukaishohei/programing/bottle/base', title='test', base=base_dict)

@route('/income')
def display_income():
    from datetime import datetime
    today = datetime.today()
    source = ["基本給", "残業代", "手当"]
    return template('./income',incomes=source, today=today)

@error(404)
def error404(error):
    return "ページがないよー"

run(host='localhost', port=8080, debug=True)
