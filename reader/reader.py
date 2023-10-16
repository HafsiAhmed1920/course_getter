from firebase_admin import storage
from firebase_config.fireConf import initialise_firebase
from pyspark.sql import SparkSession
import tempfile
import os


def reader_bytes(folder='folder85/',):
    bucket = storage.bucket()
    blobs = bucket.list_blobs(prefix=folder)
    data = [blob.download_as_bytes() for blob in blobs]
    return data


def text_to_df(data_list):
    # Initialize a SparkSessions
    spark = SparkSession.builder.getOrCreate()

    # Create an empty list to store the DataFrames
    dfs = []

    # Create a list to store temporary file paths
    temp_files = []

    for data in data_list:
        # Write the bytes data to a temporary Parquet file
        with tempfile.NamedTemporaryFile(suffix=".parquet", delete=False) as f:
            f.write(data)
            temp_path = f.name

        # Read the Parquet file into a DataFrame
        df = spark.read.parquet(temp_path)

        # Append the DataFrame to the list
        dfs.append(df)

        # Store the temporary file path
        temp_files.append(temp_path)

    # Concatenate all the DataFrames in the list
    final_df = dfs[0]
    for df in dfs[1:]:
        final_df = final_df.union(df)

    return final_df, temp_files


def remove_temp(temp_files):
    
    # Delete all temporary files
    for temp_file in temp_files:
        os.remove(temp_file)


def reader():
    initialise_firebase()
    data = reader_bytes()
    df, temp = text_to_df(data)
    return df, temp 
