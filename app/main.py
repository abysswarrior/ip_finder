
from flask import Flask 
from ipify import get_ip
  
app = Flask(__name__) 
  
@app.route("/") 
def home_view():
        ip = get_ip()
        return f"<h1>Welcome to our crypto trading profile!! </br> this will be run at {str(ip)}</h1>"
