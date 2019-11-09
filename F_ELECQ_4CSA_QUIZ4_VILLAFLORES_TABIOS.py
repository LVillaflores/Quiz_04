import speech_recognition as sr

r = sr.Recognizer()

audio = '5_person.wav'

with sr.AudioFile(audio) as source:
	audio = r.record(source)
	print('Processing')

try:
	value = r.recognize_google(audio)
	file = open("5P.txt", "a")
	file.write(value)
	print('Finished Processing')
	print(value)

except Exception as e:
	print(e)
