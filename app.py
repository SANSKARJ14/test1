from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Flask!"

@app.route('/cal', methods = ['get','post'])
def mathmetical_operator():
    operation=request.json["operation"]
    number1=request.json["number1"]
    number2= request.json["number2"]

    if operation == "add":
        ruselt = number1+number2
    elif operation == "subtract":
        ruselt = number1-number2
    elif operation == "division":
        ruselt = number1/number2
    else:
        ruselt = number1*number2



if __name__ == '__main__':
    app.run('0.0.0.0', port=8080)
