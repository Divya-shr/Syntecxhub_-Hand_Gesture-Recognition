import mediapipe as mp


class GestureDetector:

    def __init__(self):
        self.mp_hands = mp.solutions.hands

    def get_finger_states(self, landmarks):

        fingers = []

        # Index finger
        fingers.append(
            1 if landmarks[8].y < landmarks[6].y else 0
        )

        # Middle finger
        fingers.append(
            1 if landmarks[12].y < landmarks[10].y else 0
        )

        # Ring finger
        fingers.append(
            1 if landmarks[16].y < landmarks[14].y else 0
        )

        # Pinky finger
        fingers.append(
            1 if landmarks[20].y < landmarks[18].y else 0
        )

        return fingers

    def thumb_up(self, landmarks):

        # Thumb tip above thumb joint
        thumb_extended = (
            landmarks[4].y < landmarks[3].y <
            landmarks[2].y
        )

        # All other fingers folded
        other_fingers_folded = (
            landmarks[8].y > landmarks[6].y and
            landmarks[12].y > landmarks[10].y and
            landmarks[16].y > landmarks[14].y and
            landmarks[20].y > landmarks[18].y
        )

        return thumb_extended and other_fingers_folded

    def detect_gesture(self, landmarks):

        fingers = self.get_finger_states(landmarks)

        # IMPORTANT:
        # Check THUMBS UP first

        if self.thumb_up(landmarks):
            return "THUMBS UP"

        if fingers == [1, 1, 1, 1]:
            return "OPEN PALM"

        if fingers == [0, 0, 0, 0]:
            return "FIST"

        return "UNKNOWN"