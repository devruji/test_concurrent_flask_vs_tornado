from flask import Flask
from time import sleep
from threading import Thread
from datetime import datetime

app = Flask(__name__)

def background_task():
    while True:
        print(datetime.now())
        sleep(1)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

if __name__ == '__main__':
    thread = Thread(target=background_task)
    thread.daemon = True
    thread.start()
    app.run()