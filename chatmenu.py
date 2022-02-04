import speech_recognition as sr
from tkinter import *
from os import system as s
from pyttsx3 import speak as sp

def _open():
    a=sr.Recognizer()

    while True:
        with sr.Microphone() as src:
            print("Microphone listening......")
            audio=a.listen(src)
            query = a.recognize_google(audio,language='en-in')
            print(f"User said : {query} ")
            sp(f"Wait for second...opening")
            
        while True:

            if "Notepad" in query and "open"  in query:
                s("notepad")
                break;
            elif "Paint"  in query and "open" in query:
                s("mspaint")
                break;
            elif "Chrome"  in query and "open" in query:
                s("start chrome")
                break;
            elif "drive"  in query and "open"  in query:
                s("start chrome drive.google.com")
                break;
            elif "Word"  in query and "open"  in query:
                s("start winword")
                break;
            elif "Wordpad"  in query and "open"  in query:
                s("start wordpad")
                break;
            elif "file explorer"  in query and "open"  in query:
                s("start explorer")
                break;
            elif "spotify"  in query and "open"  in query:
                s("spotify")
                break;
            elif "jupyter notebook"  in query and "open"  in query:
                s("jupyter notebook")
                break;
            else:
                sp("I don't understand")
                break;
            
        break;
            
root=Tk()

l1 = Label(root,text="Welcome to GUI Chat Menu",font="CourierNew 24 bold",
          fg="yellow",bg="black")
l1.pack()

b1 = Button(root,text="Input",font="CourierNew 24 bold",
           relief=RAISED,fg="green",bg="black",width=10,command=_open)
b1.pack(pady=5)

b2 = Button(root,text="Exit",font="CourierNew 24 bold",
           relief=RAISED,fg="gray",bg="black",width=10,command=root.destroy)
b2.pack(pady=5)

root.mainloop()