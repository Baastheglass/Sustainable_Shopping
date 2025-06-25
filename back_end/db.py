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
         # Run aggregation query
        count_query = self.db.collection("users").count()
        aggregation_results = count_query.get()

        # aggregation_results is a list; extract the first result
        agg_result = aggregation_results[0]  # type: google.cloud.firestore_v1.base_aggregation.AggregationResult
        count_value = agg_result.value  # integer count

        print(f"Current user count: {count_value}")
        
        self.db.collection("users").add({
            "id": count_value + 1,
            "username": "johndoe",
            "name": "John Doe",
            "email": "john.doe@example.com",
            "password": "turtles",  
        })
        
if __name__ == "__main__":
    db = FireStoreClient()
    db.addUser()