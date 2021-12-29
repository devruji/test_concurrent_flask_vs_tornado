import tornado.ioloop
import tornado.web
import time

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        time.sleep(1)
        self.write('Hello, World!')

def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


    # then typing "ab -n 10 -c 10 http://localhost:5000/"


# ------------------- Result -------------------

# This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
# Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/        
# Licensed to The Apache Software Foundation, http://www.apache.org/

# Benchmarking localhost (be patient).....done


# Server Software:        TornadoServer/6.1
# Server Hostname:        localhost
# Server Port:            8888

# Document Path:          /
# Document Length:        13 bytes

# Concurrency Level:      10
# Time taken for tests:   0.008 seconds
# Complete requests:      10
# Failed requests:        0
# Total transferred:      2060 bytes
# HTML transferred:       130 bytes
# Requests per second:    1250.00 [#/sec] (mean)
# Time per request:       8.000 [ms] (mean)
# Time per request:       0.800 [ms] (mean, across all concurrent requests)       
# Transfer rate:          251.46 [Kbytes/sec] received

# Connection Times (ms)
#               min  mean[+/-sd] median   max
# Connect:        0    0   0.4      0       1
# Processing:     2    3   1.1      4       5
# Waiting:        1    3   1.2      4       4
# Total:          2    3   1.0      4       5
# WARNING: The median and mean for the total time are not within a normal deviation
#         These results are probably not that reliable.

# Percentage of the requests served within a certain time (ms)
#   50%      4
#   66%      4
#   75%      4
#   80%      4
#   90%      5
#   95%      5
#   98%      5
#   99%      5
#  100%      5 (longest request)