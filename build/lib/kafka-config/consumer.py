from confluent_kafka import Consumer


def reciever():
    c = Consumer({
        'bootstrap.servers': 'localhost:29092',
        'group.id': 'mygroup',
        'auto.offset.reset': 'earliest'
    })

    c.subscribe(['testing'])

    while True:
        msg = c.poll(1.0)

        if msg is None:
            continue
        else:
            print(f"Received message: {msg.value().decode('utf-8')}")
