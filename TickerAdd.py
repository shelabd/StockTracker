from flask import Flask, request
from bson import ObjectId
from urllib.parse import urlencode, quote_plus
import configparser
import urllib.parse
import pymongo

app = Flask(__name__)

# Read the credentials from the config file
config = configparser.ConfigParser()
config.read("config.ini")

#URL encode the password in case of special characters
encoded_password = urllib.parse.quote(config['DEFAULT']['MONGO_PASSWORD'], safe='')

print(encoded_password)
# Connect to MongoDB
client = pymongo.MongoClient(f"mongodb+srv://{config['DEFAULT']['MONGO_USER']}:{encoded_password}@tickers.sgstcda.mongodb.net/?retryWrites=true&w=majority", serverSelectionTimeoutMS=60000)
db = client["StockTracker"]
collection = db["tickers"]

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

    return """
        <html>
            <body>
                <form action="/" method="post">
                    <input type="text" name="name" placeholder="Name">
                    <input type="text" name="symbol" placeholder="Symbol">
                    <input type="submit" value="Submit">
                </form>
            </body>
        </html>
    """

if __name__ == "__main__":
    app.run()
