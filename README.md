speech Recognition

***system :ubuntu 14
***python version : 2.7
***speech_recognition source code is from https://github.com/Uberi/speech_recognition.git

***Installed command:
(1)sudo apt-get install -y python python-dev python-pip build-essential swig git
(2)sudo apt-get install libpulse-dev
(3)sudo pip install pocketsphinx
(4)cd speech_recognition
(5)sudo python setup.py install
(6)sudo apt-get install portaudio19-dev
(7)sudo pip install pyaudio
(8)sudo apt-get install curl



***Quick start command :python ./speech_recognition/examples/microphone_recognition.py	
	
***Sphinx voice recognition is offline,could decrease volume of dictionary to upper recognition success.
	
	(1) First,run 'MakeDicAndLm.py'
	
	(2) would create 'sample.dic' and 'sample.lm' file
		*default recognizable word: "CLOSE","DOOR","OPEN","WINDOW"，could edit MakeDicAndLm.py to change recognitzing word,recommend volume of dictionary is 2-5.
		*recognizable word can't over seven words,MUST insert by uppercase and letter order
	
	(3) create new dictionary for Sphinx 

		3.1	
			sudo chmod 777 /usr/local/lib/python2.7/dist-packages/speech_recognition/pocketsphinx-data/en-US/
		3.2 
			move 'sample.dic' and'sample.lm' file to "/usr/local/lib/python2.7/dist-packages/speech_recognition/pocketsphinx-data/en-US/" directory
	
	(4) replace dictionary of Sphinx  

		4.1
			sudo chown -R ts /usr/local/lib/python2.7/dist-packages/speech_recognition/__init__.py
		4.2
			replace word of "/usr/local/lib/python2.7/dist-packages/speech_recognition/__init__.py"
			language-model.lm.bin -> sample.lm
			pronounciation-dictionary.dict -> sample.dic
	
		
		
		
	

============

Speech recognition module for Python : https://github.com/Uberi/speech_recognition

IBM Speech to Text:http://www.ibm.com/watson/developercloud/speech-to-text.html

IBM speech-to-text-demo.mybluemix.net:https://speech-to-text-demo.mybluemix.net/

IBM Speech to Text : https://console.ng.bluemix.net/catalog/services/speech-to-text

IBM developercloud Docs:http://www.ibm.com/watson/developercloud/speech-to-text/api/v1/?curl#recognize_sessionless_nonmp12

wit.ai : https://wit.ai/docs/quickstart

api.ai : https://api.ai/

api-ai-python : https://github.com/api-ai/api-ai-python

使用python和IBM speech to text 进行 语音识别:http://blog.csdn.net/tang20120235/article/details/49762421

