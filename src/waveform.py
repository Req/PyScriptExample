
import numpy as np
#from scipy import stats
#from scipy.io import wavfile
from functools import reduce


def band_limited_noise(mid_freq, width_freq, samplerate=44100, duration=1):
    """Create the band limited noise.
    """
    freqs = []
    for index in range(1000):
        f = np.random.normal(mid_freq, width_freq)
        freqs.append(f)

    time_vector = np.linspace(0, duration, duration * samplerate)

    phases = np.random.rand(len(freqs))*2*np.pi
    signals = [np.sin(2*np.pi*freq*time_vector + phase) for freq,phase in zip(freqs,phases)]
    signal = reduce(lambda a,b: a+b,signals)
    signal /= np.max(signal)
    return signal


def save_waveform(wave, samplerate, filename="test.wav"):
    """Saves waveform as WAV.
    """
    from scipy.io import wavfile
    x = np.int16(wave * (2**15 - 1))
    wavfile.write(filename, samplerate, x)


if __name__ == "__main__":
    samplerate = 44100
    wave = band_limited_noise(mid_freq = 3000, width_freq = 4, samplerate=samplerate, duration=2)
    save_waveform(wave, samplerate)
