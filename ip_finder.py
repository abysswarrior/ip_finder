from ipify import get_ip                                                                                                                                        
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():                                                                                                                                                     
    ip = get_ip()                                                                                                                                                   
    return str(ip)
