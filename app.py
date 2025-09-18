from flask import Flask, render_template, request, session, redirect, url_for
from datetime import datetime

app = Flask(__name__)
app.secret_key = "dev-secret"   # dev use only; professor expects session usage

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sign", methods=["GET","POST"])
def sign():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            entry = {"name": name, "time": datetime.now().strftime("%H:%M:%S")}
            guestbook = session.get("guestbook", [])
            guestbook.insert(0, entry)
            session["guestbook"] = guestbook
        return redirect("/guestbook")
    return render_template("sign.html")

@app.route("/guestbook")
def guestbook():
    # Using session inside the template (prof's snippet uses session.guestbook)
    return render_template("guestbook.html")

@app.route("/clear")
def clear():
    session["guestbook"] = []
    return redirect(url_for("guestbook"))

if __name__ == "__main__":
    app.run(debug=True)
