from flask import Flask, render_template, redirect, url_for
import os, sys

from sound import Sound
from light import led
import keyboard


app = Flask(__name__)

# MEDIA
@app.route('/media_pause', methods=["GET", 'POST'])
def media_pause():
    '''
    Pauses the media
    '''
    keyboard.press_and_release('space')
    return redirect(url_for('index'))

@app.route('/media_rewind', methods=["GET", 'POST'])
def media_rewind():
    '''
    Rewinds the media
    '''
    keyboard.press_and_release('left')
    return redirect(url_for('index'))

@app.route('/media_forward', methods=["GET", 'POST'])
def media_forward():
    '''
    Skips forward in the media
    '''
    keyboard.press_and_release('right')
    return redirect(url_for('index'))

# VOLUME
@app.route('/media_volume_up', methods=["GET", 'POST'])
def media_volume_up():
    '''
    Turns up the master volume
    '''
    Sound.volume_up(4)
    return redirect(url_for('index'))

@app.route('/media_volume_down', methods=["GET", 'POST'])
def media_volume_down():
    '''
    Turns down the master volume
    '''
    Sound.volume_down(4)
    return redirect(url_for('index'))

@app.route('/media_volume_mute', methods=["GET", 'POST'])
def media_volume_mute():
    '''
    Mutes the volume
    '''
    Sound.mute()
    return redirect(url_for('index'))

# POWER OFF
@app.route('/admin_computer_off', methods=["GET", 'POST'])
def admin_computer_off():
    '''
    Shuts down the windows OS instantly and comments as to why the shutdown occured.
    '''
    os.system('shutdown -s -t 0 /c "Web Python Script Shutdown -d u"')
    return redirect(url_for('index'))

# LED CONTROL
@app.route('/led_on', methods=["GET", 'POST'])
def led_on():
    '''
    Turns on LED strip
    '''
    led.on()
    return redirect(url_for('index'))

@app.route('/led_off', methods=["GET", 'POST'])
def led_off():
    '''
    Turns off LED strip
    '''
    led.off()
    return redirect(url_for('index'))

# Distinct Page Display
@app.route('/')
def index():
    '''
    Returns index.html
    '''
    return render_template('index.html')

@app.route('/admin', methods=["GET", 'POST'])
def admin():
    '''
    returns admin.html
    '''
    return render_template('admin.html')

# START SERVICE
def run_web(port = 5000):
    '''
    Starts web service on port param
    :param port: port of web service defaults = 5000
    '''
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    run_web()