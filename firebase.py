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
    """Get top five highscores"""
    scores_ref = db.collection("scores")
    query = scores_ref.order_by("score").limit_to_last(3)
    results = query.get()
    return results
