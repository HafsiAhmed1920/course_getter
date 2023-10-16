import os
from selenium import webdriver 
from selenium.webdriver.common.by import By
from pyspark.sql import SparkSession
from pyspark.sql.functions import lit, expr
from pyspark.sql.functions import col
from Comma.common import get_course_rate, customize_text as customized, \
      have_multiple_courses as muticourse, split_courses as course_split, \
      remove_lang
from Writer.writer import upload_to_firebase
from firebase_config.fireConf import initialise_firebase

  
def process_toget_data():
    
    spark = SparkSession.builder.appName("hello").getOrCreate()
    driver = webdriver.Chrome()
    driver.get("https://data-flair.training/")
    elements = driver.find_elements(By.XPATH, '//div[@class="course-tile"]/p[1]')

    data = []
    for element in elements:
        data.append(("data flair", element.text))

    df = spark.createDataFrame(data, ["name", "text"])
    df = df.withColumn("rate", get_course_rate(df.text))
    df = df.withColumn("text", customized(df.text))
    df = df.withColumn('courses_count', lit(1))
    df = df.withColumn("courses_count", muticourse(df.text))
    df = df.withColumn("text", course_split(df.text))

    count = df.selectExpr("max(size(text)) as count").first()["count"]
    for i in range(count):
        col_name = f"course{i+1}"
        df = df.withColumn(col_name, expr(f"text[{i}]"))
        df = df.withColumn(col_name, remove_lang(col(col_name)))

    df = df.drop('text')
    df.write.mode('overwrite').parquet(r'C:\Users\ahafsi\project beta\myfiles')

    # New codeww to upload all files in the directory
    initialise_firebase()
    directory_path = r'C:\Users\ahafsi\project beta\myfiles'
    for filename in os.listdir(directory_path):
        # Construct file path
        if filename.endswith('.parquet'):    
            file_path = os.path.join(directory_path, filename)
            upload_to_firebase(file_path)