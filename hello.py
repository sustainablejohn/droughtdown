from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
@app.route("/test/<string:user>")
def hello2(user):
    return "Hello %s!" % (user)
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = True)
