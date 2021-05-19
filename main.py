from flask import Flask, flash, redirect, render_template, request, url_for

from firebase_admin import credentials, firestore
import firebase_admin

import json
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "DEBUG"

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

    flash(u'등록되지 않은 사용자입니다.', 'error')

    for userDoc in userDocs:
        userInfo = userDoc.to_dict()
        if userDoc.id == userID:
            if userInfo["PW"] == userPW:
                return redirect(url_for("render_main", userData = userID))
            else:
                flash(u'비밀번호가 올바르지 않습니다.', 'error')

    return render_template("login.html")

@app.route("/main", methods=["GET", "POST"])
def render_main():
    curUser = request.args.get("userData")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 80)