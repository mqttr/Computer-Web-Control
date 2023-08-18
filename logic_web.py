from flask import Flask, render_template, redirect, url_for
import os
from sound import Sound
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from keyboard import Keyboard
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

@app.route('/')
def index():
    return render_template('index.html')

def run_web():

    # devices = AudioUtilities.GetSpeakers()
    # interface = devices.Activate(
    #     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    # volume = interface.QueryInterface(IAudioEndpointVolume)
    # volume.GetMute()
    # print(volume.GetMasterVolumeLevel())
    # print(volume.GetVolumeRange())
    # volume.SetMasterVolumeLevel(-10.0, None)
    # print(volume.GetMasterVolumeLevel())

    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    run_web()