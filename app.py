from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "hello sameer1"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
