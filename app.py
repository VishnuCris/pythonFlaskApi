from flask import Flask,jsonify,request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route("/")
def get_example():
    """GET in server"""
    response = jsonify(message="Simple server is running")

    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/post",methods = ['POST', 'GET'])
def post():
	print(request)
	response = jsonify(message="post returns")
	response.headers.add("Access-contol-Allow-orgin","*")
	print(response)
	return response    

if __name__ == "__main__":
    app.run()
