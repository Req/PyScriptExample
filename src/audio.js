// src/audio.js

const audioCtx = new AudioContext({
  latencyHint: "interactive",
  sampleRate: 4410,
});


gain = audioCtx.createGain() // Controls volume
oscillator = audioCtx.createOscillator() // Controls frequency

gain.connect(audioCtx.destination) // connect gain node to speakers

oscillator.connect(gain) // connect oscillator to gain
oscillator.start()


function updateAudio(waveform) {
  oscillator.setPeriodicWave(waveform)
  gain.gain.value = 0.02 // ☠🕱☠ CAREFUL WITH VOLUME ☠🕱☠
}