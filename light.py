import requests

class led:
    def __init__(self):
        self.URL = "http://10.140.4.163:5000"
        self.ON_URL = self.URL + "/on"
        self.OFF_URL = self.URL + "/off"

    def on(self):
        r = requests.get(url = self.ON_URL)
        return r.text

    def off(self):
        r = requests.get(url = self.OFF_URL)
        return r.text