import flask
app = flask.Flask(__name__)

@app.route("/")
def main():
    html = "Hello World!\nHow you doing?"
    print(html)

if __name__ == "__main__":
    app.run()
