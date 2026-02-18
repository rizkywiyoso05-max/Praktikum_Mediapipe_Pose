import  cv2
import  mediapipe as mp

mpose = mp.solutions.pose # inisiasi mediapipe pose
pose = mpose.Pose()
cap = cv2.VideoCapture(0) #video dari webcam

while True:
    success, img = cap.read() #pembaca img
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #merubah warna bgr ke rgb
    hasil =pose.process(imgRGB) #melakukan pemrosesan dari citra imgRGB
    if hasil.pose_landmarks:
        print("terdeteksi")
    else:
        print("tidak terdeteksi")

    cv2.imshow("webcam",img)
    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release() # Tutup wabcam dan jendela tampilan saat q ditekan
cv2.destroyAllWindows()




