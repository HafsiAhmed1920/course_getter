from main_kafka.producer import production
from process.process_toget_data import process_toget_data
from main_kafka.consumer import consThread
from firebase_config.fireConf import initialise_firebase
       
                                                                             
initialise_firebase()
process_toget_data()
production()
consThread() 
