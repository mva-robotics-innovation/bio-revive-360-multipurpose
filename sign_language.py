# utils/sign_language.py
import mediapipe as mp
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS

hands = mp.solutions.hands.Hands()
command_active = False

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        if "command mode" in text.lower():
            global command_active
            command_active = True
            return True

def hands_to_speech(frame):
    if not command_active: return
    # Detect ASL signs → text → translate to Hindi/Telugu/Tamil/Bhojpuri
    # Using Mediapipe Hands landmarks + custom classifier
    # Then gTTS for realistic human voice
    translator = Translator()
    hindi = translator.translate("Help me", dest='hi').text
    # Play via gTTS
