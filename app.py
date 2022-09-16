#!python
from flask import Flask, request
from flask import render_template
import pyqrcode
from pynput.keyboard import Key, Controller

app = Flask(__name__)
kb = Controller()


def press_key(code):
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
    else:
        return

    kb.press(key)
    kb.release(key)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/click', methods=["POST"])
def click():
    data = request.get_json()
    if data is None:
        return ""
    code = data['code']
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
