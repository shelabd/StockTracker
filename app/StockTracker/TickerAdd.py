import os
import pymongo
import urllib.parse
import configparser
from flask import Flask, request, render_template
from bson import ObjectId

# Load the MongoDB credentials from the config file
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '../config.ini'))
current_directory = os.path.dirname(__file__)

# Get the MongoDB credentials from the config file
mongo_user = config.get('DEFAULT', 'mongo_user')
mongo_password = config.get('DEFAULT', 'mongo_password')

# URL encode the password in case of special characters
encoded_password = urllib.parse.quote(mongo_password, safe='')

# Connect to MongoDB
def connect():
    client = pymongo.MongoClient(f"mongodb+srv://{mongo_user}:{encoded_password}@tickers.sgstcda.mongodb.net/test?retryWrites=true&w=majority", serverSelectionTimeoutMS=60000)
    db = client["StockTracker"]
    collection = db["tickers"]
    return collection

app = Flask(__name__)
collection = connect()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the form data
        name = request.form.get("name")
        symbol = request.form.get("symbol")

        # Create a new document
        new_ticker = {
            "_id": ObjectId(),
            "name": name,
            "symbol": symbol
        }

        # Insert the document into the collection
        collection.insert_one(new_ticker)

    return render_template('index.html')

if __name__ == "__main__":
    app.run()
