import time
from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route("/")
def home():
    #return {'time': time.time()}
    return "Heyyyy!!"

@app.route('/time')
def get_time():
    return {'time': time.time()}

@app.route("/<name>")
def user(name):
    return f"Hello, {name}!!!"

if __name__ == "__main__":
    app.run()