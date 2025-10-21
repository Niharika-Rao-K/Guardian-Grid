<h1 align="center">🛡️ Guardian-Grid</h1>
<h3 align="center" style="color:#8b949e;">An Intelligent IoT-Enabled Anti-Theft Floor Mat with Face Recognition</h3>

<p align="center">
  <i>“Smart detection meets intelligent security — powered by IoT and AI.”</i>
</p>

---

<!-- 👇 Hidden style block (GitHub preview will skip showing it, but CSS still applies) -->

<!--
<style>
  body { font-family: 'Poppins', sans-serif; background-color: #0d1117; color: #e6edf3; line-height: 1.7; }
  h1, h2, h3 { color: #58a6ff; font-weight: 600; }
  h1 { font-size: 2.4em; margin-top: 30px; }
  h3 { color: #8b949e; font-weight: 400; }
  ul li, ol li { margin-bottom: 8px; }
  table { border-collapse: collapse; width: 85%; margin: 20px auto; background-color: #161b22; color: #e6edf3; border-radius: 10px; overflow: hidden; }
  td { border: 1px solid #30363d; padding: 10px 12px; }
  code { background-color: transparent; color: #58a6ff; font-style: italic; }
  p, li { font-size: 1.05em; }
</style>
-->

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
  <li><b>capture_images.py</b> – Captures 20 face images per person and stores them in <code>dataset/</code><br>
      <b>Run:</b> <code>python3 capture_images.py</code></li><br>

  <li><b>train_model.py</b> – Trains the LBPH model using captured faces<br>
      <b>Run:</b> <code>python3 train_model.py</code></li><br>

  <li><b>Face_recog_lbph.py</b> – Performs real-time face recognition<br>
      <b>Run:</b> <code>python3 Face_recog_lbph.py</code></li><br>

  <li><b>recognize_face_sensor.py</b> – Triggers face recognition when the piezo mat detects pressure; 
      sends SMS alerts for unknown faces and logs all detections.<br>
      <b>Run:</b> <code>python3 recognize_face_sensor.py</code></li><br>

  <li><b>dataset/</b> – Stores all captured face images per user.</li>
  <li><b>logs/</b> – Stores timestamped images of detections (recognized and unrecognized).</li>
</ul>

<p align="center">
  <img src="https://github.com/user-attachments/assets/4207c2bc-b0c6-43ee-8599-85fbbbcc7428" width="660" height="400" alt="Guardian Grid System Diagram">
</p>

---

<h2>🤖 Machine Learning Model: LBPH (Local Binary Patterns Histograms)</h2>

<h3>📘 Model Type</h3>
<p>LBPH — a classical computer vision algorithm for facial recognition, optimized for embedded devices.</p>

<h3>💡 Why LBPH?</h3>
<ul>
  <li>Lightweight and fast — ideal for Raspberry Pi.</li>
  <li>Works well with grayscale images and small datasets.</li>
  <li>Robust against lighting and expression variations.</li>
</ul>

<h3>⚙️ How It Works</h3>
<ol>
  <li>Divides an image into small grids.</li>
  <li>Compares each pixel with its neighbors to form binary patterns.</li>
  <li>Builds histograms for each region.</li>
  <li>Concatenates them into a single feature vector.</li>
  <li>Compares new faces using Euclidean or similar distance metrics.</li>
</ol>

<h3>🧠 Training Step</h3>
<p>
Images captured by <code>capture_images.py</code> are labeled and trained using <code>train_model.py</code> with OpenCV’s <code>cv2.face.LBPHFaceRecognizer_create()</code>.
</p>

<h3>🔍 Prediction Step</h3>
<p>
When the piezo sensor detects pressure, <code>recognize_face_sensor.py</code> activates the camera, performs recognition, and logs the result.
</p>

<h3>🚫 No Deep Learning Required</h3>
<ul>
  <li>No GPU or large dataset required.</li>
  <li>Ideal for <b>Edge AI</b> and IoT-based embedded applications.</li>
</ul>

---

<h2 align="center">🧩 Conclusion</h2>
<p align="center">
<b>Guardian-Grid</b> seamlessly merges IoT sensing and AI-based facial recognition to deliver a responsive, real-time, and cost-effective anti-theft system for modern environments.
</p>
