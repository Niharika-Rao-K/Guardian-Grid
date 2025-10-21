<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">

<style>
  body {
    font-family: 'Poppins', sans-serif;
    background-color: #0d1117;
    color: #e6edf3;
    line-height: 1.7;
  }
  h1, h2, h3 {
    color: #58a6ff;
    font-weight: 600;
  }
  h1 {
    font-size: 2.4em;
    margin-top: 30px;
  }
  h3 {
    color: #8b949e;
    font-weight: 400;
  }
  ul li, ol li {
    margin-bottom: 8px;
  }
  table {
    border-collapse: collapse;
    width: 85%;
    margin: 20px auto;
    background-color: #161b22;
    color: #e6edf3;
    border-radius: 10px;
    overflow: hidden;
  }
  td {
    border: 1px solid #30363d;
    padding: 10px 12px;
  }
  code {
    background-color: transparent;
    color: #58a6ff;
    font-style: italic;
  }
  p, li {
    font-size: 1.05em;
  }
</style>

<h1 align="center">🛡️ Guardian-Grid</h1>
<h3 align="center">An Intelligent IoT-Enabled Anti-Theft Floor Mat with Face Recognition</h3>

---

<h2>🎯 Project Overview</h2>
<p>
<b>Guardian-Grid</b> is an IoT-based smart security system designed to prevent unauthorized access. 
It integrates a <b>piezoelectric floor mat</b> that detects footsteps and a <b>face recognition system</b> that identifies the person in real-time. 
If an unrecognized face is detected, the system captures the image, sends an <b>SMS alert</b> via a GSM module, and logs all events for review.
</p>

---

<h2>⚙️ Hardware Requirements</h2>
<ul>
  <li><b>PC:</b> Intel Core i3 or higher, 8 GB RAM, 500 GB HDD</li>
  <li><b>Internet:</b> Minimum 2 Mbps</li>
  <li><b>Raspberry Pi 4</b></li>
  <li><b>Pi Camera</b></li>
  <li><b>Piezo Sensor</b></li>
  <li><b>GSM Module</b> (with Antenna)</li>
  <li><b>MicroSD Card:</b> 16 GB or more</li>
  <li><b>Power Supply</b> & Jumper Wires</li>
</ul>

---

<h2>💻 Software Requirements</h2>
<table>
  <tr><td><b>Operating System</b></td><td>Windows, Raspberry Pi OS</td></tr>
  <tr><td><b>IDE</b></td><td>VS Code, Sublime Text</td></tr>
  <tr><td><b>Programming Language</b></td><td>Python</td></tr>
  <tr><td><b>Libraries</b></td><td>OpenCV, Haarcascade, Numpy, PySerial</td></tr>
  <tr><td><b>Machine Learning Model</b></td><td>Local Binary Patterns Histogram (LBPH)</td></tr>
</table>

---

<h2>📂 Project File Structure</h2>
<ul>
  <li><b>capture_images.py</b> – Captures 20 face images per person and stores them in <i>dataset/</i></li>
  <li><b>train_model.py</b> – Trains the LBPH model using captured faces</li>
  <li><b>Face_recog_lbph.py</b> – Performs real-time face recognition</li>
  <li><b>recognize_face_sensor.py</b> – Triggers face recognition via piezo mat; sends alerts and logs results</li>
  <li><b>dataset/</b> – Contains face images for each individual</li>
  <li><b>logs/</b> – Contains timestamped images of detections</li>
</ul>

<p align="center">
  <h2>Circuit Diagram</h2>
  <img src="https://github.com/user-attachments/assets/4207c2bc-b0c6-43ee-8599-85fbbbcc7428" width="660" height="400" alt="Guardian Grid System Diagram">
</p>

---

<h2>🤖 Machine Learning Model: LBPH (Local Binary Patterns Histograms)</h2>

<h3>📘 Model Type</h3>
<p>LBPH — a classical computer vision algorithm for facial recognition, optimized for embedded hardware.</p>

<h3>💡 Why LBPH?</h3>
<ul>
  <li>Lightweight and efficient for Raspberry Pi</li>
  <li>Works well with grayscale images</li>
  <li>Robust against lighting and expression variations</li>
</ul>

<h3>⚙️ How It Works</h3>
<ol>
  <li>Divides an image into small grids</li>
  <li>Compares each pixel with neighbors to form binary patterns</li>
  <li>Builds histograms for each grid region</li>
  <li>Concatenates them into a single feature vector</li>
  <li>Compares new faces using distance metrics like Euclidean distance</li>
</ol>

<h3>🧠 Training Step</h3>
<p>
Images captured by <i>capture_images.py</i> are labeled and trained using <i>train_model.py</i> with OpenCV’s 
<b>cv2.face.LBPHFaceRecognizer_create()</b>.
</p>

<h3>🔍 Prediction Step</h3>
<p>
When the piezo sensor detects pressure, <i>recognize_face_sensor.py</i> activates the camera and checks for known faces, logging results automatically.
</p>

<h3>🚫 No Deep Learning Required</h3>
<ul>
  <li>No GPU or large datasets needed</li>
  <li>Ideal for <b>Edge AI</b> and low-power IoT systems</li>
</ul>

---

<h2 align="center">🧩 Conclusion</h2>
<p align="center">
<b>Guardian-Grid</b> merges sensor technology and facial recognition to create a responsive, affordable, and intelligent anti-theft system designed for modern homes and labs.
</p>


