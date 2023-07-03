from flask import Flask, request, jsonify

app = Flask (__name__)   #object of class

@app.route('/abc', methods =['GET', 'POST']) #define route of function , GET & POST will send data
#GET means sending a data through url i.e google search; POST means posting a data in body i.e gmail entering username
def test1():
    if (request.method == 'POST'):
        a = request.json ['num1']
        b = request.json [  'num2']
        result = a+b
        return jsonify((str(result)))


@app.route('/abc1/testapi', methods = ['GET', 'POST'])
def test2():
    if (request.method == 'POST'):
        a = request.json ['num1']
        b = request.json [  'num2']
        result = a*b
        return jsonify((str(result)))


@app.route('/abc1/akki/test3', methods = ['GET', 'POST'])
def test3():
    if (request.method == 'POST'):
        a = request.json ['num1']
        b = request.json [  'num2']
        result = a/b
        return jsonify((str(result)))

@app.route('/abc1/akki/test4', methods = ['GET', 'POST'])
def test4():
    if (request.method == 'POST'):
        a = request.json ['num1']
        b = request.json [  'num2']
        result = a**b
        return jsonify((result))




if __name__ == '__main__' :
 app.run()


#def test(a,b):
 #   return a+b
#print(test (2,3))



