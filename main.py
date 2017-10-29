from flask import Flask

app = Flask(__name__)

@app.route('/')
def source():
    html = "Hello World!\nHow you doing?"
    print(html)
