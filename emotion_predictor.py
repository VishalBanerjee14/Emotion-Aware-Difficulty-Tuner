import cv2
import numpy as np
from tensorflow.keras.models import load_model
import os

EMOTIONS = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

# Load the trained model
model_path = 'model/emotion_model.h5'
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}. Please train the model first.")

model = load_model(model_path)

# Load face detection cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def get_emotion_from_frame(frame):
    """Extract emotion from a single frame"""
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    if len(faces) == 0:
        return "neutral", None
    
    # Get the largest face
    largest_face = max(faces, key=lambda x: x[2] * x[3])
    x, y, w, h = largest_face
    
    roi = gray[y:y+h, x:x+w]
    roi = cv2.resize(roi, (48, 48))
    roi = roi.reshape(1, 48, 48, 1) / 255.0
    
    preds = model.predict(roi, verbose=0)[0]
    emotion = EMOTIONS[np.argmax(preds)]
    
    return emotion, largest_face

def start_real_time_detection(callback=None):
    """Start real-time emotion detection with optional callback"""
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera")
        return
    
    print("Real-time emotion detection started. Press 'q' to quit.")
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame")
                break
            
            emotion, face_coords = get_emotion_from_frame(frame)
            
            # Draw face rectangle and emotion text on frame
            if face_coords is not None:
                x, y, w, h = face_coords
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, emotion.upper(), (x, y-10), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            
            # Display the frame
            cv2.imshow('Emotion Detection', frame)
            
            # Call callback function if provided
            if callback:
                callback(emotion)
            
            # Break loop on 'q' press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    except KeyboardInterrupt:
        print("\nStopping emotion detection...")
    finally:
        cap.release()
        cv2.destroyAllWindows()

def get_emotion():
    """Legacy function for single emotion detection"""
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        return "neutral"

    emotion, _ = get_emotion_from_frame(frame)
    return emotion

if __name__ == "__main__":
    # Test the real-time detection
    start_real_time_detection()