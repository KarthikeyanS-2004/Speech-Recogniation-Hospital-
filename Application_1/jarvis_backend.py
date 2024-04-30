import pyttsx3 
import speech_recognition as sr
import datetime
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Spartan's Jarvis Sir. Please tell me how may I help you?")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:  
        print("Say that again please...") 
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
        elif 'gynecologist' in query or 'women specialist' in query:
            speak("Doctor.Geetha")
            print("Dr.Geetha")
            speak("she is in the Ground floor room number:106")
            print("She is in the Ground Floor\nRoom No:106")
            speak('Timing:10:30am to 12:00pm')
            print("Timing:10:30am to 12:00pm")
            speak("contact number is 9751503202")
            print("Contact No:9751503202")
            
        elif 'dermatologist' in query or 'skin specialist' in query:
            speak("doctor.david colbert")
            print("Dr.David Colbert")
            speak("he is in the ground floor, room numner:104")
            print("He is in the Ground Floor\nRoom No:104")
            speak("timing:11:00am to 12:30pm")
            print("Timing:11:00am-12:30pm")
            speak("contact number is 9751503202")
            print("Contact No:9751503202")
        
        elif'cardiologist' in query or 'heart specialist' in query:
            speak("doctor salim yusuf")
            print("Dr.Salim Yusuf")
            speak("he is in the ground floor right to the reception, room number:105")
            print("He is in the Ground Floor,right to the Reception\nRoom No:105")
            speak("timing:10:00am to 11:30am")
            print("Timing:10:00am-11:30am")
            speak("contact number is 9751503202")
            print("Contact No:9751503202")

        elif'oncologist' in query or 'cancer specialist' in query:
            speak("doctor ashok vaid")
            print("Dr.Ashok Vaid")
            speak("he is in the ground floor room number:103")
            print("He is in the Ground Floor\nRoom No:103")
            speak("timing:1:30pm to 2:30pm")
            print("Timing:1:30pm-2:30pm")
            speak("contact number is 9751503202")
            print("Contact No:9751503202")

        elif'neurologist' in query or 'brain' in query or 'nerv' in query:
            speak("doctor mukul verma")
            print("Dr.Mukul Verma")
            speak("he is in the ground floor room number 102")
            print("He is in the Ground floor\n Room No:102")
            speak("timing:2:00pm to 3:00pm")
            print("Timing:2:00pm-3:00pm")
            speak("contact number is 9751503202")
            print("Contact No:9751503202")

        elif'nephrologist' in query or 'kidney specialist' in query:
            speak("doctor murugananth")
            print("Dr.Murugananth")
            speak("he is in the ground floor room number 101")
            print("He is in the Ground floor\nRoom No:101")
            speak("timing:9:30am to 10:30am")
            print("Timing:9:30am-10:30am")
            speak("contact number is 9751503202")
            print("Contact No:9751503202")

        elif'psychiatrist' in query or 'psychiatry' in query:
            speak("doctor sarada menon")
            print("Dr.Sarada Menon")
            speak("she is in the ground floor room number 107")
            print("She is in the Ground floor\nRoom No:107")
            speak("timing:3:00pm to 4:00pm")
            print("Timing:3:00pm-4:00pm")
            speak("contact number is 9751503202")
            print("Contact No:9751503202")

        elif'dentist' in query or 'dental' in query:
            speak("doctor srisha")
            print("Dr.Srisha")
            speak("she is in the ground floor room number 108")
            print("She is in the Ground Floor\nRoom No:108")
            speak("timing:10:00am to 11:30am and 3:30pm to 4:30pm")
            print("Timing:10:00am-11:30am and 3:30pm-4:30pm")
            speak("contact number is 9751503202")
            print("Contact No:9751503202")

        elif'physiotherapist' in query or 'physiotherapy' in query:
            speak("doctor naveen")
            print("Dr.Naveen")
            speak("he is in the ground floor room number 109")
            print("He is in the Ground Floor\nRoom No:109")
            speak("timing:8:30am to 10:30am")
            print("Timing:8:30am to 10:30am")
            speak("contact number is 9751503202")
            print("Contact No:9751503202")

        elif'anesthesialogist' in query or 'anaesthesia' in query:
            speak("doctor bommana vinay kumar")
            print("Dr.Bommana Vinay Kumar")
            speak("he is in the ground floor room number 110")
            print("He is in the Ground Floor\nRoom No:110")
            speak("contact number is 9751503202")
            print("Contact No:9751503202")

        elif 'emergency ward' in query:
            speak("near second entrance, next to the reception")
            print("Near second Entrance, next to the Reception")
        
        elif 'icu' in query:
            speak("go straight from the second entrance, beside the operation theatre")
            print("Go straight from the 2nd Entrance, Beside the Operation Theatre")
        elif 'mri' in query:
            speak("take right from the reception and go straight, room number 1A")
            print("Take right from the Reception and Go straight\nRoom No:1A")

        elif 'ct' in query or 'scan' in query:
            speak("take right from the reception and go straight, near MRI scan, room number 1B")
            print("Take right from the Reception and Go straight, near MRI Scan\nRoom No:1B")

        elif 'ecg' in query:
            speak("take right from the reception and go straight near CT scan room number 1C")
            print("Take right from the Reception and Go straight, near CT scan\nRoom No:1C")

        elif 'x-ray' in query or 'xray' in query:
            speak("take right from the reception and go straight, near ECG centre, room number 1D")
            print("Take right from the Reception and Go straight, near ECG centre\nRoom No:1D")

        elif'pathologist' in query or 'pathology' in query:
            speak("doctor dhanush")
            print("Dr.Dhanush")
            speak("he is in the first floor room number 201")
            print("He is in the 1st Floor\nRoom No:201")
            speak("contact number is 9751503202")
            print("Contact No:9751503202")

        elif'pediatrician' in query or 'child specialist' in query:
            speak("doctor karthikeyan")
            print("Dr.Karthikeyan")
            speak("he is in the first floor room number 202")
            print("He is in the 1st Floor\nRoom No:202")
            speak("timing:9:00am to 11:00am")
            print("Timing:9:00am to 11:00am")
            speak("contact number is 9751503202")
            print("Contact No:9751503202")

        elif'operation theatre' in query:
            speak("go straight from the second entrance, beside the ICU ward")
            print("Go straight from the 2nd Entrance, beside the ICU ward")

        elif 'gate number 2' in query or  'entrance 2' in query:
            speak("below the 'EMERGENCY' board")
            print("Below the 'EMERGENCY' board")

        elif'canteen' in query or 'food' in query:
            speak("canteen or food court is in the Basement")
            print("Canteen/Food Court is in the BASEMENT")

        elif 'toilet' in query or 'restroom' in query:
            speak("beside the steps in every floor in the hospital")
            print('Beside the steps in Every Floor in the Hospital')

        elif 'lab' in query or 'test' in query:
            speak("back to the hospital near exit gate")
            print("Back to the Hospital near Exit Gate")

        elif'pharmacy' in query or 'medical' in query:
            speak("beside the main gate or entrance near reception")
            print("Beside the Main Gate/Entrance near Reception")

        elif 'deluxe' in query:
            speak("deluxe rooms are in the second floor from 202 to 220")
            print("Deluxe rooms are in the 2nd Floor\nFrom 202 to 220")

        elif 'suit' in query:
            speak("Suit rooms are in the third floor from 301 to 310")
            print("Suit rooms are in the 3rd Floor\nFrom 301 to 310")

        elif 'general' in query:
            speak("general wards are in the ground floor from 111 to 130")
            print("General wards are in the Ground Floor\nFrom 111 to 130")          

        elif "finish" in query or 'ok' in query or 'thank you' in query:
            speak("I think I was useful to you Sir. thank you")
            print("Thank You...")
            break
        else:
            continue
