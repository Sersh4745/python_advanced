from flask import Flask, render_template, make_response, request, session

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'this is a very very secret key'


@app.route('/')
def home():
    if request.cookies.get('name'):
        return f'<h1>Home Page. Hello, {request.cookies.get("name")}</h1>'
    return 'Home Page'


@app.route('/cookie/')
def cookie():
    res = make_response(f'<h1>Home Cookie</h1>')
    res.set_cookie('name', 'Ivan', max_age=60 * 2)
    return res


@app.route('/delete-cookie/')
def delete_cookie():
    res = make_response(f'<h1>Cookie deleted</h1>')
    res.set_cookie('name', '', max_age=0)
    return res


@app.route('/visit/')
def visits():
    if 'visit' in session:
        session['visit'] = session.get('visit') + 1
    else:
        session['visit'] = 1
    return f'Count visits = {session.get("visit")}'


@app.route('/delete-visit/')
def delete_visits():
    session.pop('visit', 'None')
    return 'Visits deleted'


if __name__ == '__main__':
    app.run()
