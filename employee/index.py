from flask import Flask, jsonify, request
app = Flask(__name__)

employee = [
	{'emp_name':'Pradeep','emp_id':13515},
	{'emp_name':'Pallavi','emp_id':12984}
]

@app.route("/employee")
def get_employee():
	return jsonify(employee)

@app.route("/employee",methods=['POST'])
def add_employee():
	employee.append(request.get_json())
	return '',204

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("4000"), debug=True)
