import pyttsx3,datetime,wikipedia
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning tej")
    elif hour>=12 and hour<18:
        speak("good afternoon tej")
    else:
        speak("good night tej")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 4000
        r.pause_threshold = 0.5
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User Said : " + query)
    except Exception as e:
        print("Please Speak Again(try speaking louder)")    
        return "none"  
    return query
wishme()
while True:
    query = takecommand().lower()
    if query=="search wikipedia":
        speak('what do you want to search')
        topic = takecommand().lower()
        print('Searching Wikipedia...')
        speak('Searching Wikipedia')
        results = wikipedia.summary(topic, sentences=2)
        speak("Accoring to Wikipedia")
        print(results)
        speak(results)