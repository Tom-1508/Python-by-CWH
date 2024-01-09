import win32com.client as wincom

print("Welcome to RoboSpeaker. built by Tamal")
speak = wincom.Dispatch("SAPI.SpVoice")

while(True):
    text = input("Enter what you want me to say: ")
    if(text == 'q'):
        break
    else:
       speak.Speak(text)
