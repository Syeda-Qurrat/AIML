# 🏋️ Shoulder Press Rep Counter using Computer Vision

A real-time **AI-powered exercise repetition counter** that detects and counts dumbbell shoulder press repetitions using **MediaPipe Pose Estimation, OpenCV, and NumPy**.

---

## 📌 Project Overview

This project uses **computer vision and pose estimation** to track elbow joint movement through a webcam feed. It calculates the angle between shoulder–elbow–wrist coordinates and counts repetitions based on joint angle thresholds.

The system works in real-time and visually displays:

* Live elbow angle values
* Total repetition count
* Pose landmark connections

---

## 🚀 Features

* Real-time webcam-based detection
* Human pose tracking using MediaPipe
* Elbow joint angle calculation using NumPy
* Automatic rep counting using angle-threshold logic
* Visual feedback with OpenCV overlays
* Left and right arm tracking

---

## 🛠️ Tech Stack

* **Python**
* **OpenCV**
* **MediaPipe (Pose Estimation)**
* **NumPy**

---

## 🧠 How It Works

1. Captures live video feed using OpenCV.
2. Uses MediaPipe Pose to extract body landmarks.
3. Identifies shoulder, elbow, and wrist coordinates.
4. Calculates elbow angle using trigonometric angle formula.
5. Applies threshold logic:

   * Angle > 160° → "Down" stage
   * Angle < 60° → "Up" stage
6. Increments repetition counter when a full motion cycle is completed.
7. Displays real-time feedback on screen.

---

## 📷 Application Window

* Shows pose skeleton overlay
* Displays elbow angle values
* Shows total repetition count
* Press **'q'** to exit

---

## ▶️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/shoulder-press-counter.git
cd shoulder-press-counter
```

### 2️⃣ Install Dependencies

```bash
pip install opencv-python mediapipe numpy
```

### 3️⃣ Run the Script

```bash
python shoulder_press_counter.py
```

Make sure your webcam is enabled.

---

## 🎯 Learning Outcomes

* Implemented real-time pose estimation
* Applied trigonometry for joint angle calculation
* Built motion tracking logic using threshold-based classification
* Gained hands-on experience in computer vision and human movement analysis

---

## 📌 Future Improvements

* Add accuracy metrics
* Add UI dashboard
* Add multiple exercise detection
* Deploy as fitness monitoring web app

---
