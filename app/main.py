
from flask import Flask 
import requests
from ipwhois import IPWhois
  
app = Flask(__name__) 
  
@app.route("/") 
def home_view():
  try:
    ip = requests.get('https://api.ipify.org?format=json')

    lookup = IPWhois(ip.json()['ip']).lookup_whois()

    return f"<h1>Welcome to our crypto trading profile!! </br> this is running at IP/region : {ip.json()['ip']} {lookup['nets'][0]['description']} {lookup['nets'][0]['country']}</h1>"
  except Exception as e:
    return f"<h1>can not get ip {str(e)}</h1>"
