import os
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv

class FireStoreClient:
    def __init__(self):    
        load_dotenv()
        cred = credentials.Certificate("firebase-secret.json")
        firebase_admin.initialize_app(cred, {
            "projectId": os.environ["GCLOUD_PROJECT"]
        })
        self.db = firestore.client()
        
    def addUser(self):
        pass
        
if __name__ == "__main__":
    db = FireStoreClient()
