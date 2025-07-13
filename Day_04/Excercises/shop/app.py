from flask import Flask, render_template, session, request, redirect
app = Flask(__name__)
app.secret_key = "secret"
@app.get('/')
def show_shop():
    if "shop" not in session:
        session["shop"] = []
    return render_template("homepage.html", shop=session["shop"])

@app.post("/")
def add():
    if request.form["shop"]:
        session["shop"].append(request.form["shop"])
    session.modified = True
    return redirect("/")

@app.post("/delete/item/")
def delete_item():
    shop = request.form["shop"]
    if shop in session.get("shop", []):
        session["shop"].remove(shop)
        session.modified = True
    return redirect("/")

app.run()