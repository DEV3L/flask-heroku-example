from flask import render_template

from app import app

@app.route('/index1')
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

@app.route('/index2')
def index2():
    adventurer = {'hat': 'fedora',
                  'name': 'DEV3L'}

    games = [1,2,3,4,5]
    return render_template('index.html',
                           # parameters sent to template
                           title='', adventurer=adventurer, games=games)


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