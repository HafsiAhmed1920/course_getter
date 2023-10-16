from kafka_config.prodConf import send_df_as_json
from reader.reader import reader, remove_temp


def production():
    df, temp = reader()
    send_df_as_json(df)
    print("success")
    remove_temp(temp)
