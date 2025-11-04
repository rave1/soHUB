from flask import Flask, request

app = Flask(__name__)


@app.route("/temp", methods=["POST"])
def temp():
    print(request.data)
