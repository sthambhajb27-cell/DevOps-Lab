from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://mongo:27017/')
client = MongoClient(MONGO_URI)
db = client.treasurebook

@app.route('/node', methods=['POST'])
def add_node():
    data = request.json
    db.nodes.insert_one(data)
    return jsonify({"message": f"{data.get('Type')} added successfully"}), 201

@app.route('/edge', methods=['POST'])
def add_edge():
    data = request.json
    db.edges.insert_one(data)
    return jsonify({"message": f"{data.get('Type')} edge added successfully"}), 201

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
