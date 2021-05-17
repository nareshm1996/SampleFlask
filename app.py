from flask import Flask
from flask_ipinfo import IPInfop

app = Flask(__name__)
ipinfo = IPInfo()

@app.route("/")
def hello():
    return "Your IP Address is :" + ipinfo.ipaddress

if __name__ == "__main__":
    app.run()
