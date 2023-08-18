import requests




class led:
    def __init__(self):
        self.URL = "http://10.140.4.163:5000"
        self.ON_URL = self.URL + "/on"
        self.OFF_URL = self.URL + "/off"

    def on(self):
        requests.get(url = self.ON_URL)

    def off(self):
        requests.get(url = self.OFF_URL)

if __name__ == "__main__":
    a = led()
    a.off()