import cv2 # type: ignore
import RPi.GPIO as GPIO # type: ignore
import time
import os
from datetime import datetime
from picamera2 import Picamera2 # type: ignore
import serial # type: ignore
import smtplib
from email.message import EmailMessage

# --------------------------- CONFIG ---------------------------
SENSOR_PIN = 17
PHONE_NUMBER = "+91xxxxxxxxxx"
EMAIL_ADDRESS = "abc@gmail.com"        # <--- your email
EMAIL_PASSWORD = "qqxv sbtp zdvn eaqg"     # <--- 16-char app password
# --------------------------------------------------------------

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

# Load face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

# Load Haar cascade
face_cascade = cv2.CascadeClassifier("/home/pi/haarcascades/haarcascade_frontalface_default.xml")

# Load labels
labels = {}
with open("labels.txt", "r") as f:
    for line in f:
        key, value = line.strip().split(":")
        labels[int(key)] = value

# Set up Picamera2
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "BGR888"
picam2.configure("preview")
picam2.start()
time.sleep(2)

# ---------------------- SMS Function ----------------------
def send_sms(phone_number, message):
    try:
        ser = serial.Serial('/dev/serial0', baudrate=115200, timeout=3)
        print("[INFO] GSM Serial port opened.")
        time.sleep(2)

        ser.flushInput()
        ser.write(b'AT\r')
        time.sleep(0.5)
        response = ser.read(ser.inWaiting()).decode()
        print("[DEBUG] GSM Response to AT:", response)
        if "OK" not in response:
            print("[ERROR] GSM not responding properly.")
            return

        ser.write(b'AT+CMGF=1\r')
        time.sleep(0.5)

        ser.write(f'AT+CMGS="{phone_number}"\r'.encode())
        time.sleep(0.5)

        ser.write(f"{message}\x1A".encode())
        time.sleep(3)

        print("[INFO] SMS sent successfully")

    except Exception as e:
        print(f"[ERROR] Failed to send SMS: {e}")

# ---------------------- Email Function ----------------------
def send_email_with_image(image_path):
    msg = EmailMessage()
    msg['Subject'] = 'Unknown Person Detected!'
    msg['From'] = sender@gmail.com # type: ignore
    msg['To'] = receiver@gmail.com # type: ignore
    msg.set_content('An unknown person was detected. See the attached image.')

    try:
        with open(image_path, 'rb') as f:
            file_data = f.read()
            file_name = os.path.basename(image_path)
            msg.add_attachment(file_data, maintype='image', subtype='jpeg', filename=file_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("[EMAIL] Alert email sent successfully.")

    except Exception as e:
        print(f"[EMAIL ERROR] Failed to send email: {e}")

# -------------------- Face Detection Logic --------------------
def detect_and_log():
    frame = picam2.capture_array()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    status = "not_detected"
    name = "Unknown"

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        id_, conf = recognizer.predict(roi_gray)
        if conf < 80:
            name = labels.get(id_, "Unknown")
            status = "detected"
            cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
        else:
            name = "Unknown"
            status = "unknown"
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    os.makedirs("logs", exist_ok=True)
    log_path = f"logs/{status}{name}{timestamp}.jpg"
    cv2.imwrite(log_path, frame)
    print(f"[{status.upper()}] {name} - saved to {log_path}")

    if len(faces) > 0 and status == "unknown":
        print("[DEBUG] Unknown face detected. Triggering SMS & Email.")
        send_sms(PHONE_NUMBER, "Unknown person detected on camera!")
        send_email_with_image(log_path)
    else:
        print(f"[DEBUG] Not sending alerts. Faces: {len(faces)}, Status: {status}")

# -------------------------- Main Loop -------------------------
try:
    print("System ready. Step on the sensor to scan a face.")
    previous_sensor_val = 0
    while True:
        sensor_val = GPIO.input(SENSOR_PIN)
        if sensor_val == 1 and previous_sensor_val == 0:
            print("Step detected - scanning face...")
            detect_and_log()
            while GPIO.input(SENSOR_PIN):
                time.sleep(0.1)
            time.sleep(1)
        previous_sensor_val = sensor_val
        time.sleep(0.05)

except KeyboardInterrupt:
    print("Program stopped by user.")

finally:
    GPIO.cleanup()
    print("GPIO cleaned up.") 
