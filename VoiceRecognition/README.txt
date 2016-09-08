speech Recognition

Installed:
(1)sudo apt-get install -y python python-dev python-pip build-essential swig git
(2)sudo apt-get install libpulse-dev
(3)sudo pip install pocketsphinx
(4)git clone https://github.com/Uberi/speech_recognition.git
(5)cd speech_recognition
(6)sudo python setup.py install
(7)sudo apt-get install portaudio19-dev
(8)sudo pip install pyaudio
(9)sudo apt-get install curl



Quick start:

(1) 設定資料 
	1.1 打開 ./speech_recognition/examples/microphone_recognition.py
	
	1.2 用#號註解掉不用的語音辨識，留下 Sphinx、Wit.ai、api.ai,並將TOKEN補上
		1.2.1
			(1)api.ai的TOKEN sample: 851d755279ef40fcb7394fd5e058fe9b
			(2)WIT.AI的KEY sample: G4R357JHVZI2B62KG7VFVZAKJPMHVBWW
			(3)其中的 Sphinx 語音辨識是離線辨識
	
	1.3 IBM語音辨識建議改用
		
		1.3.1 補音源輸出在 麥克風輸入後 (11行)
		with open("microphone-results.wav", "wb") as f:
			print("writing,wait...")
			f.write(audio.get_wav_data())
		
		1.3.2 補上IBM 與音辨識 (補在最後)
		try:
			import os
			cmd = 'curl -X POST -u "913b7804-d0d0-4dc5-8b42-32da7e5e3046":"Upi2DwkrWPQR" --header "Content-Type: audio/wav" --data-binary @microphone-results.wav "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?model=en-UK_BroadbandModel"'
			a  = str(os.popen(cmd).readlines())	
			begin = a.find("transcript")+14
			end = a.find('"',begin+1)	
			result = "IBM : "+a[begin:end]+"\n"
			OutputReult+=result
		except sr.RequestError as e:
			print("Sphinx error; {0}".format(e))
	
	1.4 run 
	
	
other	
	其中的 Sphinx 語音辨識是離線辨識,可利用減少辨識文字量
	(1) run MakeDicAndLm.py
	(2) 會產出 sample.dic,sample.lm
	(3) 
		3.1	
			sudo chmod 777 /usr/local/lib/python2.7/dist-packages/speech_recognition/pocketsphinx-data/en-US/
		3.2 
			放到 /usr/local/lib/python2.7/dist-packages/speech_recognition/pocketsphinx-data/en-US/
	(4) 
		4.1
			sudo chown -R ts /usr/local/lib/python2.7/dist-packages/speech_recognition/__init__.py
		4.2
			修正 /usr/local/lib/python2.7/dist-packages/speech_recognition/__init__.py中
			language-model.lm.bin -> sample.lm
			pronounciation-dictionary.dict -> sample.dic
		
		
		
	