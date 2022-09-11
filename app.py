#!python
from flask import Flask, request, make_response
from flask import render_template
import pyqrcode
from pynput.keyboard import Key, Controller

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
#
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(128))


kb = Controller()


def press_key(code):
    key = Key.media_volume_up
    if code == "up":
        key = Key.up
    elif code == "down":
        key = Key.down
    elif code == "left":
        key = Key.left
    elif code == "right":
        key = Key.right
    elif code == "enter":
        key = Key.enter
    elif code == "cmd":
        key = Key.cmd
    elif code == "escape":
        key = Key.esc
    elif code == "space":
        key = Key.space
    if key is None:
        return

    kb.press(key)
    kb.release(key)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/click', methods=["POST"])
def click():
    code = request.get_json()['code']
    press_key(code)
    return ""


if __name__ == '__main__':
    import socket


    def get_ip_address():
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]


    port = 9090
    url = f"http://{get_ip_address()}:{port}"
    print(pyqrcode.create(url).terminal())
    app.run("0.0.0.0", port=port, )
