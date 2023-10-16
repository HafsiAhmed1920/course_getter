from process.process_toget_data import process_toget_data
from kafka.consumer import consThread
from kafka.producer import production


process_toget_data()
production()
consThread()