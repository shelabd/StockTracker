# Back-end

import pymongo
import configparser
import urllib.parse
# Flask app
from flask import Flask, request, render_template
from bson import ObjectId

# Read the credentials from the config file
config = configparser.ConfigParser()
config.read("config.ini")

# URL encode the password in case of special characters
encoded_password = urllib.parse.quote(config['DEFAULT']['MONGO_PASSWORD'], safe='')

# Connect to MongoDB
def connect():
    client = pymongo.MongoClient(f"mongodb+srv://{config['DEFAULT']['MONGO_USER']}:{encoded_password}@tickers.sgstcda.mongodb.net/?retryWrites=true&w=majority", serverSelectionTimeoutMS=60000)
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
