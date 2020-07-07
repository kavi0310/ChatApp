from pymongo import MongoClient
from werkzeug.security import generate_password_hash

client = MongoClient("mongodb+srv://mongodb_student:mongodb_mongo@sandbox-m4yaf.mongodb.net/test?authSource=admin&replicaSet=Sandbox-shard-0&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=true")

chat_db = client.get_database("ChatDB")
users_collection = chat_db.get_collection("users")


def save_user(username, email, password):
    password_hash = generate_password_hash(password)
    users_collection.insert_one({'_id': username, 'email': email, 'password': password_hash})


save_user("kavitha","ab@c,com","kavi")