# Import necessary libraries
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("YourApp") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

import pandas as pd
file = pd.read_csv("FuzzyPanDataset_orig.csv")
print(file.head())

# Drop any rows with missing values
df = df.dropna()

# # Feature Engineering: Convert categorical variables to numerical using StringIndexer
# indexers = [StringIndexer(inputCol=column, outputCol=column+"_index").fit(df) for column in ["AppName", "KarzaName", "PanCard", "ApiProvider"]]
# pipeline = Pipeline(stages=indexers)
# df_indexed = pipeline.fit(df).transform(df)

# # Assemble features
# assembler = VectorAssembler(inputCols=["AppName_index", "KarzaName_index", "Score", "PanCard_index", "ApiProvider_index"], outputCol="features")
# output = assembler.transform(df_indexed)

# # Split the data into training and testing sets
# train_data, test_data = output.randomSplit([0.7, 0.3], seed=42)

# # Train a logistic regression model
# lr = LogisticRegression(featuresCol='features', labelCol='Result', maxIter=10)
# lr_model = lr.fit(train_data)

# # Evaluate the model
# predictions = lr_model.transform(test_data)
# evaluator = BinaryClassificationEvaluator(labelCol="Result")
# accuracy = evaluator.evaluate(predictions)

# print("Accuracy:", accuracy)

# # Save the model
# lr_model.save("dbfs:/path/to/save/model")