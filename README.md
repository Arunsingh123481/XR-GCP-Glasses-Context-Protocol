# NCP-Neural-Context-Protocol
=======
# XR-GCP Glasses Context Protocol

This repo contains the real-time fusion of GCP (Glasses Context Protocol) and NCP (Neural Context Protocol) for context-aware XR systems.

- Modular architecture
- Flask-based API
- GCP: spatial, environmental, user context
- NCP: mood, intent, mental load prediction

---

## 📦 Features

✅ Environmental sensing (light/noise levels)  
✅ Social context (people nearby, interaction mode)  
✅ Spatial context (room, objects, dimensions)  
✅ User context (activity, gaze direction)  
✅ REST API endpoint + Server-Sent Events (SSE) streaming  
✅ Modular and portable Python implementation  

---

## 🌐 API Endpoints

  Endpoint                 Description               Method 

`/api/context`   Get current context as JSON           GET    
`/api/stream`    Get real-time context updates         GET    

Response Example:

json :-
{
  "environmental": {
    "light_level": "medium",
    "noise_level": "low"
  },
  "social": {
    "interaction_mode": "conversation",
    "people_nearby": 2
  },
  "spatial": {
    "room": "living_room",
    "dimensions": {
      "width": 4.0,
      "height": 2.5,
      "depth": 5.0
    },
    "objects": ["desk", "lamp", "sofa"]
  },
  "user": {
    "gaze_direction": "forward",
    "activity": "working"
  }
}

How to Run on PC (Linux / Mac / Windows)

1️⃣ Clone the repository:

git clone https://github.com/Arunsingh123481/XR-GCP-Glasses-Context-Protocol.git
cd XR-GCP-Glasses-Context-Protocol

2️⃣ Create a virtual environment (recommended):

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3️⃣ Install requirements:

pip install -r requirements.txt

4️⃣ Start the server:

python app.py

5️⃣ Access on local device:

    http://localhost:8080/api/context

    http://localhost:8080/api/stream

👓 Deployment on Smart Glasses or Embedded Devices
A. Ubuntu / Linux-based Smart Glasses (e.g., custom XR dev kits)

    Ensure Python 3 and pip are installed.

    Clone or copy this repository to the device.

    Install requirements in a virtual environment:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

requirements.txt
Flask==2.3.3
opencv-python==4.8.0.76
sounddevice==0.4.6
numpy==1.26.4


Start the server:

python app.py

For production: run with Gunicorn or systemd:

    gunicorn -w 2 -b 0.0.0.0:8080 app:app

    Access via local network or device loopback.

B. Android-based Smart Glasses

For Android-based systems that support Python (e.g., via Termux):

    Install Termux.

    Install Python:

pkg install python

Clone the repo:

git clone https://github.com/Arunsingh123481/XR-GCP-Glasses-Context-Protocol.git
cd XR-GCP-Glasses-Context-Protocol

Install requirements:

pip install -r requirements.txt

Run:

    python app.py

⚠️ Note: On Android you may need to adjust permissions for microphone/camera if your mock context uses them.
C. Other OS (e.g., Yocto, custom Linux)

    Ensure you have Python 3.8+ support.

    Use pip to install Flask and other dependencies.

    Copy or clone the project.

    Adapt mock_context.py to use available sensors/APIs on your hardware.

    Run the server as a service or background process.

💡 Innovation

This protocol defines a standardized, machine-readable context model for XR and wearable devices, enabling:

  Adaptive interfaces

  Context-aware applications

  Simulated and real sensor integration

  Local privacy-preserving computation

Research potential:
You can extend this work into a research paper by discussing:

  Context modeling standards for XR

  Implementation architecture

  Privacy design (on-device API)

  Developer feedback and use-
