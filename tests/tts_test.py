from src.speech.tts import TTS

tts = TTS(
    voice="af_bella",
)

tts.speak("Hello, dummy~")
