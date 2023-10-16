from kafka_config.conConf import consumer_thread, processor_thread
import queue

course_wanted = input("what is the course you are seeking for ? ")


def evaluator(course_name: str): 
    if course_name.lower() == course_wanted.lower():
        return True
    return False


def consThread():
    # Create a queue
    q = queue.Queue()
    consumer_thread(q)
    processor_thread(q, evaluator)
