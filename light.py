import requests

URL = "http://10.140.4.163:5000"
ON_URL = URL + "/on"
OFF_URL = URL + "/off"

def on():
    r = requests.get(url = ON_URL)
    return r.text

def off():
    r = requests.get(url = OFF_URL)
    return r.text