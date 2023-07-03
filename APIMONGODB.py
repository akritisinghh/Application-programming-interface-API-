from flask import Flask, request, jsonify
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://akritisingh:akritisingh@cluster0.8d5kqsv.mongodb.net/")
database = client ['APIMongodb']
collection = database['apimongodbdata']

@app.route("/insert/mongodb", methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name:number})
        return jsonify({'message': 'Data inserted successfully'})


@app.route("/update/mongodb", methods = ['POST'])
def update():
    if request.method == 'POST':
        name = request.json['name']
        new_number = request.json['new_number']
        collection.update_one({'name' : name}, {'$set': {'number' : new_number}})
        return jsonify({'message': 'Data updated successfully'})

@app.route("/delete/mongodb", methods = ['POST'])
def delete():
    if request.method == 'POST':
        name = request.json['name']
        collection.delete_one({'name': name})
        return jsonify({'message': 'Data Deleted successfully'})


@app.route("/fetch", methods = ['POST'])
def fetch_data():
    data = list(collection.find({}, {'_id': 0}))  # Fetch all documents from the collection and exclude '_id' field
    return jsonify(data)




if __name__ == '__main__':
    app.run(port = 5001)  #Changing port no because same port is running in mysql API which is giving error; either restart pycharm or change port
