from flask import Flask
from flask import request

# library used to make api
app = Flask(__name__)
# app variable is object of flask class

#decorator
@app.route("/")
# function
def hello_world():
    return "<h1>Hello, World!</h1>"

#decorator
@app.route("/hello_world1")
# function
def hello_world1():
    return "<h1>Hello, World1!</h1>"

#decorator
@app.route("/hello_world2")
# function
def hello_world2():
    return "<h1>Hello, World2!</h1>"

@app.route("/test")
def test():
    a=11
    return "this is my function to run app  {}".format(a)
#   placeholder -> {}

@app.route("/test2/test2")
def test2():
    data=request.args.get("x")
    return "this is a data input from my url{}".format(data)



if __name__=="__main__":
    # ip address of local host
    app.run(host="0.0.0.0")
