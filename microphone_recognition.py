#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source) # listen for 1 second to calibrate the energy threshold for ambient noise levels
    print("Say something!")
    audio = r.listen(source)

with open("microphone-results.wav", "wb") as f:
    print("writing,wait...")
    f.write(audio.get_wav_data())


print("recognizing,wait...")

OutputReult=""
# recognize speech using IBM
print("Wait IBM Result...")
try:
	import os
	cmd = 'curl -X POST -u "913b7804-d0d0-4dc5-8b42-32da7e5e3046":"Upi2DwkrWPQR" --header "Content-Type: audio/wav" --data-binary @microphone-results.wav "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?model=en-UK_BroadbandModel"'
	a  = str(os.popen(cmd).readlines())
	
	begin = a.find("transcript")+14
	end = a.find('"',begin+1)

	#print "IBM : "+a[begin:end]
	result = "IBM : "+a[begin:end]+"\n"
	OutputReult+=result
except sr.RequestError as e:
    	print("Sphinx error; {0}".format(e))



# recognize speech using Sphinx
print("Wait Sphinx Result...")
try:
    #print("Sphinx(offline) : " + r.recognize_sphinx(audio))
    result = "Sphinx(offline) : " + r.recognize_sphinx(audio)+"\n"
    OutputReult+=result
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))




# recognize speech using api.ai
print("Wait api.ai Result...")
API_AI_CLIENT_ACCESS_TOKEN = "851d755279ef40fcb7394fd5e058fe9b" # api.ai keys are 32-character lowercase hexadecimal strings
try:
    #print("api.ai : " + r.recognize_api(audio, client_access_token=API_AI_CLIENT_ACCESS_TOKEN))
    result = "api.ai : " + r.recognize_api(audio, client_access_token=API_AI_CLIENT_ACCESS_TOKEN)+"\n"
    OutputReult+=result
except sr.UnknownValueError:
    print("api.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from api.ai service; {0}".format(e))


# recognize speech using Wit.ai
print("Wait Wit.ai Result...")
WIT_AI_KEY = "G4R357JHVZI2B62KG7VFVZAKJPMHVBWW" # Wit.ai keys are 32-character uppercase alphanumeric strings
try:
    #print("Wit.ai(Free): " + r.recognize_wit(audio, key=WIT_AI_KEY))
    result = "Wit.ai(Free): " + r.recognize_wit(audio, key=WIT_AI_KEY)+"\n"
    OutputReult+=result
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))


print("Result -----------------")
print(OutputReult)

