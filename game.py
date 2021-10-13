import speech_recognition as sr

r = sr.Recognizer()

def speak():
	with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source)
			print("\nSpeak: Left or Right?")
			audio = r.listen(source, 2);
			
	try:
			print("You said: " + r.recognize_google(audio))
			return r.recognize_google(audio)
	except:
			print("Sorry, I did not understood that.")


print("\nClear the maze without falling into the Abyss.")

isGameOver = False
win = False

right = 0
left = 0
while (not isGameOver):
	ans = speak()
	if (ans == "left"):
		left +=1
		if (left == 3):
			print("\nYou win!, not that it matters.")
			isGameOver = True
	elif (ans == "right"):
		right += 1
		if (right == 2):
			print("\nRIP Game Over, You fall into the Abyss!")
			exit(0)
		continue;