import mysql.connector as conn
from flask import Flask, request, jsonify

app = Flask(__name__)

mydb = conn.connect(host="localhost", user="root", passwd="mysql@DS")
cursor = mydb.cursor()

# Create the 'apitest' database
cursor.execute("CREATE DATABASE IF NOT EXISTS apitest")

# Connect to the 'apitest' database
mydb = conn.connect(host="localhost", user="root", passwd="mysql@DS", database="apitest")
cursor = mydb.cursor()

# Create the 'mysqltable' table
cursor.execute("CREATE TABLE IF NOT EXISTS mysqltable (name varchar(30), number int(15))")


@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.json['name']
        number = request.json['number']
        cursor.execute("insert into mysqltable values (%s, %s)", (name,number))
        mydb.commit()
        return jsonify({'message': 'Data inserted successfully'})

@app.route("/update", methods = ['POST'])
def update():
    if request.method == 'POST':
        get_name = request.json['get_name']
        cursor.execute("update mysqltable set number = number + 500 where name = %s", (get_name,))
        mydb.commit()
        return jsonify({'message': 'Data Updated successfully'})

@app.route("/delete", methods = ['POST'])
def delete():
    if request.method == 'POST':
        name_del = request.json['name_del']
        cursor.execute("delete from mysqltable where name = %s ",(name_del, ))
        mydb.commit()
        return jsonify({'message': 'Data Deleted successfully'})

@app.route("/fetch", methods = ['POST'])
def fetch_data():
    cursor.execute("select * from mysqltable")
    l = []
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))


if __name__ == '__main__':
    app.run()