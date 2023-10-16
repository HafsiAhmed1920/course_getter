from confluent_kafka import Consumer
import threading
import json 
import time 
import sys

last_message_time = time.time()


def reciever(q):
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
            q.put(msg.value().decode('utf-8'))


def check_inactivity(q, timeout=10):
    global last_message_time
    while True:
        if (time.time() - last_message_time) > timeout:
            q.put(None)
            break


def processor(q, evaluator):
    global last_message_time
    while True:
        # get the message from the queue
        msg = q.get()
        if msg is None:
            print("there is no such thing in our data base ! its either you mispelled it or we didn't get such a product yet !! it will be available soon ! !!!! ")
            sys.exit(1)
        msg = json.loads(msg)
        # use the message 
        if evaluator(msg.get('course1')): 
            last_message_time = time.time()
            print(f"this one : {msg}")


def consumer_thread(q):
    cons_thread = threading.Thread(target=reciever, args=(q,))
    cons_thread.start()


def timer_thread(queue, timeout=10):
    tiThread = threading.Thread(target=check_inactivity, args=(queue, timeout))
    tiThread.start()


def processor_thread(q,  evaluator):
    pros_thread = threading.Thread(target=processor, args=(q, evaluator))
    pros_thread.start()
    timer_thread(q)
