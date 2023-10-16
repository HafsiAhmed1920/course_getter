from main_kafka.producer import production
from process.process_toget_data import process_toget_data
from main_kafka.consumer import consThread
                                                                             

process_toget_data()
production()
consThread() 
