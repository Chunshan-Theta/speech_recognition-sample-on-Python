import os
cmd = 'curl -X POST -u "913b7804-d0d0-4dc5-8b42-32da7e5e3046":"Upi2DwkrWPQR" --header "Content-Type: audio/wav" --data-binary @ex1.wav "https://stream.watsonplatform.net/speech-to-text/api/v1/recognize?model=en-UK_BroadbandModel"'
a  = str(os.popen(cmd).readlines())
begin = a.find("transcript")+14
end = a.find('"',b+1)
print "result : "+a[begin:end]
