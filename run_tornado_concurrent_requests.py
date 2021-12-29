
import ssl
import tornado.ioloop
import tornado.web

from tornado import gen

import aiohttp
import asyncio

async def mock_api_request(num):
    await gen.sleep(1)
    return num

class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False)
        ) as session:
            tasks = []
            for i in range(5):
                task = asyncio.ensure_future(mock_api_request(i))
                tasks.append(task)
            responses = await asyncio.gather(*tasks)
            print(responses)

if __name__ == '__main__':
    application = tornado.web.Application(
        [
            (r'/', MainHandler),
        ]
    )
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()