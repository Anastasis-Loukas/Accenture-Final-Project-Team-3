# Databricks notebook source
# MAGIC %md
# MAGIC ## Sales Data Cleaning

# COMMAND ----------

# MAGIC %md
# MAGIC Read the first file to see the structure of the data.

# COMMAND ----------


sales17 = spark.table("accenture_final_project.bronze_layer.sales_2017")
#display(sales17)

# COMMAND ----------

# MAGIC %md
# MAGIC Concatenate the data from all the years into one Dataframe

# COMMAND ----------

sales17 = spark.table("accenture_final_project.bronze_layer.sales_2017")
sales18 = spark.table("accenture_final_project.bronze_layer.sales_2018")
sales19 = spark.table("accenture_final_project.bronze_layer.sales_2019")
sales20 = spark.table("accenture_final_project.bronze_layer.sales_2020")

sales = sales17.unionByName(sales18)\
                .unionByName(sales19)\
                .unionByName(sales20)

display(sales)

# COMMAND ----------

# MAGIC %md
# MAGIC Correcting the names of the columns to not have any trouble

# COMMAND ----------

sales = sales.withColumnRenamed("Unit_Price", "UnitPrice")

# COMMAND ----------

# MAGIC %md
# MAGIC Making the order date column as date type from string.

# COMMAND ----------

from pyspark.sql.functions import regexp_replace, to_date, col

sales = sales.withColumn(
    "OrderDate",
    to_date(regexp_replace("OrderDate", r"^[A-Za-z]+,\s*", ""), "MMMM d, yyyy")
)

# COMMAND ----------

# MAGIC %md
# MAGIC Removing the $ sign from currency columns and making them double type.

# COMMAND ----------

from pyspark.sql.functions import regexp_replace

sales = sales.withColumn("UnitPrice",
        regexp_replace("UnitPrice", "[$,]", "").cast("double")
)

sales = sales.withColumn("Sales",
        regexp_replace("Sales", "[$,]", "").cast("double")
)

sales = sales.withColumn("Cost",
        regexp_replace("Cost", "[$,]", "").cast("double")
)

# COMMAND ----------

# MAGIC %md
# MAGIC Making the other string type columns integer type.

# COMMAND ----------

sales = sales.withColumn("ProductKey", col("ProductKey").cast("int")) \
       .withColumn("ResellerKey", col("ResellerKey").cast("int")) \
       .withColumn("EmployeeKey", col("EmployeeKey").cast("int")) \
       .withColumn("SalesTerritoryKey", col("SalesTerritoryKey").cast("int")) \
       .withColumn("Quantity", col("Quantity").cast("int"))

# COMMAND ----------

# MAGIC %md
# MAGIC Seeing the correct schema

# COMMAND ----------

sales.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC Check for Null Values

# COMMAND ----------

from pyspark.sql.functions import col, sum

sales.select([
    sum(col(c).isNull().cast("int")).alias(c)
    for c in sales.columns
]).show()

# COMMAND ----------

# MAGIC %md
# MAGIC Check fo duplicate rows

# COMMAND ----------

total = sales.count()
unique = sales.distinct().count()

print("Total rows:", total)
print("Unique rows:", unique)
print("Duplicate rows:", total - unique)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Checking for Outliers and Bad data.

# COMMAND ----------

# MAGIC %md
# MAGIC Check for negative values

# COMMAND ----------

sales.filter(
    (col("Quantity") < 0) |
    (col("UnitPrice") < 0) |
    (col("Sales") < 0) |
    (col("Cost") < 0)
    ).show()

# COMMAND ----------

# MAGIC %md
# MAGIC Basic statistics for our data.

# COMMAND ----------

sales.describe().show()

# COMMAND ----------

# MAGIC %md
# MAGIC Check for outliers with Interquartile Range (IQR) Method.

# COMMAND ----------

from pyspark.sql.functions import col

# calculate quartiles
q1, q3 = sales.approxQuantile("Sales", [0.25, 0.75], 0)

iqr = q3 - q1

lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

print("Lower bound:", lower_bound)
print("Upper bound:", upper_bound)

outliers = sales.filter(
    (col("Sales") < lower_bound) | (col("Sales") > upper_bound)
)

outliers.show()

# COMMAND ----------

outliers.count()

# COMMAND ----------

# MAGIC %md
# MAGIC Boxplot to see also about outliers!

# COMMAND ----------

import matplotlib.pyplot as plt

# convert only the needed column to pandas
sales_pd = sales.select("Sales").toPandas()

plt.boxplot(sales_pd["Sales"])
plt.title("Boxplot of Sales")
plt.ylabel("Sales")
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC The numeric columns were inspected for extreme values using summary statistics.
# MAGIC Large values were observed in the Sales column; however, these correspond to high-value product transactions and bulk orders. Since the AdventureWorks dataset represents realistic sales activity, these values were retained.

# COMMAND ----------

# MAGIC %md
# MAGIC The sales data are clean!

# COMMAND ----------

display(sales)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Creating the delta table 

# COMMAND ----------

# DBTITLE 1,Creating Delta table save (fixed syntax)
sales_silver = sales

sales_silver.write \
    .format("delta") \
    .mode("overwrite").option("overwriteSchema", "true") \
    .saveAsTable("accenture_final_project.silver_layer.sales")

# COMMAND ----------

display(spark.table("accenture_final_project.silver_layer.sales"))
