import tornado.ioloop
import tornado.web

from tornado import gen
from tornado.ioloop import IOLoop, PeriodicCallback

from time import sleep
from datetime import datetime

loop = IOLoop.current()

class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        await gen.sleep(1)
        self.write('Hello, world')

async def background_task():
    while True:
        print(datetime.now())
        await gen.sleep(1)

if __name__ == '__main__':
    application = tornado.web.Application(
        [
            (r'/', MainHandler),
        ]
    )
    application.listen(8888)
    loop.spawn_callback(background_task)
    loop.start()