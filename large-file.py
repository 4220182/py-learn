"""
一个几十G的文件想用Python解决方案，

方法一：利用awk对文件进行“模数切割”，Mod的不同余数分别对应一个处理线程。

targetFile=xxx
threadNum=5    # 设定五个线程
for((i=0; i<threadNum; i++))
do
    awk 'NR%n==t {print $0}' n=$threadNum t=$i $targetFile | python doTask.py &
done

方法二：多线程处理
"""