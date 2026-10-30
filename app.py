from flask import Flask, render_template, Response, request, jsonify
import cv2
import mediapipe as mp
import numpy as np

app = Flask(__name__)

# Homepage multipurpose theme
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health_scan():
    return render_template('health_scan.html')

@app.route('/factory')
def factory_monitor():
    return render_template('factory_monitor.html')

@app.route('/sign')
def sign_language_page():
    return render_template('sign_language.html')

@app.route('/advanced')
def advanced_health():
    return render_template('advanced_health.html')

@app.route('/whisper')
def whisper_page():
    return render_template('whisper_voice.html')

# VIDEO FEEDS
mp_pose = mp.solutions.pose
mp_hands = mp.solutions.hands
mp_face = mp.solutions.face_mesh

def gen_factory_monitor():
    cap = cv2.VideoCapture(0)
    pose = mp_pose.Pose()
    face_mesh = mp_face.FaceMesh()
    while True:
        ret, frame = cap.read()
        if not ret: break
        # 1. Body dotted lines
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb)
        if results.pose_landmarks:
            for lm in results.pose_landmarks.landmark:
                h,w,_ = frame.shape
                cv2.circle(frame, (int(lm.x*w), int(lm.y*h)), 3, (0,255,0), -1)
            # Check working or not - movement detection
            # 2. PPE detection - YOLO (helmet, gloves, shoes)
            # 3. Mobile distraction - if phone in hand
            # 4. Workstation objects
        _, buf = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + buf.tobytes() + b'\r\n')

@app.route('/video_factory')
def video_factory():
    return Response(gen_factory_monitor(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
