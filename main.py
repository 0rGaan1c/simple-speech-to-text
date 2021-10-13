import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Adusting for Ambient Noise ")
    r.adjust_for_ambient_noise(source, duration=1)

    try:
        duration = int(input("Recording duration(in seconds): "))
    except:
        print("Duration must be an integer.")
        exit(0)

    print(f"Recording for {duration} seconds")
    audio = r.listen(source, timeout=duration)
    print("Done recording")
    

try:
    print("\nText: " + r.recognize_google(audio))
except:
    print("Sorry, I did not understood that.")