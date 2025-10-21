import cv2 # type: ignore
import os
import numpy as np # type: ignore

DATASET_DIR = 'dataset'
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def prepare_data():
    faces = []
    labels = []
    label_map = {}
    label_id = 0

    for person in os.listdir(DATASET_DIR):
        person_path = os.path.join(DATASET_DIR, person)
        if not os.path.isdir(person_path):
            continue
        label_map[label_id] = person
        for image_name in os.listdir(person_path):
            image_path = os.path.join(person_path, image_name)
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            faces_rects = face_cascade.detectMultiScale(img, scaleFactor=1.2, minNeighbors=5)
            for (x, y, w, h) in faces_rects:
                face = img[y:y + h, x:x + w]
                faces.append(face)
                labels.append(label_id)
        label_id += 1
    return faces, labels, label_map

faces, labels, label_map = prepare_data()

# Train the LBPH face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(labels))

# Live camera recognition
cap = cv2.VideoCapture(0)
print("Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces_rects = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    for (x, y, w, h) in faces_rects:
        face_roi = gray[y:y + h, x:x + w]
        label, confidence = recognizer.predict(face_roi)
        name = label_map.get(label, 'Unknown')
        cv2.putText(frame, f'{name} ({int(confidence)})', (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

