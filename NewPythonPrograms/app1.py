from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route('/')
def hey():
    return redirect(url_for('heythere'))
        
@app.route('/healthy')
def heythere():
    return "hello worlds"

if __name__=='__main__':
    app.run()

