import socket, os
from flask import Flask 

import datetime

app = Flask(__name__)

app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
flask_port=8888
hostname = socket.gethostname()

@app.route("/whatsthetime",methods=["GET"])
def epochtime():
    return f"<H1>[{hostname}] The Time is  : {datetime.datetime.now().strftime('%m/%d/%Y, %H:%M:%S.%f')}</H1>"

app.run(host="0.0.0.0", port=flask_port, debug=False)