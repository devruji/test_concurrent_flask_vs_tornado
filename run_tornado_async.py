
import tornado.ioloop
import tornado.web

from tornado import gen

class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        await gen.sleep(1)
        self.write('Hello, world')

if __name__ == '__main__':
    application = tornado.web.Application(
        [
            (r'/', MainHandler),
        ]
    )
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()


# ------------------- Result -------------------

# This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
# Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/        
# Licensed to The Apache Software Foundation, http://www.apache.org/

# Benchmarking localhost (be patient).....done


# Server Software:        TornadoServer/6.1
# Server Hostname:        localhost
# Server Port:            8888

# Document Path:          /
# Document Length:        12 bytes

# Concurrency Level:      10
# Time taken for tests:   2.015 seconds
# Complete requests:      10
# Failed requests:        0
# Total transferred:      2050 bytes
# HTML transferred:       120 bytes
# Requests per second:    4.96 [#/sec] (mean)
# Time per request:       2014.631 [ms] (mean)
# Time per request:       201.463 [ms] (mean, across all concurrent requests)     
# Transfer rate:          0.99 [Kbytes/sec] received

# Connection Times (ms)
#               min  mean[+/-sd] median   max
# Connect:        0    0   0.0      0       0
# Processing:  1003 1008   2.6   1008    1011
# Waiting:     1002 1008   2.9   1008    1011
# Total:       1003 1008   2.6   1008    1011

# Percentage of the requests served within a certain time (ms)
#   50%   1008
#   66%   1009
#   75%   1011
#   80%   1011
#   90%   1011
#   95%   1011
#   98%   1011
#   99%   1011
#  100%   1011 (longest request)