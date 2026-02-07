import time

from pyspark.sql import functions as F
from pyspark.sql import SparkSession
spark_conn = SparkSession.builder.appName("Pyspark demo") \
    .master("local[*]").getOrCreate()

df_spark = spark_conn.read.csv("Data/emp.csv",header=True)
time.sleep(10)
#df_spark.printSchema()
# get me row nimber 10 to 20
df_spark.limit(20).subtract(df_spark.limit(10)).show()
# f1.head(20).tail(10)

time.sleep(60)







