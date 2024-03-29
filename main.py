from flask import Flask, render_template

# __name__ determines the root directory for the application
app = Flask(__name__)


# The association between a URL and the function that handles it is called
# a route. The function index is called a view function.
@app.route("/")
def index():
    @app.route("/")
    def index():
        return render_template("index.html")

    return "<h1>Hello World!</h1>"


@app.route("/user/<name>")
def user(name):
    return "<h1>Hello, {}!</h1>".format(name)
