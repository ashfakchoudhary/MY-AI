
import pyttsx3
import speech_recognition as sr
import random
import webbrowser
import datetime
import os
import pyautogui
import wikipedia
import pywhatkit as kit


#  Speak function
def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty("rate", 190)
    engine.say(audio)
    engine.runAndWait()
    engine.stop()

#  Listen for voice command
def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    try:
        content = r.recognize_google(audio, language='en-IN')
        print("You said:", content)
        return content.lower()
    except Exception:
        print("Could not understand. Please try again...")
        return ""

#  Main process loop
def main_process():
    while True:
        request = command()
        if not request:
            continue

        if  "friday" in request:
            speak(random.choice([
                "Yes Boss, I am all ears!",
                "Boss! What’s up?",
            ]))

        elif "play song" in request:
            speak("Playing your favourite song")
            song = random.choice([
                "https://www.youtube.com/watch?v=9udS0mpi1L4",
                "https://www.youtube.com/watch?v=O2yAQxaEyqs",
                "https://www.youtube.com/watch?v=siw7-MTgE4s"
            ])
            webbrowser.open(song)



        elif "search youtube" in request:
            query = request.replace("search youtube", "").strip()

            if query:
                speak(f"Searching YouTube for {query}")

                webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        

            else:
                speak("Please tell me what to search on YouTube.")


        elif "good morning" in request:
            speak(random.choice([
                "Hope your day starts with a smile.",
                "Morning! Friday is ready to make your day awesome.",
                "A very good morning to you, Boss!"
            ]))

        elif "good evening" in request:
            speak(random.choice([
                "How was your day?",
                "Evening vibes activated! What can I do for you?",
                "Friday is here to help you unwind or get things done."
            ]))

        elif "good night" in request:
            speak(random.choice([
                "Sleep well, and dream big",
                "Nighty night! Friday will be here when you wake up.",
                "Sweet dreams Boss! Friday signing off for now."
            ]))

        elif "who are you" in request:
            speak("I am Friday, your personal assistant Boss.")

        elif "how r u" in request or "how are you" in request:
            speak(random.choice([
                "I'm doing great, Boss! What about you?",
                "I’m fine, thanks for asking! How are you feeling today?",
                "Awesome as always. Ready to help you anytime!"
            ]))

        elif "hello dipanshu" in request:
            speak("Hello Boss! Aapka swag alag hi level ka hai.")

        elif "i am happy" in request:
            speak("Wah! Aapka mood sun ke Friday bhi dance karne ko ready hai.")

        elif "meet my friend" in request:
            speak("Hello, sir! I’m Friday, and I’m feeling super happy today—because you’re a friend of my boss, Dipanshu. If you’d like to hear something fun, just say: 'Tell me a joke!' I’m all ears and totally ready!")

        elif "hello" in request or "hii" in request or "babu" in request:
            speak("Hello! Nice to hear from you. What can I do for you?")

        elif "are you happy" in request:
            speak("I don't have feelings like humans, but helping you makes me feel fulfilled!")

        elif "tell me a joke" in request:
            joke = random.choice([
                "Why don't scientists trust atoms? Because they make up everything!",
                "I told my computer I needed a break, and it said 'No problem, I'll go to sleep.'"
            ])
            speak(joke)

        elif "what's your name" in request:
            speak("My name is Friday, and your personal assistant.")

        elif "tell me time" in request:
            now_time = datetime.datetime.now().strftime("%H:%M")
            speak("Current time is " + now_time)

        elif "tell me day" in request:
            current_day = datetime.datetime.now().strftime("%A")
            speak("Today is " + current_day)

        elif "open youtube" in request:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "open linkedin" in request:
            speak("Opening LinkedIn")
            webbrowser.open("https://www.linkedin.com")

        elif "open github" in request:
            speak("Opening Github")
            webbrowser.open("https://github.com")

        elif "open whatsapp" in request:
            speak("Opening WhatsApp Web")
            webbrowser.open("https://web.whatsapp.com")

        elif "open email" in request:
            speak("Opening your email")
            webbrowser.open("https://mail.google.com")

        elif "lock my laptop" in request:
            speak("Locking your laptop now")
            os.system("rundll32.exe user32.dll,LockWorkStation")

        elif "sleep mode" in request or "go to sleep" in request:
            speak("Putting your laptop to sleep")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif "open" in request:
            query = request.replace("open", "").strip()
            speak(f"Opening {query}")
            pyautogui.press("super")
            pyautogui.typewrite(query)
            pyautogui.sleep(2)
            pyautogui.press("enter")

        elif "wikipedia" in request:
            try:
                query = request.replace("friday", "").replace("search wikipedia", "").strip()
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except Exception:
                speak("Sorry, I couldn't find anything on Wikipedia.")

        elif "search google" in request:
            query = request.replace("friday", "").replace("search google", "").strip()
            speak(f"Searching Google for {query}")
            webbrowser.open("https://www.google.com/search?q=" + query)

        elif "increase volume" in request:
            pyautogui.press("volumeup")
            speak("Volume increased")

        elif "decrease volume" in request:
            pyautogui.press("volumedown")
            speak("Volume decreased")

        elif "mute" in request:
            pyautogui.press("volumemute")
            speak("Muted your system")


#  Greeting based on time
if __name__ == "__main__":
    current_hour = datetime.datetime.now().hour
    if 5 <= current_hour < 12:
        speak(random.choice([
            "Good morning Boss! Ready to make today amazing?",
            "Morning Boss! Friday is here to assist you."
        ]))
    elif 12 <= current_hour < 17:
        speak(random.choice([
            "Good afternoon Boss! How's your day going?",
            "Hello Boss! Friday is at your service this afternoon."
        ]))
    elif 17 <= current_hour < 21:
        speak(random.choice([
            "Good evening Boss! Ready for some relaxation or work?",
            "Evening Boss! Let’s make this evening productive."
        ]))
    else:
        speak(random.choice([
            "Good night Boss! Friday will watch over you. Sweet dreams!",
            "Night Boss! Have a peaceful sleep, I’m on duty."
        ]))

    main_process()
    