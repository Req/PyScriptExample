# src/controls.py

import numpy as np

from pyodide import create_proxy, to_js

from js import updateChart
from js import updateAudio
from waves import wave

range1 = document.querySelector("#range1")
range2 = document.querySelector("#range2")

sampling_frequency = 800
seconds = 1.5
time = np.linspace(0, seconds, int(seconds * sampling_frequency))

def band_limited_noise():#freq, width, samples=44100, samplerate=44100):

    print("here")
    samplerate = 4410
    # High sound: ca. 4200 Hz, 160 Hz bandwidth
    param = [4200, 160, 2*samplerate, samplerate, 0.001]

    freq = param[0]
    width = param[1]
    samples = int(param[2])
    samplerate = int(param[3])
    step = param[4] # 0.001

    t = np.linspace(0, samples/samplerate, samples)

    f = freq-width
    freqs = [f]
    counter = 0
    while f < freq:
        counter += 1
        # scipy.stats.norm(f, loc=freq, scale=width)
        q = f + np.random.normal(freq, width)
        df = step/q
        f += df 
        f1 = 2*freq - f + np.random.rand()
        freqs.append(f)
        freqs.append(f1)

    phases = np.random.rand(len(freqs))*2*np.pi
    signals = [np.sin(2*np.pi*freq*t + phase) for freq,phase in zip(freqs,phases)]
    signal = reduce(lambda a,b: a+b,signals)
    signal /= np.max(signal)
    return signal

def on_range_update(event):
    label = event.currentTarget.nextElementSibling
    label.innerText = event.currentTarget.value
    plot_waveform()

    waveform = band_limited_noise()
    updateAudio(waveform) 

def plot_waveform():
    frequency1 = float(range1.value)
    frequency2 = float(range2.value)

    waveform = wave(frequency1)(time) + wave(frequency2)(time)
    updateChart(to_js(time), to_js(waveform))

    waveform = band_limited_noise()
    updateAudio(waveform) 


proxy = create_proxy(on_range_update)
range1.addEventListener("input", proxy)
range2.addEventListener("input", proxy)

plot_waveform()