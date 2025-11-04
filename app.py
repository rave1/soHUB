from flask import Flask, request

app = Flask(__name__)


@app.route("/temp", methods=["POST"])
def temp():
    print("---- NEW REQUEST ----")
    print("Headers:", dict(request.headers))
    print("Raw body:", request.data)
    print("Form data:", request.form)
    print("JSON:", request.get_json(silent=True))
    print("----------------------", flush=True)
    return "Good!", 201
