import cv2
import mediapipe as mp
import pyautogui
import time

from gesture_detector import GestureDetector

# Webcam
cap = cv2.VideoCapture(0)

# MediaPipe setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Gesture detector
detector = GestureDetector()

# Cooldown for actions
last_action = 0
cooldown = 2  # seconds

# FPS calculation
prev_time = time.time()

while True:

    success, frame = cap.read()

    if not success:
        break

    # Mirror image
    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(rgb)

    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            # Draw landmarks
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            # Detect gesture
            gesture = detector.detect_gesture(
                hand_landmarks.landmark
            )

            # Hand position for text
            h, w, c = frame.shape

            x = int(hand_landmarks.landmark[0].x * w)
            y = int(hand_landmarks.landmark[0].y * h)

            # Display gesture label
            cv2.putText(
                frame,
                gesture,
                (x - 20, y - 20),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2
            )

            # Gesture → Action Mapping
            current_time = time.time()

            if current_time - last_action > cooldown:

                if gesture == "THUMBS UP":
                    pyautogui.press("playpause")
                    print("Play / Pause")

                elif gesture == "OPEN PALM":
                    pyautogui.press("volumeup")
                    print("Volume Up")

                elif gesture == "FIST":
                    pyautogui.press("volumedown")
                    print("Volume Down")

                last_action = current_time

    # FPS display
    current = time.time()

    fps = 1 / (current - prev_time)

    prev_time = current

    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    cv2.imshow(
        "Hand Gesture Recognition",
        frame
    )

    key = cv2.waitKey(1)

    if key == 27:  # ESC key
        break

cap.release()
cv2.destroyAllWindows()