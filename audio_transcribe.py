#!/usr/bin/env python3

import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path

FileName = "ex4.wav"
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), FileName)
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
#AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

# use the audio file as the audio source
r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source) # read the entire audio file

################recognize

'''
# recognize speech using IBM Speech to Text
IBM_USERNAME = "93a4c552-8254-47e0-ad4f-86fb78410e29" # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
IBM_PASSWORD = "vBYojbSRHujD" # IBM Speech to Text passwords are mixed-case alphanumeric strings
try:
    print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM Speech to Text service; {0}".format(e))

'''
# recognize speech using IBM
import os
cmd = 'curl -X POST -u "913b7804-d0d0-4dc5-8b42-32da7e5e3046":"Upi2DwkrWPQR" --header "Content-Type: audio/wav" --data-binary @'+FileName+' "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?model=en-UK_BroadbandModel"'
a  = str(os.popen(cmd).readlines())
begin = a.find("transcript")+14
end = a.find('"',begin+1)
print "IBM : "+a[begin:end]


# recognize speech using Sphinx
try:
    print("Sphinx(offline) : " + r.recognize_sphinx(audio))
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))




# recognize speech using api.ai
API_AI_CLIENT_ACCESS_TOKEN = "851d755279ef40fcb7394fd5e058fe9b" # api.ai keys are 32-character lowercase hexadecimal strings
try:
    print("api.ai : " + r.recognize_api(audio, client_access_token=API_AI_CLIENT_ACCESS_TOKEN))
except sr.UnknownValueError:
    print("api.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from api.ai service; {0}".format(e))


# recognize speech using Wit.ai
WIT_AI_KEY = "G4R357JHVZI2B62KG7VFVZAKJPMHVBWW" # Wit.ai keys are 32-character uppercase alphanumeric strings
try:
    print("Wit.ai(Free): " + r.recognize_wit(audio, key=WIT_AI_KEY))
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))





