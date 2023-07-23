from flask import Flask, render_template

app = Flask(__name__,static_folder='templates/css')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/blank")
def blank():
    return render_template("secret.html")

@app.route("/<text>")
def err404(text):
    return render_template("404.html", page = text)


if __name__ == "__main__":
    app.run(debug=True, port=5000)