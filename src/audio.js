// src/audio.js
let initialized = false
let audioCtx, gain, oscillator

function init() {
  audioCtx = new AudioContext({
    latencyHint: "interactive",
    sampleRate: 44100,
  })

  gain = audioCtx.createGain() // Controls volume
  oscillator = audioCtx.createOscillator() // Controls frequency

  gain.connect(audioCtx.destination) // connect gain node to speakers
  gain.gain.value = 0.02 // ☠🕱☠ CAREFUL WITH VOLUME ☠🕱☠

  oscillator.connect(gain) // connect oscillator to gain
  oscillator.start()
}

function updateAudio(waveform) {
  if (!initialized) {
    initialized = true
    init()
  }

  // See output of this Log!
  /*
  Waveform is "Proxy", not an array
  I don't grok PyScript so I don't know what that means
  You need to give an array of floats and then convert that like in my example in SO
  const sineTerms = new Float32Array(waveform)
  const cosineTerms = new Float32Array(sineTerms.length)
  const customWaveform = audioContext.createPeriodicWave(cosineTerms, sineTerms)
  return customWaveform
  */
  console.log("123", waveform)

  try {
    oscillator.setPeriodicWave(waveform)
  }catch(e) {
    console.error("WTF", e)
  }
}
