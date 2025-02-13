from pyspark.sql import SparkSession
from pyspark.sql.functions import month
from pyspark.sql.functions import max as max_f
from pyspark.sql.functions import min as min_f
from pyspark.sql.functions import avg as avg_f
import time

spark = (SparkSession
        .builder
        .appName('Bauyr aizere azim')
        .config("spark.hadoop.fs.defaultFS", "hdfs://10.58.94.45:9000")
        .getOrCreate()
)
sc = spark.sparkContext

hdfs_path = "hdfs://10.58.94.45:9000/bauyr/dataset.csv"
df =  spark.read.csv(hdfs_path, header=True,  inferSchema = True, sep=',')
df.show()
df.printSchema()

temperature_max = df.groupBy(month('Date_time').alias('month')).agg(max_f('Temperature_C').alias('max_temp'))
temperature_min = df.groupBy(month('Date_time').alias('month')).agg(min_f('Temperature_C').alias('min_temp'))
temperature_avg = df.groupBy(month('Date_time').alias('month')).agg(avg_f('Temperature_C').alias('Avg'))

temperature_avg.show()
temperature_max.show()
temperature_min.show()

