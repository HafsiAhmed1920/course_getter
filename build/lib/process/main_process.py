from kafka.consumer import consThread
from kafka.producer import production
from process.process_toget_data import process_toget_data
                                                                                           

process_toget_data()
production()
consThread() 
