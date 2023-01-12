from flask import Flask

app = Flask(__name__)

@app.route("/test")
def test():
    return "Service 1 called"
