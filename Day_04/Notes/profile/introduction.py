from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def index():
    return "Index Page"
@app.route("/profile/")
@app.route("/profiles/")
def profile():
    return "Leomhar Ken Lico"

@app.route("/profile/hobby")
@app.route("/profile/hobbies")
def hobby():
    return "Watch and read"

@app.route("/profile/interest")
@app.route("/profiles/interests")
def interest():
    return "open world games"

@app.route("/profile/opinion")
@app.route("/profile/opinions")
def opinion():
    return "my opinion on delicious foods is yes."
@app.route("/coffee/")
def coffee():
    return render_template("coffee_lover.html")

@app.route("/profile/joke")
@app.route("/profile/jokes")
def opinion():
    return "my opinion on delicious foods is yes."


app.run()