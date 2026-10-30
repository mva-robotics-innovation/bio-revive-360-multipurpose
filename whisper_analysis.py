# utils/whisper_analysis.py
import whisper
from transformers import pipeline

model = whisper.load_model("base")
# For disabled person - unclear whisper
def analyze_whisper(audio_path):
    result = model.transcribe(audio_path)
    unclear_text = result["text"]
    # LLM RAG to understand intent
    llm = pipeline("text2text-generation", model="google/flan-t5-base")
    clear_intent = llm(f"Clarify this unclear speech: {unclear_text}")[0]['generated_text']
    
    # Voice clone - using his sample
    # Use: Coqui TTS XTTS-v2 for voice cloning
    # pip install TTS
    # from TTS.api import TTS
    # tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
    # tts.tts_to_file(text=clear_intent, speaker_wav="his_voice_sample.wav", file_path="output.wav", language="en")
    return clear_intent
