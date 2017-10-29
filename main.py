import os
import flask
app = flask.Flask(__name__)

@app.route("/")
def main():
    html = "Hello World!\nHow you doing?"
    print(html)

if __name__ == "__main__:
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
