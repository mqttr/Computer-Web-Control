from flask import Flask, render_template, redirect, url_for
import os
from sound import Sound
import keyboard

app = Flask(__name__)

@app.route('/media_pause', methods=["GET", 'POST'])
def media_pause():
    keyboard.press_and_release('space')
    return redirect(url_for('index'))

@app.route('/media_rewind', methods=["GET", 'POST'])
def media_rewind():
    return redirect(url_for('index'))

@app.route('/media_volume_up', methods=["GET", 'POST'])
def media_volume_up():
    Sound.volume_up(4)
    return redirect(url_for('index'))

@app.route('/media_volume_down', methods=["GET", 'POST'])
def media_volume_down():
    Sound.volume_down(4)
    return redirect(url_for('index'))

@app.route('/media_volume_mute', methods=["GET", 'POST'])
def media_volume_mute():
    Sound.mute()
    return redirect(url_for('index'))

@app.route('/admin_computer_off', methods=["GET", 'POST'])
def admin_computer_off():
    os.system('shutdown -s -t 0 /c "Web Python Script Shutdown -d u"')
    return redirect(url_for('index'))

@app.route('/admin_stop_service', methods=["GET", 'POST'])
def admin_stop_service():
    exit()
    return redirect(url_for('index'))

@app.route('/led_on', methods=["GET", 'POST'])
def led_on():
    light.on()
    return redirect(url_for('index'))


@app.route('/led_off', methods=["GET", 'POST'])
def led_off():
    light.off()
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html')

def run_web():
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    run_web()