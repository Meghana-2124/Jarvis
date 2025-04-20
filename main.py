import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
from plyer import notification
import pyautogui
import wikipedia
import pywhatkit as pwk

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate",150)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def command():
    content = " "
    while content == " ":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            content = r.recognize_google(audio, language='en-in')
            print("Processing please wait......" + content)
        except Exception as e:
            print("Please try again....")
            return ""
    return content

def main_process():
    while True:
        request = command().lower()
        if "stop" in request or "exit" in request:
            speak("Goodbye!")
            break
        if "hello" in request:
            speak("Welcome, how can I help you")
        elif "play music" in request:
            speak("playing music")
            song = random.randint(1,3)
            if song == 1:
                webbrowser.open("https://www.youtube.com/watch?v=pytdWKT-NV4")
            elif song == 2:
                webbrowser.open("https://www.youtube.com/watch?v=qg89z5xMyTU")
            elif song == 3:
                webbrowser.open("https://www.youtube.com/watch?v=HTeP7ja9UFY")
        elif "tell me the time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("The current time is: " + str(now_time))
        elif "which day is today" in request:
            now_day = datetime.datetime.now().strftime("%A")
            speak("Today is: " + str(now_day))
        elif "new task" in request:
            task = request.replace("new task", "")
            task = task.strip()
            if task != "":
                speak("Adding task : "+ task)
                with open ("todo.txt", "a") as file:
                    file.write(task + "\n")
        elif "speak task" in request:
            with open ("todo.txt", "r") as file:
                speak("Work we have to do today is : "+ file.read())
        elif "show notification" in request:
             with open ("todo.txt", "r") as file:
                  tasks =  file.read()
             notification.notify(
                 title = " Today's work",
                 message = tasks
             )
        elif "open you tube" in request:
            webbrowser.open("www.youtube.com")
        elif "open" in request:
            query = request.replace("open", "")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("Enter")
        elif "wikipedia" in request:
            request = request.replace("jarvis", "")
            request = request.replace("search wikipedia", "")
            result = wikipedia.summary(request, sentences= 2)
            print(result)
            speak(result)
        elif "search google" in request:
            request = request.replace("jarvis", "")
            request = request.replace("search google", "")
            webbrowser.open("https://www.google.com/search?q="+request)
        elif "send whatsapp" in request:
            pwk.sendwhatmsg("+91 89XXXXXXXX", "Hi, how r u?", 16,21,30)
        elif "meal plan" in request:
            meal = request.replace("meal plan", "")
            meal = meal.strip()
            if meal != "":
                speak("ok next "+ meal)
                with open ("meal_plan.txt", "a") as file:
                    file.write(meal+ "\n")
        elif "speak meal" in request:
            with open ("meal_plan.txt", "r") as file:
                speak("meal we have to cook today is : "+ file.read())


main_process()

