# 🎈 Emotion Balloon Game

A fun and simple Python game where your emotions control a colorful balloon! The balloon changes color and speed based on your real-time emotions detected through your webcam.

## ✨ Features

- **Real-time emotion detection** using your webcam
- **7 emotion categories**: Angry, Disgust, Fear, Happy, Sad, Surprise, Neutral
- **Dynamic balloon behavior** that changes color and speed based on your emotions
- **Simple and intuitive gameplay** - just collect stars!
- **Threaded architecture** for smooth real-time performance
- **Beautiful visual feedback** with emotion-based colors

## 🎮 How to Play

1. **Move the balloon** using arrow keys
2. **Collect yellow stars** to score points
3. **Show different emotions** to see the balloon change:
   - 😊 **HAPPY**: Yellow balloon, fast movement
   - 😢 **SAD**: Blue balloon, slow movement  
   - 😠 **ANGRY**: Red balloon, very fast
   - 😲 **SURPRISE**: Orange balloon, super fast
   - 😨 **FEAR**: Purple balloon, medium speed
   - 🤢 **DISGUST**: Green balloon, slow
   - 😐 **NEUTRAL**: Pink balloon, normal speed

## 📋 Requirements

- Python 3.10.11 (required for TensorFlow compatibility)
- Webcam
- Virtual environment (recommended)

## 🚀 Installation

1. **Activate your virtual environment:**
   ```bash
   # Windows
   emo-env\Scripts\activate
   
   # Linux/Mac
   source emo-env/bin/activate
   ```

2. **Install required packages:**
   ```bash
   pip install tensorflow opencv-python pygame numpy
   ```

## ⚙️ Setup

1. **Train the model** (if not already trained):
   ```bash
   python train_model.py
   ```
   This will create `model/emotion_model.h5` using the FER dataset.

2. **Test emotion detection:**
   ```bash
   python test_emotion.py
   ```
   This will verify that your camera and model are working correctly.

3. **Start the game:**
   ```bash
   python main.py
   ```

## 🎯 Game Controls

- **Arrow Keys**: Move the balloon in all directions
- **ESC**: Quit the game
- **'q'**: Quit emotion detection window

## 📁 Project Structure

```
Game/
├── main.py                 # Main game launcher
├── train_model.py          # Model training script
├── emotion_predictor.py    # Real-time emotion detection
├── game_engine.py          # Balloon game logic and rendering
├── test_emotion.py         # Testing script
├── model/
│   └── emotion_model.h5    # Trained emotion model
└── FER dataset/            # Training dataset
    ├── train/
    └── test/
```

## 🔧 Troubleshooting

### Common Issues

1. **Camera not working:**
   - Make sure your webcam is connected and not in use by another application
   - Try running `python test_emotion.py` to test camera access

2. **Model not found:**
   - Run `python train_model.py` to train the model
   - Make sure the FER dataset is in the correct location

3. **TensorFlow errors:**
   - Ensure you're using Python 3.10.11
   - Make sure you're in the virtual environment
   - Reinstall TensorFlow if needed: `pip install tensorflow==2.13.0`

4. **Performance issues:**
   - Close other applications using the camera
   - Make sure you have good lighting for emotion detection

### Error Messages

- **"Model file not found"**: Run `python train_model.py`
- **"Could not open camera"**: Check webcam connection and permissions
- **"Training dataset not found"**: Ensure FER dataset is in the project directory

## 🎨 Technical Details

- **Emotion Detection**: Uses CNN trained on FER2013 dataset
- **Face Detection**: OpenCV Haar Cascade Classifier
- **Game Engine**: Pygame for graphics and input handling
- **Threading**: Separate threads for emotion detection and game rendering
- **Model Architecture**: Convolutional Neural Network with 2 Conv layers

## 🎉 Why This Game is Better

- **Simple concept**: Just move a balloon and collect stars
- **Clear visual feedback**: Balloon color changes with emotions
- **Intuitive controls**: Standard arrow key movement
- **No complex mechanics**: No obstacles to avoid or lives to lose
- **Educational**: Learn how emotions affect behavior
- **Fun for all ages**: Simple enough for kids, interesting for adults

## 🤝 Contributing

Feel free to improve the game mechanics, add new features, or enhance the emotion detection accuracy!

## 📄 License

This project is for educational purposes. The FER dataset is publicly available for research use.