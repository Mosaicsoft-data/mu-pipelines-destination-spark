from typing import TypedDict

from pyspark.sql import SparkSession

spark: SparkSession = SparkSession.Builder().getOrCreate()


class MUPipelinesSparkContext(TypedDict):
    spark: SparkSession
