import os
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def firebase_access(service_account_key_path):
    """Initialize the Firebase Admin SDK"""
    try:
        cred = credentials.Certificate(service_account_key_path)
        default_app = firebase_admin.initialize_app(cred)
        db = firestore.client()
        return db
    except Exception as e:
        print(f"Error initializing Firebase: {e}")
        return None


def add_entry(db, score, username = "null"):
    """Add record to database"""
    try:
        scores_ref = db.collection("scores")
        scores_ref.add({"score": score, "username" : username})

    except Exception as e:
        print("Error adding user / score")


def get_top_five(db):
<<<<<<< HEAD
    scores_dict = {}
=======
    """Get top five highscores"""
>>>>>>> c1e9be254666e13cf349eb35ab9885f07239e543
    scores_ref = db.collection("scores")
    query = scores_ref.order_by("score").limit_to_last(5)
    docs = query.get()
    for doc in docs:
        scores_dict[doc.id] = doc.to_dict()
    return scores_dict
