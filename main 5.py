import speech_recognition as sr
import google.generativeai as genai
import os

recognizer = sr.Recognizer()
API_KEY = 'AIzaSyDFF0qlHYRFm0U9wKX5iLfuuMKfnvTw1Qs' 
genai.configure(api_key=API_KEY)

def capture_voice_input():
    """Capture audio from microphone"""
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    return audio    

def convert_voice_to_text(audio):
    """Convert speech to text using Google's speech recognition"""
    if audio is None:
        return ""
    
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def process_voice_command(text):
    """Process the voice command using Gemini AI"""
    if not text:
        return True  
    
    text_lower = text.lower()
    if "stop" in text_lower:
        print("thank you!")
        return False
    
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest") 
        response = model.generate_content(text)
        print("Gemini:", response.text)
    except Exception as e:
        print(f"Error processing command: {e}")
    
    return True

def main():
    """Main program loop"""
    print("Voice Assistant started. Say 'stop'.")
    while True:
        audio = capture_voice_input()
        text = convert_voice_to_text(audio)
        if not process_voice_command(text):
            break

if __name__ == "__main__":
    main()