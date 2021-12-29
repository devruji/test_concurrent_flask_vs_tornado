import tornado.ioloop
import tornado.web
from tornado import gen
from time import sleep
from datetime import datetime
from tornado.ioloop import IOLoop, PeriodicCallback

loop = IOLoop.current()

class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        await gen.sleep(1)
        self.write('Hello, world')

def background_task():
    print(datetime.now())

if __name__ == '__main__':
    application = tornado.web.Application(
        [
            (r'/', MainHandler),
        ]
    )
    application.listen(8888)
    task = PeriodicCallback(background_task, 1000)
    task.start()
    loop.start()