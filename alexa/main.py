import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
def talk(text):
    engine.say('text')
    engine.say('What can I do for you')
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                engine.say(command)
                engine.runAndWait()
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %P')
        print(time)
        talk('current time is'+time)
    elif 'who the hack is' in command:
        person = command.replase('who the hack is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('Sorry ,I have a headache')
    elif 'Are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'Joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Please say the command again.')
while True:
    run_alexa()
