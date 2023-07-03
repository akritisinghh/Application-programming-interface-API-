import mysql.connector as conn
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/sql/testing', methods=['GET', 'POST'])
def api_testing():
    # Establish database connection
    mydb = conn.connect(host="localhost", user="root", passwd="mysql@DS", database="APITest")
    cursor = mydb.cursor()

    # Create table if it doesn't exist
    s = "CREATE TABLE IF NOT EXISTS akkidetails1 (employee_id INT(10), Employee_Name VARCHAR(80), employee_email_id VARCHAR(20), employee_salary INT(8), employee_attendance INT(3))"
    cursor.execute(s)

    # Execute a SELECT query
    cursor.execute("SELECT * FROM akkidetails1")
    result = cursor.fetchall()
    print(result)

    # Close the database connection
    cursor.close()
    mydb.close()

    return jsonify({"message": "API testing successful"})

if __name__ == '__main__':
    app.run()
