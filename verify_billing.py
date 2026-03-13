import os
import sys
from google.cloud import texttospeech, vision
import google.generativeai as genai
from dotenv import load_dotenv

# Setup
sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'serviceAccountKey.json'

def test_gemini():
    print("\nTesting Gemini API...", end=" ", flush=True)
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("❌ Failed: GEMINI_API_KEY not found in .env", flush=True)
            return
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("Hello")
        if response.text:
            print("✅ Success", flush=True)
        else:
            print("⚠️ Response received but empty", flush=True)
    except Exception as e:
        print(f"❌ Failed: {e}", flush=True)

def test_tts():
    print("Testing Text-to-Speech API...", end=" ", flush=True)
    try:
        client = texttospeech.TextToSpeechClient()
        synthesis_input = texttospeech.SynthesisInput(text="Billing verification test.")
        voice = texttospeech.VoiceSelectionParams(language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
        audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)
        client.synthesize_speech(input=synthesis_input, voice=voice, audio_config=audio_config)
        print("✅ Success", flush=True)
    except Exception as e:
        print(f"❌ Failed: {e}", flush=True)

def test_vision():
    print("Testing Vision API...", end=" ", flush=True)
    try:
        client = vision.ImageAnnotatorClient()
        file_path = 'diagram-export-9-29-2025-3_41_04-PM.png'
        if os.path.exists(file_path):
            with open(file_path, "rb") as image_file:
                content = image_file.read()
            image = vision.Image(content=content)
            client.text_detection(image=image)
            print("✅ Success", flush=True)
        else:
            print(f"⚠️ Skipped ({file_path} not found)", flush=True)
    except Exception as e:
        print(f"❌ Failed: {e}", flush=True)

if __name__ == "__main__":
    print("--- Verifying Google Cloud Services & Billing Status ---", flush=True)
    test_gemini()
    # test_tts()
    # test_vision()
    print("\nDone.", flush=True)
