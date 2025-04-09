import os
os.environ["HADOOP_HOME"] = "C:\\hadoop"  # Set HADOOP_HOME for Windows

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as sum_
import pandas as pd

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Retail Sales Trend Analyzer") \
    .master("local[*]") \
    .getOrCreate()

# Read CSV file
df = spark.read.csv("retail_sales_data.csv", header=True, inferSchema=True)
print("Loaded data:")
df.show(5)

# Group by product_id and date, calculate total sales
sales_by_product_date = df.groupBy("product_id", "date") \
                          .agg(sum_("sales_amount").alias("total_sales")) \
                          .orderBy("date")
print("Sales by product and date:")
sales_by_product_date.show(5)

# Find top 5 products by total sales
top_products = df.groupBy("product_id") \
                 .agg(sum_("sales_amount").alias("total_sales")) \
                 .orderBy(col("total_sales").desc()) \
                 .limit(5)
print("Top 5 products:")
top_products.show()

# Convert to Pandas DataFrame and save as CSV
top_products_pd = top_products.toPandas()
top_products_pd.to_csv("C:\\Users\\Lihle\\Downloads\\GithubProjects\\Sales-Trend-Analyzer\\top_products.csv", index=False)
print("Saved results to C:\\Users\\Lihle\\Downloads\\GithubProjects\\Sales-Trend-Analyzer\\top_products.csv")

# Stop SparkSession
spark.stop()