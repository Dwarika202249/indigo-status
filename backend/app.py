from flask import Flask, jsonify
from flask_cors import CORS
from flightdata import flights
from pymongo import MongoClient
import firebase_admin
from firebase_admin import credentials, messaging

app = Flask(__name__)
CORS(app)

# MongoDB setup
client = MongoClient('mongodb://localhost:27017/')
db = client.flight_status
flights_collection = db.flights

# flights_collection.insert_many(flights)

# Initialize Firebase Admin SDK
cred = credentials.Certificate('./serviceAccountKey.json')
firebase_admin.initialize_app(cred)

def send_notification(token, title, body):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        token=token,
    )

    response = messaging.send(message)
    print('Successfully sent message:', response)

# Example usage
# send_notification('device_token', 'Flight Status Update', 'Your flight AI101 is now On Time')


@app.route('/api/flights', methods=['GET'])
def get_flights():
    flights = list(flights_collection.find({}, {'_id': 0}))
    return jsonify(flights)

if __name__ == '__main__':
    app.run(debug=True)
