import os 
import json 
import firebase_admin 
from firebase_admin import credentials
from firebase_admin import firestore 

def firebase_access(service_account_key_path):
    # Initialize the Firebase Admin SDK
    try:
        cred = credentials.Certificate(service_account_key_path)
        default_app = firebase_admin.initialize_app(cred)
        db = firestore.client()
        return db
    except Exception as e:
        print(f"Error initializing Firebase: {e}")
        return None


# def add entry(db) 

