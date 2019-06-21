"""
jmxquery模块，通过JMX轻松运行查询并从Java虚拟机收集指标。

利用jmxquery查询kafka的指标：
安装jmxquery: pip3.6 install jmxquery

参考：https://github.com/dgildeh/JMXQuery

在kafka的启动文件./bin/kafka-server-start 增加JMX环境变量

if [ "x$KAFKA_HEAP_OPTS" = "x" ]; then
    export KAFKA_HEAP_OPTS="-Xmx1G -Xms1G"
    export JMX_PORT="8888"
fi
"""
from jmxquery import JMXConnection, JMXQuery

jmxConnection = JMXConnection("service:jmx:rmi:///jndi/rmi://127.0.0.1:8888/jmxrmi")
jmxQuery = [JMXQuery("*:*")]
metrics = jmxConnection.query(jmxQuery)
for metric in metrics:
    print(f"{metric.to_query_string()} ({metric.value_type}) = {metric.value}")
