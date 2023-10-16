from kafka_config.producer import send_df_as_json
from reader.reader import reader, remove_temp


df, temp = reader()
send_df_as_json(df)
print("success")
remove_temp(temp)
