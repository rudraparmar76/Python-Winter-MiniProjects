import pyttsx3

print("----------- Welcome to RoboSpeaker 1.1 - Created By Rudra -----------".center(80))

def speak_in_voice(engine):
    voice_id = int(input("- Press 1 for Female Voice and 0 for Male Voice:"))
    if(voice_id == 0):
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice_id].id)

        engine.say(f"You have choosen {voice_id} which is Male Voice. ")
        engine.runAndWait()
    elif(voice_id == 1):
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[voice_id].id)

        engine.say(f"You have choosen {voice_id} which is Female Voice. ")
        engine.runAndWait()
    else:
        engine.say("Error ! Enter a valid Number.")
        engine.runAndWait()
        speak_in_voice(engine)

def say_goodBye(engine):
    engine.say("Thank you for using RoboSpeaker 1.1. Exiting the program.")
    engine.runAndWait()

engine = pyttsx3.init()

speak_in_voice(engine)

while True:

    x = input("- Enter what you want me to speak or else press q to exit: ")

    rate = engine.getProperty('rate')
    engine.setProperty('rate',rate+8)

    if x.lower() == "q":
        say_goodBye(engine)
        break

    engine.say(x)
    engine.runAndWait()

