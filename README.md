# 🧠 XR-GCP + NCP: Context Fusion Protocol for Smart XR Glasses

This repository contains the prototype of a **real-time contextual inference system** that fuses **GCP (Glasses Context Protocol)** and **NCP (Neural Context Protocol)** to enable intelligent, context-aware behavior in XR devices.

Designed for smart glasses, edge devices, and XR applications, this system can simulate user environments and predict mental states like **intent**, **mood**, and **mental load** using lightweight Python components.

---

## ⚙️ Key Features

- ✅ Modular GCP Adapter (spatial, environmental, user, and social context)
- ✅ NCP Cognitive Engine (intent, mood, mental load)
- ✅ Context fusion via Flask API
- ✅ Real-time Server-Sent Events (SSE) streaming
- ✅ Easily extensible to support gesture, EEG, and scene sensors

---

## 🌐 API Endpoints

 Endpoint                Description                      Method 
 `/api/context`         Get current GCP context           `GET`  
 `/api/stream`          Real-time GCP stream              `GET`
 `/api/fused_stream`    Auto-generated GCP+NCP stream     `GET`


#Sample Output

json
{
  "spatial": {"room": "living_room", "objects": ["TV", "lamp"]},
  "environmental": {"noise_level": "low", "light_level": "medium"},
  "social": {"people_nearby": 2, "interaction_mode": "conversation"},
  "user": {"activity": "relaxing", "gaze_direction": "left"},
  "neural": {
    "intent": "focus",
    "mental_load": "medium",
    "mood": "calm"
  }
}

How to Run (Linux / Mac / Windows)
1.Clone the Repository

git clone https://github.com/Arunsingh123481/XR-GCP-Glasses-Context-Protocol.git
cd XR-GCP-Glasses-Context-Protocol

2 Create Virtual Environment (recommended)

python3 -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

3.Install Dependencies

pip install -r requirements.txt

4.Run the Flask Server

export XR_NCP_CONSENT=true
python app.py

🔗 Access Locally

    http://localhost:8080/api/context

    http://localhost:8080/api/fused_stream

👓 Smart Glasses Deployment Guide
A. Ubuntu/Linux XR Glasses

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

    ✅ Use gunicorn or systemd for production

gunicorn -w 2 -b 0.0.0.0:8080 app:app

B. Android-Based XR (Termux)

pkg install python git
git clone https://github.com/Arunsingh123481/XR-GCP-Glasses-Context-Protocol.git
cd XR-GCP-Glasses-Context-Protocol
pip install -r requirements.txt
python app.py

C. Custom Linux/Yocto XR Devices

    Use pip or opkg to install Python 3.8+

    Adapt mock_adapter.py to read from real sensors

    Run app.py via background daemon or init system

📦 requirements.txt

Flask==2.3.3
opencv-python==4.8.0.76
sounddevice==0.4.6
numpy==1.26.4

💡 Innovation and Research Scope

This project introduces a standardized neural-environmental context protocol for XR, enabling:

    🎯 Cognitive intent + mood prediction

    🧠 Fusion of perceptual + neural context

    🛠️ Modular architecture for edge devices

    🔒 On-device, privacy-aware context inference

🧪 Research Potential

    📘 Publish as: “Neural-Environmental Context Fusion for Cognitive-Aware XR Systems”

    Topics you can expand:

        Context modeling standards for wearables

        Fusion architectures (XR inference pipelines)

        Privacy-preserving local cognition models

        Adaptive XR interfaces based on cognitive state

Author

Arun Singh
🔗 github.com/Arunsingh123481

🚀 Coming Soon

EEG input integration (Muse, NeuroSky)

Webcam + emotion AI integration

React dashboard UI

Gesture → Intent fusion
