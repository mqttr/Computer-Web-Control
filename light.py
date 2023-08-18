import requests

class led:

    URL = "http://10.140.4.163:5000"
    ON_URL = URL + "/on"
    OFF_URL = URL + "/off"

    def on():
        r = requests.get(url = led.ON_URL)
        return r.text

    def off():
        r = requests.get(url = led.OFF_URL)
        return r.text