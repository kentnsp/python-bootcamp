from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


app.run()
