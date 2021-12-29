from flask import Flask
from time import sleep

app = Flask(__name__)

@app.route('/')
def hello_world() -> str:
    sleep(1)
    return '<p>Hello, World!</p>'

if __name__ == '__main__':
    # Default : threaded = True
    app.run(threaded=True, debug=True)
    # app.run(threaded=False, debug=True)

    # then typing "ab -n 10 -c 10 http://localhost:5000/"

# ------------------- Result -------------------

# This is ApacheBench, Version 2.3 <$Revision: 1879490 $>
# Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
# Licensed to The Apache Software Foundation, http://www.apache.org/

# Benchmarking localhost (be patient).....done


# Server Software:        Werkzeug/2.0.2
# Server Hostname:        localhost
# Server Port:            5000

# Document Path:          /
# Document Length:        20 bytes

# Concurrency Level:      10
# Time taken for tests:   4.040 seconds
# Complete requests:      10
# Failed requests:        0
# Total transferred:      1740 bytes
# HTML transferred:       200 bytes
# Requests per second:    2.48 [#/sec] (mean)
# Time per request:       4039.894 [ms] (mean)
# Time per request:       403.989 [ms] (mean, across all concurrent requests)
# Transfer rate:          0.42 [Kbytes/sec] received

# Connection Times (ms)
#               min  mean[+/-sd] median   max
# Connect:        0    0   0.5      1       1
# Processing:  1006 1014   3.1   1015    1017
# Waiting:     1005 1013   3.7   1014    1016
# Total:       1006 1015   3.3   1016    1018
# WARNING: The median and mean for the initial connection time are not within a normal deviation
#         These results are probably not that reliable.

# Percentage of the requests served within a certain time (ms)
#   50%   1016
#   66%   1016
#   75%   1016
#   80%   1016
#   90%   1018
#   95%   1018
#   98%   1018
#   99%   1018
#  100%   1018 (longest request)