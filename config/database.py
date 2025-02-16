from pymongo import AsyncMongoClient
from config.settings import MONGO_URI

def connect_to_mongo():
    try:
        client = AsyncMongoClient(MONGO_URI)
        db = client.get_database()
        print(f"✅ Successfully connected to MongoDB: {db.name}")  # Print confirmation
        return db
    except Exception as e:
        print(f"❌ MongoDB Connection Error: {e}")  # Print error if connection fails
        return None

# Run the connection when database.py is imported
db = connect_to_mongo()
