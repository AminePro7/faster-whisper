import pyaudio
import wave
from datetime import datetime
import keyboard
from faster_whisper import WhisperModel

def record_audio(filename, duration=5):
    # Audio recording parameters
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                   channels=CHANNELS,
                   rate=RATE,
                   input=True,
                   frames_per_buffer=CHUNK)

    print("* recording")

    frames = []

    for i in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("* done recording")

    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

def main():
    # Load the Whisper model
    print("Loading Whisper model...")
    model = WhisperModel("medium", device="cpu", compute_type="int8", cpu_threads=4)
    print("Model loaded!")

    while True:
        # Wait for spacebar press to start recording
        print("\nPress and hold SPACE to record (or 'q' to quit)...")
        keyboard.wait('space')
        
        if keyboard.is_pressed('q'):
            break

        # Generate unique filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        audio_file = f"recording_{timestamp}.wav"

        # Record audio while space is held
        record_audio(audio_file)

        # Transcribe the audio
        print("Transcribing...")
        segments, info = model.transcribe(audio_file)
        
        # Print the transcription
        for segment in segments:
            print("\nTranscription:", segment.text)

if __name__ == "__main__":
    main() 