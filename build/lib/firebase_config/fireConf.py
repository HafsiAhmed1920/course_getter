import firebase_admin
from firebase_admin import credentials


def initialise_firebase():
    cred = credentials.Certificate(r'C:\Users\ahafsi\project beta\data-pipeline.json')
    firebase_admin.initialize_app(cred,
                                  {'storageBucket': 'datapipe-aad93.appspot.com'})
