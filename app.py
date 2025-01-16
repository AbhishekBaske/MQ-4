from flask import Flask, render_template
from pymongo import MongoClient

# MongoDB connection
MONGO_URI = "mongodb+srv://AbhishekBaske:Fjxd4014@cluster0.voz8a.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)
db = client.get_database('my_database')  # Database name
collection = db.get_collection('serial_data')  # Collection name

# Initialize Flask application
app = Flask(__name__)

@app.route('/')
def home():
    # Fetch the data from MongoDB
    data = list(collection.find().sort("timestamp", -1).limit(10))  # Retrieve the latest 10 entries
    for item in data:
        item["_id"] = str(item["_id"])  # Convert ObjectId to string for JSON compatibility
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
