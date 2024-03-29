from flask import Flask

# __name__ determines the root directory for the application
app = Flask(__name__)


# The association between a URL and the function that handles it is called
# a route. The function index is called a view function.
@app.route("/")
def index():
    return "<h1>Hello World!</h1>"
