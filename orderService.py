from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["microservices_demo"]         # Match the original naming
products_collection = db["orders"]

@app.route('/orders', methods=['GET'])
def get_orders_by_user():
    user_id = request.args.get('user_id')
    user_orders = [order for order in orders if order["user_id"] == user_id]
    return jsonify(user_orders)

if __name__ == '__main__':
    app.run(port=5001)
