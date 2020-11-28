from flask import Flask, render_template, flash, redirect
from flask_script import Manager

from src.forms import LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'any secret string'


@app.route('/hello')
def index1():
    user = {'username': 'DEV3L'}
    return '''
    <html>
        <head>
            <title>Home Page - Microblog</title>
        </head>
        <body>
            <h1>Hello, ''' + user['username'] + '''!</h1>
        </body>
    </html>'''


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Justin'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]

    print('name = ' + posts[0]['author']['username'])
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


manager = Manager(app)

if __name__ == '__main__':
    manager.run()
