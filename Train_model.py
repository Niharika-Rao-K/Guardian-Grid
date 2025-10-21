import cv2 # type: ignore
import os
import numpy as np # type: ignore

dataset_path = "dataset"
recognizer = cv2.face.LBPHFaceRecognizer_create()
face_cascade = cv2.CascadeClassifier('/home/pi/haarcascades/haarcascade_frontalface_default.xml')



faces = []
labels = []
label_map = {}

label_id = 0

for person in os.listdir(dataset_path):
    person_path = os.path.join(dataset_path, person)
    label_map[label_id] = person
    for image_file in os.listdir(person_path):
        img_path = os.path.join(person_path, image_file)
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        faces.append(img)
        labels.append(label_id)
    label_id += 1

recognizer.train(faces, np.array(labels))
recognizer.save("trainer.yml")

with open("labels.txt", "w") as f:
    for key in label_map:
        f.write(f"{key}:{label_map[key]}\n")
