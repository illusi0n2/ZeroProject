from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
@app.route("/index/")
def index():
    """Главная страница с текущей датой и временем"""
    current_time = datetime.now()
    return render_template('index.html',
                         current_time=current_time,
                         time_str=current_time.strftime("%d.%m.%Y %H:%M:%S"))

@app.route("/main/")
def main_page():
    return render_template("main.html")

@app.route("/blog/")
def blog_page():
    return render_template("blog.html")

@app.route("/contacts/")
def contacts_page():
    return render_template("contacts.html")

if __name__ == '__main__':
    app.run()
