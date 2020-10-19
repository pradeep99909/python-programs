from flask import Flask
from flask import jsonify,make_response
from flask import request
#import requests

from flask_cors import CORS,cross_origin
app=Flask(__name__)
CORS(app)

@app.route("/a",methods=["GET"])
def hello():
	data = request.args['arg1']
	data=data.split(',')
	print(data)
	ret={1:'hello',2:'bye'}
	res = make_response(jsonify({"message": ret}), 200)
	return res
if __name__ == '__main__':
    app.run()
