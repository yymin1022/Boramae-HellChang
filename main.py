from flask import Flask, redirect, render_template, request, url_for

from firebase_admin import credentials, firestore
import firebase_admin

import requests

app = Flask(__name__)

@app.route("/")
def render_login():
    return render_template("login.html")

@app.route("/auth", methods=["GET", "POST"])
def render_auth():
    userID = request.form["userID"]
    userPW = request.form["userPW"]

    if (not len(firebase_admin._apps)):
        serverCredentials = credentials.Certificate("/home/server/web/serviceInfo.json")
        firebase_admin.initialize_app(serverCredentials)

    db = firestore.client()

    userList = db.collection(u'user')
    userDocs = userList.stream()

    for userDoc in userDocs:
        userInfo = userDoc.to_dict()
        if userDoc.id == userID and userInfo["PW"] == userPW:
            return redirect(url_for("render_main", user = userID), code=307)

    return render_template("auth.html")

@app.route("/main", methods=["GET", "POST"])
def render_main():
    print(request.args.get("userData"))
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 80)