import time
import multiprocessing
import speech_recognition as sr
# from openai import OpenAI
import json
import os


def speak(mic,person):
    with sr.Microphone(device_index=mic) as source:

        r.adjust_for_ambient_noise(source)

        print("Listening...")
        audio = r.listen(source)
        print("Stop Listening")

        try:
            # using google to transcribe the audio file to text
            text = r.recognize_google(audio)

            print(text)

            # print("mic " + str(mic) + " " + person + " said: " + text)
            with open("/home/billhuynh/git/HRI-576/lab2/name.txt", "a") as f:
                f.write(text+"\n")  

        except Exception as e:
            print(f"An error occurred: {e}")

        time.sleep(1)		


if __name__ == "__main__":		

    # Initialize the recognizer
    r = sr.Recognizer()

    chat_history = [{"role": "system", "content": "You are a NAO robot that provides appropiate gestures while answering my questions breifly. Provide the response in this example format: First part of response ^start(animations/Stand/Gestures/Hey_1) second part of response. "}]
    with open("history.txt", "w") as f:
        json.dump(chat_history,f)
# replace the parameters accordingly
    previous_dir_count = len(os.listdir("/home/billhuynh/git/HRI-576/lab2/names/"))
    while True:
        new_dir_count = len(os.listdir("/home/billhuynh/git/HRI-576/lab2/names/"))
        if (new_dir_count > previous_dir_count):
            previous_dir_count = new_dir_count
            speak(5,"Human")
