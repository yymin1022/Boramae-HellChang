from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)

@app.route('/')
def render_login():
    return render_template("login.html")

@app.route("/auth")
def render_auth():
    return render_template("auth.html")

@app.route("/main")
def render_main():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80)