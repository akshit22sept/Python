import speech_recognition as sr
import pyttsx3
import webbrowser
import smtplib
import os
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()




def note():
    os.startfile('notepad.exe')
    speak("Opening NotePad")


def google():
    webbrowser.open('https://www.google.com/')
    speak("Opening Google")


def youtube():
    webbrowser.open('https://www.youtube.com/')
    speak("Opening Youtube")


def amazon():
    webbrowser.open('https://www.amazon.in/')
    speak("Opening Amazon")




said = ''


def get_audio():
    global said
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print(e)
    return said.lower()


while True:
    text = get_audio()
    if 'alexander' in text:
        speak('yes sir ready for duty ')
        speak('sorry for hibernating ')
    if ('how are you' in text or 'what about you' in text):
        speak('Amazin')
        speak('how are you my master')
        text = get_audio()
        speak('have a great day')
    elif ('why' in text and 'time' in text) or ('why' in text and 'making' in text):
        speak('To save dinosaurs from their extinction')
    elif 'hello' in text or 'hi' in text:
        speak('Hello there, How are you')
        text = get_audio()
        if ('how are you' in text or 'what about you' in text) and (
                'good' in text or 'great' in text or 'Amazing' in text):
            speak('Amazin ready to create a time machine')
        if 'good' in text or 'great' in text or 'Amazing' in text and not 'what about you' in text:
            speak('Have a Great day')
        elif 'bad' in text or 'not very well' in text or 'not good' in text:
            speak('Hope every thing gets better soon')
        elif 'what about you' in text:
            speak('Great')
        else:
            speak('Have a great day')
    elif 'what are you doing' in text:
        speak('getting ready to make my time machine')
    elif'what is your name' in text:
        speak('My name is Alexander')
    elif'open' in text:
        if 'google' in text:
            google()

        elif 'youtube' in text:
            youtube()

        elif 'amazon' in text:
            amazon()

        elif 'notepad' in text:
            note()
        elif 'open gmail' in text:
            speak('User number')
            e = input('User no. :  ')
            webbrowser.open(f'https://mail.google.com/mail/u/{e}/#inbox')

            speak("opening your gmail master")
        elif 'excel' in text:
            speak('Openning Excel')
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Excel 2007')
        elif 'word' in text:
            speak('Openning Word')
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007')
        elif 'access' in text:
            speak('Openning Access')
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Access 2007')
        elif 'powerpoint' in text:
            speak('Openning Powerpoint')
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Powerpoint 2007')
        elif 'office' in text:
            speak('Openning Powerpoint')
            os.startfile(
                'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Powerpoint 2007')
            speak('Openning Access')
            os.startfile(
                'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Access 2007')
            speak('Openning Word')
            os.startfile(
                'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Word 2007')
            speak('Openning Excel')
            os.startfile(
                'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\Microsoft Office Excel 2007')

        else:
            speak('Sorry, I didnt Understand that')
    elif'bye' in text:
        speak('Bye')
        break
    elif'search for' in text:
        e = text.replace('search for', '')
        speak(f"searching for{e}")
        webbrowser.open(f'https://www.google.com/search?q={e}')

    elif'send mail' in text:
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login('example@gmail.com', 'Password')

            print('Enter the Mail ID :  ')
            q = input()


            speak("Message")
            text = get_audio()
            print("Do you want to send this message ? y/n  ")
            h = get_audio()
            if h != 'no':

                server.sendmail("example@gmail.com", f"{q}", f"{text}")

            else:
                speak('Do you still want to Speak The Message ')
                z = get_audio()
                while z != 'no':
                    speak("The Message")
                    print("Message :")
                    text = get_audio()
                    speak("Do you want to send this message ? y/n  ")
                    print("Do you want to send this message ? y/n  ")
                    h = get_audio()
                    if h != 'no':
                        server.sendmail("example@gmail.com", f"{q}", f"{text}")
                        server.quit()
                        speak("sent")
                        print('sent')
                        break

                    else:
                        speak('Do you still want to Speak The Message ')
                        z = get_audio()
                if z == 'no':
                    g = input("Message :  ")
                    server.sendmail("example22sept@gmail.com", f"{q}", f"{g}")
                    server.quit()
                    speak("sent")
                    print('sent')


        except:
            pass
    elif 'login' in text:
        speak('logging in')


