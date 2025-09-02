# Mouse Cursor Control Using Eye Movements and Voice Commands

This project allows users to control a **computer mouse cursor using eye movements**  
and interact with applications/websites through **voice commands**.  
It is aimed at providing accessibility solutions for people with disabilities.  

The project was presented at an **International Conference on Sustainable Development Goals (SDGs)**.

---

##  Features
-  Real-time **eye movement tracking** using webcam to move the cursor  
-  **Mouth detection step** → mouth open/close once to initialize face recognition  
-  **Voice command support**: open apps & websites by speaking commands  
-  Accessibility-focused solution for users with limited mobility  
-  Built using **Computer Vision + Speech Recognition**

---

**Tech Stack**

- **Python**
- **OpenCV** – for real-time image processing and eye detection
- **TensorFlow** – for deep learning model support
- **NumPy** – for numerical computations
- **CNN** (Convolutional Neural Networks) – for machine learning & deep learning based eye movement detection
- **PyAutoGUI** – to control mouse actions programmatically
- **SpeechRecognition (Python Library)** – for handling voice commands

---

##  How to Run (PyCharm)
1. Open this project in **PyCharm**.
2. In the bottom panel, open the **Terminal**.
3. First, run the mouse control script:
   ```bash
   python mouse-cursor-control.py

A webcam window will open.
Step 1: Open and close your mouth once → this initializes face detection.
Step 2: Eye tracking starts → you can now move the cursor using your eyes.
To stop the program, press CTRL + C in the terminal.

To start voice commands, run:
   ```bash
   python voice.py

It will ask: “What do you want?”
Say one of the supported commands.
Command	Action Performed
YouTube	- Opens YouTube in browser
Google	- Opens Google in browser
Notepad	- Opens Notepad application

Acknowledgment

**This project was presented at a 2-day International Conference on Sustainable Development Goals (SDGs)
and received certification for its contribution to accessibility solutions.**




Author

Sahana Afrin A
Junior Web Developer & Designer
Passionate about building accessible tech & innovative solutions

