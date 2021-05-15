from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def render_main():
    return render_template('index.html')

@app.route("/login")
def render_login():
    return render_template("login.html")

@app.route("/main")
def render_main():
    return render_template("main.html")

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80)