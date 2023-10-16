from confluent_kafka import Producer

p = Producer({'bootstrap.servers': 'localhost:29092'})


def msg_feedback(err, msg): 
    if err is not None:
        print(f"Message delivery failed: {err} ")
    else:
        print(f"message delivered to {msg.topic()} ({msg.partition()})")


def send_msg(msg):
    p.produce('testing', msg, callback=msg_feedback)
    p.flush()


def send_df_as_json(df):
    # Convert DataFrame to JSON
    json_df = df.toJSON().collect()
    
    # Produce JSON messages to Kafka
    for json_row in json_df:
        p.produce('testing', json_row, callback=msg_feedback)
        
    p.flush()