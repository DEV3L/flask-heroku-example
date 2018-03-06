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

@app.route('/')
@app.route('/index')
def index():
    adventurer = {'hat': 'fedora',
                  'name': 'DEV3L'}

    games = [1,2,3,4,5]
    return render_template('index.html', title='Dashboard', adventurer=adventurer, games=games)
