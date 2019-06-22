"""
输出监控指标

参考：
https://github.com/prometheus/client_python
https://prometheus.io/docs/concepts/metric_types

样例：
https://blog.csdn.net/kozazyh/article/details/93240722

"""

from prometheus_client import start_http_server, Summary, Counter
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
Counter_TIME = Counter('My_Counter','My Counter Desc')

# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request(random.random())
        Counter_TIME.inc()
