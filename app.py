from flask import Flask, jsonify
from corrector import search_word

app = Flask(__name__)


@app.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    return "Welcome to the simple spelling corrector interface! Test test"


@app.route("/correct/<string:word>")
def correct(word):
    pred = search_word(word)
    val = {"Input": word, "Correct": pred}
    return jsonify(val)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081, debug=True)