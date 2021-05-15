from flask import Flask, redirect, render_template, request, url_for

from firebase_admin import credentials, firestore
import firebase_admin

app = Flask(__name__)

@app.route("/")
def render_login():
    return render_template("login.html")

@app.route("/auth", methods=["GET", "POST"])
def render_auth():
    userID = request.form["userID"]
    userPW = request.form["userPW"]

    serverCredentials = credentials.Certificate("/home/server/web/serviceInfo.json")
    firebase_admin.initialize_app(serverCredentials)

    db = firestore.client()

    return render_template("auth.html")

@app.route("/main")
def render_main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 80)