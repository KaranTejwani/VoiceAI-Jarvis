import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import os
import uuid

SAMPLE_RATE = 44100
DURATION = 5      

def record_audio(filename="temp.wav"):
    print("🎤 Recording... Speak now.")
    
    audio = sd.rec(int(SAMPLE_RATE * DURATION), 
                   samplerate=SAMPLE_RATE, 
                   channels=1,          
                   dtype='int16')        
    
    sd.wait()
    
    write(filename, SAMPLE_RATE, audio)
    print("✅ Recording finished.")

def transcribe_audio(filename="temp.wav", model_size="base"):
    print(f"🧠 Loading Whisper model: {model_size}")

    model = whisper.load_model(model_size)
    
    print("📝 Transcribing...")
    result = model.transcribe(filename, fp16=False, verbose=True)
    
    print("🗣️ Transcription:", result["text"])
    return result["text"]

if __name__ == "__main__":
    filename = f"record_{uuid.uuid4()}.wav"
    
    record_audio(filename)
    transcribe_audio(filename)
    
    os.remove(filename)
