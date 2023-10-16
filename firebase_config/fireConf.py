import firebase_admin
from firebase_admin import credentials


def initialise_firebase():
    cred = credentials.Certificate(r'Path to your credentiels\data-pipeline.json')
    firebase_admin.initialize_app(cred,
                                  {'storageBucket': your-bucket-url.com'})
