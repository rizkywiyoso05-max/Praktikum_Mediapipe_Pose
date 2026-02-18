import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        landmarks = results.pose_landmarks.landmark

        shoulder_right = landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value]
        wrist_right = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value]

        shoulder_left = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
        wrist_left = landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value]

        # Cek tangan kanan terangkat
        if wrist_right.y < shoulder_right.y:
            cv2.putText(img, "Tangan kanan", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        # Cek tangan kiri terangkat
        if wrist_left.y < shoulder_left.y:
            cv2.putText(img, "Tangan kiri", (50, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Deteksi Angkat Tangan", img)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
