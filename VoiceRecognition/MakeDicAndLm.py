print "======  lm \n"

content = "\\data\\\n"


word = ["CLOSE","DOOR","OPEN","WINDOW"]

S1 =0
S2 =0
if len(word)==2 :
	S1 = -1.0792
	S2 = -0.6021
if len(word)==3 :
	S1 =-1.2553
	S2 =-0.9031	
if len(word)==4 :
	S1 =-1.3802
	S2 =-0.9031	
if len(word)==5 :
	S1 =-1.4771
	S2 =-1.0000	
if len(word)==6 :
	S1 =-1.5563
	S2 =-1.0792	
if len(word)==7 :
	S1 =-1.6232
	S2 =-1.1461	

content += "ngram 1="
content += str(len(word)+2)
content +="\nngram 2="
content += str(len(word)*2)
content +="\nngram 3="
content += str(len(word))
content +="\n\n"

content +="\\1-grams:\n"
content +="-0.7782 </s> -0.3010\n"
content +="-0.7782 <s> -0.2218\n"
for index in word:
	content += str(S1)	
	content +=" "+index
	content +=" -0.2218\n"

content +="\n\\2-grams:\n"
for index in word:
	content += str(S2)	
	content +=" <s> "+index
	content +=" 0.0000\n"
for index in word:
	content +="-0.3010"	
	content +=" "+index
	content +=" </s> -0.3010\n"

content +="\n\\3-grams:\n"
for index in word:
	content +="-0.3010 <s>"	
	content +=" "+index
	content +=" </s>\n"
content +="\n\\end\\"





print content

print "\n======\n"

FileText = open("sample.lm","w")
FileText.write(content)
FileText.close()
content = ""
print "======  dic"
for i in word:
	with open("Alldic.txt") as f:
		for data in f.readlines():
			index=""
			if data.find("(")!=-1:
				index = data[data.find("("):data.find(")")+1]
				data = data[0:data.find("(")]+data[data.find(" "):]				
			if data[0:data.find(" ")] == str(i.lower()):
				if index != None:
					data = data[:data.find(" ")]+index+data[data.find(" "):] 
				print data.upper().replace("\n","")
				content += data.upper().replace("\n","")+"\n"
FileText = open("sample.dic","w")
FileText.write(content)
FileText.close()
