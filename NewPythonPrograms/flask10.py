from flask import Flask

app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/porter")
def port():
    return "hello Porter"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=4000)