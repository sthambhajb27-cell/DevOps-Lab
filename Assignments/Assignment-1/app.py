from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

# Connect to MongoDB
# The hostname 'mongo' should match the container name in the Docker network
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://mongo:27017/')
client = MongoClient(MONGO_URI)
db = client.taskdb
tasks_collection = db.tasks

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = []
    for task in tasks_collection.find({}, {"_id": 0}):
        tasks.append(task)
    return jsonify(tasks), 200

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    tasks_collection.insert_one(data)
    return jsonify({"message": "Task created successfully"}), 201

@app.route('/tasks/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    tasks_collection.update_one({"id": task_id}, {"$set": data})
    return jsonify({"message": "Task updated successfully"}), 200

@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks_collection.delete_one({"id": task_id})
    return jsonify({"message": "Task deleted successfully"}), 200

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
