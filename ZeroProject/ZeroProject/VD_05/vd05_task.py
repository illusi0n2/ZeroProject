from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home/")
def home_page():
    context = {
        "title" : "Home"
    }
    return render_template("home.html", **context)

@app.route("/about/")
def about_page():
    context = {
        "title" : "Home"
    }
    return render_template("about.html", **context)

if __name__ == '__main__':
    app.run()
