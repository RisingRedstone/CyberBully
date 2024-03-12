# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 04:17:06 2024

@author: prath
"""

import whisper
import pyaudio
import wave
import requests
from transformers import pipeline

distilled_student_sentiment_classifier = pipeline(
    model="lxyuan/distilbert-base-multilingual-cased-sentiments-student", 
    return_all_scores=True
)

callRequest = 0
VoiceOutput = {"text":"","toxic":0}
def whisperCall(file_path):
    global callRequest
    if(callRequest == 1):
        return ""
    callRequest = 1
    record_audio(file_path)
    model = whisper.load_model("base")
    result=model.transcribe(file_path)
    VoiceOutput['text'] = result["text"]
    VoiceOutput['toxic'] = distilled_student_sentiment_classifier(result["text"]);
    callRequest = 0
    return result

def record_audio(file_path, duration=7, sample_rate=44100, chunk_size=1024, format=pyaudio.paInt16, channels=1):
    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Open a stream
    stream = p.open(format=format,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=chunk_size)

    print("Recording...")

    frames = []
    for i in range(0, int(sample_rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)
    
    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(p.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

    print("Recording done.")

    # Stop the stream and close it
    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == "__main__":
    #file_path = "D:\\Progress\\Projects\\cyberbullying\\recorded_audio.wav"
    file_path = "C:\\Simple\\recorded_audio.wav"
    record_audio(file_path)

    print(f"Audio recorded and saved to {file_path}")

