import requests

class led:

    URL = "http://10.140.4.163:5000"
    ON_URL = URL + "/on"
    OFF_URL = URL + "/off"

    def on():
        '''
        Turns on LED strip by sending a GET request to the Raspeberryu Pi's web server
        '''
        r = requests.get(url = led.ON_URL)
        return r.text

    def off():
        '''
        Turns off LED strip by sending a GET request to the Raspeberryu Pi's web server
        '''
        r = requests.get(url = led.OFF_URL)
        return r.text