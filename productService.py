from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["microservices_demo"]         # Match the original naming
products_collection = db["products"]      # Same as original dict name

@app.route('/products/<product_id>', methods=['GET'])
def get_product(product_id):
    product = products_collection.find_one({"id": product_id}, {"_id": 0})
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(port=5002)
