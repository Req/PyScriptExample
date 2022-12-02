# src/controls.py

import numpy as np

from pyodide import create_proxy, to_js

from js import updateChart
from js import updateAudio
from waveform import band_limited_noise

range1 = document.querySelector("#range1")
range2 = document.querySelector("#range2")

samplerate = 44100


def on_range_update(event):
    label = event.currentTarget.nextElementSibling
    label.innerText = event.currentTarget.value
    plot_waveform()

    #waveform = band_limited_noise()
    #updateAudio(waveform) 

def plot_waveform():
    frequency = float(range1.value)
    width = float(range2.value)

    #waveform = wave(frequency1)(time) + wave(frequency2)(time)
    #updateChart(to_js(time), to_js(waveform))

    waveform = band_limited_noise(mid_freq = frequency, width_freq = width, samplerate=samplerate, duration=1)
    print(waveform)
    updateAudio(waveform) 


proxy = create_proxy(on_range_update)
range1.addEventListener("input", proxy)
range2.addEventListener("input", proxy)

plot_waveform()