# Import necessary libraries
from pyspark.sql import SparkSession

import pandas as pd
file = pd.read_csv("FuzzyPanDataset_orig.csv")



# initialize spark session
spark = SparkSession.builder \
    .appName("") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df= spark.read.option(
  'header', 'true').csv("FuzzyPanDataset_orig.csv")

print(df.show())

