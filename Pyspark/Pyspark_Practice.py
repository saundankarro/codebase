import pyspark
from pyspark.sql import SparkSession, SQLContext
import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable


spark = SparkSession.builder.appName('PysparkPractice').getOrCreate()

# print(spark)

df_pyspark=spark.read.option('header','true').csv('test1.csv', inferSchema=True)


# print(df_pyspark)
df_pyspark.show()

df_pyspark.printSchema()