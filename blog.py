from flask import Flask, render_template

app = Flask(__name__)


# decorator
@app.route("/")  # request = root(/)
def index():
    return render_template("index.html")


@app.route("/about")  # request = root(/)
def about():
    return render_template("index.html")


@app.route("/articles")  # request = root(/)
def articles():
    return render_template("index.html")


@app.route("/register")  # request = root(/)
def register():
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)
