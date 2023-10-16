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
