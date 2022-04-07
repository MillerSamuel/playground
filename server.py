from turtle import color
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return "Hello"

@app.route('/play')
def play():
    return render_template("index.html",num=3,color="blue")

@app.route('/play/<int:num>')
def play2(num):
    return render_template("index.html",num=num,color="blue")

@app.route('/play/<int:num>/<color>')
def play3(num,color):
    return render_template("index.html",num=num,color=color)





if __name__=="__main__":
    app.run(debug=True)