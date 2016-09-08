#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

SphinxOn = True
WitOn = True
ApiOn = True
IBMOn = True
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

with open("microphone-results.wav", "wb") as f:
    print("writing,wait...")
    f.write(audio.get_wav_data())

if SphinxOn:
	# recognize speech using Sphinx
	try:
		print("Sphinx thinks you said " + r.recognize_sphinx(audio))
	except sr.UnknownValueError:
		print("Sphinx could not understand audio")
	except sr.RequestError as e:
		print("Sphinx error; {0}".format(e))
if WitOn:
	# recognize speech using Wit.ai
	WIT_AI_KEY = "G4R357JHVZI2B62KG7VFVZAKJPMHVBWW" # Wit.ai keys are 32-character uppercase alphanumeric strings
	try:
		print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
	except sr.UnknownValueError:
		print("Wit.ai could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Wit.ai service; {0}".format(e))

if ApiOn:
	# recognize speech using api.ai
	API_AI_CLIENT_ACCESS_TOKEN = "851d755279ef40fcb7394fd5e058fe9b" # api.ai keys are 32-character lowercase hexadecimal strings
	try:
		print("api.ai thinks you said " + r.recognize_api(audio, client_access_token=API_AI_CLIENT_ACCESS_TOKEN))
	except sr.UnknownValueError:
		print("api.ai could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from api.ai service; {0}".format(e))
if IBMOn:		
# recognize speech using IBM
	try:
		import os
		cmd = 'curl -X POST -u "913b7804-d0d0-4dc5-8b42-32da7e5e3046":"Upi2DwkrWPQR" --header "Content-Type: audio/wav" --data-binary @microphone-results.wav "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?model=en-UK_BroadbandModel"'
		a  = str(os.popen(cmd).readlines())	
		begin = a.find("transcript")+14
		end = a.find('"',begin+1)	
		result = "IBM : "+a[begin:end]+"\n"
		print(result)
	except sr.RequestError as e:
		print("Sphinx error; {0}".format(e))
