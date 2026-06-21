# Hand Gesture Recognition using MediaPipe and OpenCV

## Overview

This project performs real-time hand gesture recognition using a webcam.

The system detects hand landmarks using MediaPipe and classifies the following gestures:

- Open Palm
- Fist
- Thumbs Up

Each gesture is mapped to a system action:

| Gesture | Action |
|----------|----------|
| Open Palm | Volume Up |
| Fist | Volume Down |
| Thumbs Up | Play/Pause |

---

## Technologies Used

- Python
- OpenCV
- MediaPipe
- PyAutoGUI

---

## Project Structure

HandGestureRecognition/
│
├── main.py
├── gesture_detector.py
├── requirements.txt
├── README.md
│
├── screenshots/
└── demo/

---

## Installation

```bash
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

---

## Features

- Real-time hand landmark detection
- Gesture classification
- Gesture-to-action mapping
- FPS display
- Webcam-based interaction

---

## Supported Gestures

### Open Palm

Action:
Volume Up

### Fist

Action:
Volume Down

### Thumbs Up

Action:
Play/Pause

---

## Future Enhancements

- Peace Sign Detection
- OK Sign Detection
- Sign Language Recognition
- Gesture-Based Presentation Control

---

## Author

Your Name
