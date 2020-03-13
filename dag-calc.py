from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("My App")

sc = SparkContext(conf=conf)
def dag_calc(sc):
    '''构建DAG(有向无环图)调度流程
          ---> b --->
    a--->|          |---> d
          ---> c --->
       输出结果：
       [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    '''
    rdd = sc.parallelize(list(range(10)))
    a = rdd.map(lambda x: x * 2)
    b = a.map(lambda x: x + 1)
    c = a.map(lambda x: x / 2)
    d = b.union(c)
    print(d.collect())

dag_calc(sc)

