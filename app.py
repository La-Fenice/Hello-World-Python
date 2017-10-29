from datetime import datetime
from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Hello World</h1>
    <h2>My name is Edward Maguire</h2>
    <h3>This webapp was made using python/flask/html and is hosted
    for free on <a href="https://dashboard.heroku.com/apps">heroku</a></h3>
    <h3>It is currently {time}.</h3>
    <img src="https://fiverr-res.cloudinary.com/t_main1,q_auto,f_auto/gigs/46941709/original/d5ace87ba59d0d4e5151668e60e8eaf673153ff7.jpg">
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
