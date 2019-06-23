"""
输出监控指标

参考：
https://github.com/prometheus/client_python
https://prometheus.io/docs/concepts/metric_types

样例：
https://blog.csdn.net/kozazyh/article/details/93240722

使用python内置WSGI server: wsgiref ,考虑性能问题你也可以使用其他WSGI server
"""

from prometheus_client import start_http_server, Summary, Counter
import random
import time
from flask import Flask, jsonify
from wsgiref.simple_server import make_server

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
Counter_TIME = Counter('My_Counter','My Counter Desc')

REQUEST_TIME2 = Summary('request_processing_seconds_2', 'Time spent processing request_2')
Counter_TIME2 = Counter('My_Counter_2','My Counter Desc_2')

app = Flask(__name__)

# Decorate function with metric.
@app.route("/test1")
@REQUEST_TIME.time()
def process_request():
    """A dummy function that takes some time."""
    time.sleep(random.random())
    Counter_TIME.inc()
    return jsonify({"return1": "success OK!"})

@app.route("/test2")
@REQUEST_TIME2.time()
def process_request2():
    """A dummy function that takes some time."""
    time.sleep(random.random())
    Counter_TIME2.inc()
    return jsonify({"return2": "success OK!"})


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.

    httpd = make_server(
        '127.0.0.1', # The host name.
        8001, # A port number where to wait for the request.
        app # Our application object name, in this case a function.
    )
    httpd.serve_forever()