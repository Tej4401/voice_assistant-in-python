import pyttsx3,datetime,wikipedia,webbrowser,subprocess,smtplib
import speech_recognition as sr
def send_mail(send_email, password, message,rec_mail):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(send_email, password)
    server.sendmail(send_email, rec_email, message)
    server.quit()
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
    elif query=="open youtube":
        chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab("https://youtube.com")
    elif query=="open google":
        chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab("https://google.com")
    elif query=="open facebook":
        chrome_path="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
        webbrowser.get('chrome').open_new_tab("https://facebook.com")
    elif query=="execute":
        speak("enter your command")
        command=takecommand().lower()
        print(subprocess.check_output(command,shell=True))
    elif query=="send mail":
        speak("please enter recipient mail")
        rec=takecommand()
        speak("enter your message")
        msg = takecommand()
        send_mail("tej4april@gmail.com", "thisismypassword123456noneofyourbusiness7890", msg,rec)
