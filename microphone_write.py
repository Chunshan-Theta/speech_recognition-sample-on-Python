#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
    print("Say something!")
    audio = r.listen(source)

with open("microphone-write-results.wav", "wb") as f:
    print("writing,wait...")
    f.write(audio.get_wav_data())


print("Complete, File name is microphone-write-results.wav")



