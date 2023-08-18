from flask import Flask, render_template, redirect, url_for
import os
from sound import Sound
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from keyboard import Keyboard
import light


import math
app = Flask(__name__)

@app.route('/media_pause', methods=["GET", 'POST'])
def media_pause():
    Keyboard.key(Keyboard.VK_SPACE)
    return redirect(url_for('index'))

@app.route('/media_rewind', methods=["GET", 'POST'])
def media_rewind():
    return redirect(url_for('index'))

@app.route('/media_volume_up', methods=["GET", 'POST'])
def media_volume_up():
    Sound.volume_up()
    return redirect(url_for('index'))

@app.route('/media_volume_down', methods=["GET", 'POST'])
def media_volume_down():
    Sound.volume_down()
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
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = interface.QueryInterface(IAudioEndpointVolume)

    print(volume.GetMute())
    print(volume.GetVolumeRange())
    volume.SetMasterVolumeLevel(-20.0, None)
    print(volume.GetMasterVolumeLevel())

    print(f"Value: {35.171868 * math.log10(.27)} Error Wrong: {-20.0 / (35.171868 * math.log10(.27))}")
    print(f"Value: {35.171868 * math.log10(.52)} Error Wrong: {-10.0 / (35.171868 * math.log10(.52))}")

    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    run_web()