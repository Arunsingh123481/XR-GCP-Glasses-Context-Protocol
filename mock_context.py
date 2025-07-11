import random
import cv2
import pyaudio
import numpy as np

# -----------------------------------------------------------------------------
# Global evolving state for partial simulation
# -----------------------------------------------------------------------------
_state = {
    "light_level": "medium",
    "noise_level": "low",
    "people_nearby": 2
}

# -----------------------------------------------------------------------------
# Webcam-based light level detection
# -----------------------------------------------------------------------------
def detect_light_level():
    """
    Capture one frame from the webcam and estimate ambient light level.
    Returns: "low", "medium", or "high"
    """
    try:
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        print("Captured:", ret)

        # Convert to grayscale for brightness estimation
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        brightness = gray.mean()

        if brightness < 85:
            return "low"
        elif brightness < 170:
            return "medium"
        else:
            return "high"

    except Exception as e:
        print(f"[WARN] detect_light_level() error: {e}")
        return "medium"


def detect_noise_level():
    """
    Record a short snippet from the mic and classify noise level.
    Returns: "quiet", "low", "high"
    """
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    SECONDS = 0.2  # very short listen
    
    p = pyaudio.PyAudio()
    try:
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                        input=True, frames_per_buffer=CHUNK)
        frames = stream.read(int(RATE * SECONDS), exception_on_overflow=False)
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        # Convert to NumPy array and calculate volume
        audio_data = np.frombuffer(frames, dtype=np.int16)
        volume_norm = np.linalg.norm(audio_data) / len(audio_data)

        if volume_norm < 50:
            return "quiet"
        elif volume_norm < 300:
            return "low"
        else:
            return "high"

    except Exception as e:
        print(f"[WARN] detect_noise_level() error: {e}")
        p.terminate()
        return "low"


# -----------------------------------------------------------------------------
# Update evolving state for social context simulation
# -----------------------------------------------------------------------------
def update_state():
    """
    Simulate social context changing over time.
    """
    if random.random() < 0.4:
        _state["people_nearby"] = random.randint(0, 5)

# -----------------------------------------------------------------------------
# Main mock context generator
# -----------------------------------------------------------------------------
def generate_mock_context():
    """
    Returns a full context dictionary with:
    - spatial context (room, dimensions, objects)
    - social context (people_nearby, interaction_mode)
    - environmental context (light_level, noise_level)
    - user context (gaze_direction, activity)
    """
    update_state()

    context = {
        "spatial": {
            "room": random.choice(["living_room", "kitchen", "bedroom"]),
            "dimensions": {
                "width": round(random.uniform(3, 6), 1),
                "height": 2.5,
                "depth": round(random.uniform(4, 7), 1)
            },
            "objects": random.sample(["desk", "lamp", "sofa", "TV", "chair"], 3)
        },
        "social": {
            "people_nearby": _state["people_nearby"],
            "interaction_mode": random.choice(["alone", "conversation", "meeting"])
        },
        "environmental": {
            "light_level": detect_light_level(),
            "noise_level": detect_noise_level(),
        },
        "user": {
            "gaze_direction": random.choice(["left", "right", "forward"]),
            "activity": random.choice(["working", "relaxing", "moving"])
        }
    }

    return context
