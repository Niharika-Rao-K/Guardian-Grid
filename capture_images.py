#Asks for name of person and captures 20 pictures of him and stores it as a folder with his name inside the dataset folder
import cv2 # type: ignore
import os
import time
from picamera2 import Picamera2 # type: ignore
import numpy as np # type: ignore

# Load Haar cascade
face_cascade = cv2.CascadeClassifier('/usr/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')

# Ask for the person's name
name = input("Enter person's name: ")
save_path = os.path.join("dataset", name)
os.makedirs(save_path, exist_ok=True)
print(f"[INFO] Saving images to: {save_path}")

# Initialize Picamera2
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()

time.sleep(2)  # allow camera to warm up

count = 0
MAX_IMAGES = 20

while count < MAX_IMAGES:
    frame = picam2.capture_array()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # Draw and save each face
    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]
        img_name = os.path.join(save_path, f"{count}.jpg")
        cv2.imwrite(img_name, face_img)
        count += 1
        print(f"[INFO] Saved {img_name}")
        if count >= MAX_IMAGES:
            break

    # Show frame
    cv2.imshow("Capturing Faces", frame)

    # Press 'q' to quit early
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("[INFO] Done capturing images.")
cv2.destroyAllWindows()
picam2.close()
