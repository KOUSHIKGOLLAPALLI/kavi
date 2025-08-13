import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print(f"Kavi 🗣️: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    try:
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎤 Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        query = r.recognize_google(audio)
        print(f"You 🧑: {query}")
        return query.lower()
    except Exception as e:
        print(f"[Voice Error] {e}")
        return input("⌨ Type your command: ").lower()
