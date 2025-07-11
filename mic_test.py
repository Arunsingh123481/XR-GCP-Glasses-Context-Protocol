import pyaudio
import numpy as np

def detect_noise_level():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    SECONDS = 0.2
    
    p = pyaudio.PyAudio()
    try:
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                        input=True, frames_per_buffer=CHUNK)
        frames = stream.read(int(RATE * SECONDS), exception_on_overflow=False)
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        audio_data = np.frombuffer(frames, dtype=np.int16)
        volume_norm = np.linalg.norm(audio_data) / len(audio_data)

        if volume_norm < 50:
            return "quiet"
        elif volume_norm < 300:
            return "low"
        else:
            return "high"

    except Exception as e:
        print("Error:", e)
        p.terminate()
        return "low"

print("Noise Level:", detect_noise_level())
