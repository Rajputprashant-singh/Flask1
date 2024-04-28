from flask import Flask, request, jsonify

obj = Flask(__name__)

@obj.route('/')
def hello():
    return "Hello, World!"

@obj.route('/cal', methods=["POST"])
@obj.route('/cal', methods=["GET"])
def math_operator():
    data = request.get_json()
    operation = data["operation"]
    number1 = data["number1"]
    number2 = data["number2"]
    
    if operation == "add":
        result = int(number1) + int(number2)
    elif operation == "multiply":
        result = int(number1) * int(number2)
    elif operation == "division":
        result = int(number1) / int(number2)
    else:
        result = int(number1) - int(number2)
        
    return jsonify({"result": result})

if __name__ == '__main__':
    obj.run(debug=True)
