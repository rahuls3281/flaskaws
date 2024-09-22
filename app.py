from flask import Flask


app=Flask(__name__)

@app.route("/")
def home():
    return {"message":"This is Home API"}

@app.route("/testing")
def testing():
    return {"message":"This is testing API"}
