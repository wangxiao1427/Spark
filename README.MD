## 在windows安装Spark环境，所需依赖为jdk/Spark/Hadoop

1. 安装jdk，http://www.oracle.com/technetwork/java/javase/downloads/index.html
安装完成后配置环境变量，过程略

2. 安装Scala，http://www.scala-lang.org/
选择windows版本，scala-2.12.3.msi
安装完成之后，先设置环境变量，将scala安装目录的bin目录添加到path系统变量中，然后使用scala命令验证安装结果

3. 安装Spark，http://spark.apache.org/
此处我们选择Spark-2.2.0-bin-hadoop2.7.tgz，解压后将Spark/bin的所在目录添加到path系统变量中，完成之后，此时如果用spark-shell命令验证安装是否成功会报错，
是因为还缺少了hadoop组件

4. 安装Hadoop，https://archive.apache.org/dist/hadoop/common/
选择的hadoop版本需要和第3步的spark匹配，所以此处选择hadoop2.7.0，下载解压后将hadoop/bin目录添加到path系统环境变量中

上述完成之后使用spark-shell命令测试spark/hadoop是否安装成功，过程中可能会遇到的问题：  
* spark-shell命令报空指针问题  
主要是因为Hadoop的bin目录下没有winutils.exe文件的原因造成的。这里的解决办法是：可以去 https://github.com/steveloughran/winutils 选择你安装的Hadoop版本号，然后进入到bin目录下，找到winutils.exe文件，下载方法是点击winutils.exe文件，进入之后在页面的右上方部分有一个Download按钮，点击下载即可
* 出现的ava.net.BindException: Cannot assign requested address: Service 'sparkDriver' failed after 16 retries (starting from 0)!问题  
解决办法：https://blog.csdn.net/chengyuqiang/article/details/69665878 ，
hosts文件中添加 <本机ip> sk1

## 最后如何在python下搭建Spark环境：
1. 添加环境变量  
PATHONPATH=%SPARK_HOME%\python;%SPARK_HOME%\python\lib\py4j-0.10.8.1-src.zip
2. 安装pip install py4j

3. 安装pip install pyspark