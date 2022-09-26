import numpy as np
import pandas as pd
from pydub import AudioSegment
import pydub

def load_audio(path, duration):
    audio = pydub.AudioSegment.silent(duration=duration)
    audio = audio.overlay(AudioSegment.from_file(path).set_frame_rate(22050).set_channels(1))[0:duration]
    raw = (np.fromstring(audio._data, dtype="int16") + 0.5) / (0x7FFF + 0.5)   # convert to float
    return raw


if __name__ == '__main__':
    audio = AudioSegment.silent(duration=5000)
    audio = audio.overlay(AudioSegment.from_file("./base.wav").set_frame_rate(22050).set_channels(1))[0:5000]
    raw = (np.fromstring(audio._data, dtype="int16") + 0.5) / (0x7FFF + 0.5)
    
    