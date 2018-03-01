# from flask import Flask
#
# app = Flask(__name__)
#
# from app import routes


from flask import Flask
from flask_runner import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return 'hello world!!!'


if __name__ == '__main__':
    manager.run()
