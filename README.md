# Guardian-Grid
The primary objective of this project is to design and develop an intelligent anti-theft security system using an IoT-enabled floormat integrated with face recognition technology
Hardware Requirements:
●	A PC with the following or greater specifications:
o	Intel Core i3 or higher
o	8 GB RAM
o	500 GB Hard Drive
●	A stable internet connection (2Mbps or higher)
●	Raspberry Pi 4 
●	Pi Camera
●	Piezo sensor
●	Jumper Wires
●	Power Supply
●	MicroSD Card (at least 16GB)
●	GSM Module (with Antenna)

2.2 Software Requirements:

•	Operating system	                   : Windows, Raspberry Pi OS
•	IDE                                           : VS Code, Sublime text
•	Language                                  : Python
•	Libraries of Python                   : OpenCV, Haarcascade, Numpy, PySerial(for UART communication with the GSM module)
•	Machine Learning Model used : Local Binary Patterns Histogram(LBPH)
<img width="660" height="400" alt="image" src="https://github.com/user-attachments/assets/4207c2bc-b0c6-43ee-8599-85fbbbcc7428" />
Files present:
1.	capture_images.py- Asks for name of person and captures 20 pictures of him and stores it as a folder with his name inside the dataset folder
   How to run: python3 capture_images.py
3.	train_model.py-Trains the RPi with the photos captures by capture_images.py
   How to run: python3 train_model.py
5.	Face_recog_lbph.py-Performs real-time face recognition using OpenCV
   How to run: python3 Face_recog_lbph.py
7.	recognize_face_sensor.py- This Python code is designed for a Raspberry Pi-based face recognition security system. It uses a piezo sensor to detect if someone steps on a mat, triggering the PiCamera2 to capture an image. The captured image is analyzed using OpenCV's LBPH face recognizer and a Haar Cascade classifier to detect and recognize faces. If the face is unknown, the system saves the image, sends an SMS alert using a GSM module, and sends an email with the image attachment. Recognized faces are labeled and logged without alerts. The system continuously monitors the sensor and logs all detections with timestamps, enhancing home or lab security with real-time alerts.
   How to run: python3 recognize_face_sensor.py
  RUN THIS CODE AND PERFORM THE EXPERIMENT
9.	Dataset folder- stores images of people
10.	Logs folder- stores both recognized and unrecognized face photos with date & time.
Machine Learning Model Used: LBPH (Local Binary Patterns Histograms)
1.	Model Type:
•	Local Binary Patterns Histograms (LBPH) — a classic computer vision-based face recognition algorithm.
2.	Why LBPH is used:
•	Lightweight and fast — ideal for low-power devices like Raspberry Pi.
•	Works well with grayscale images and small datasets.
•	Robust against lighting variations and facial expressions.
3.	How It Works:
•	Divides image into grids and compares each pixel with its neighbors.
•	Generates a binary pattern based on intensity differences.
•	Builds histograms of these patterns for each region and concatenates them into a feature vector.
•	Uses Euclidean distance (or similar) to compare new faces with trained ones.
4.	Training Step:
•	Implemented using train_model.py with images captured and labeled using capture_images.py.
•	Model is trained using OpenCV’s cv2.face.LBPHFaceRecognizer_create().
5.	Prediction Step:
•	recognize_face_sensor.py loads the trained model and predicts face ID when triggered by the piezo sensor.
6.	No Deep Learning Required:
•	Unlike CNNs or DNNs, LBPH does not require GPU or large datasets.
•	Makes it ideal for edge AI and embedded systems.


