#!/usr/bin/env python3
"""
Simple test script to verify emotion detection is working
"""

import os
import sys
from emotion_predictor import get_emotion, start_real_time_detection

def test_single_emotion():
    """Test single emotion detection"""
    print("Testing single emotion detection...")
    print("Please look at the camera for 3 seconds...")
    
    try:
        emotion = get_emotion()
        print(f"Detected emotion: {emotion}")
        return True
    except Exception as e:
        print(f"Error in single emotion detection: {e}")
        return False

def test_real_time():
    """Test real-time emotion detection"""
    print("\nTesting real-time emotion detection...")
    print("Press 'q' to quit the real-time test")
    
    try:
        start_real_time_detection()
        return True
    except Exception as e:
        print(f"Error in real-time emotion detection: {e}")
        return False

def check_dependencies():
    """Check if all required files exist"""
    print("Checking dependencies...")
    
    # Check if model exists
    if not os.path.exists('model/emotion_model.h5'):
        print("❌ Model file not found. Please run train_model.py first.")
        return False
    else:
        print("✅ Model file found")
    
    # Check if dataset exists
    if not os.path.exists('FER dataset/train'):
        print("❌ Training dataset not found.")
        return False
    else:
        print("✅ Training dataset found")
    
    return True

def main():
    print("=== Emotion Detection Test ===")
    
    # Check dependencies
    if not check_dependencies():
        print("\nPlease fix the missing dependencies before running the game.")
        return
    
    print("\nStarting tests...")
    
    # Test single emotion detection
    if test_single_emotion():
        print("✅ Single emotion detection works!")
    else:
        print("❌ Single emotion detection failed!")
        return
    
    # Ask user if they want to test real-time
    response = input("\nDo you want to test real-time emotion detection? (y/n): ")
    if response.lower() == 'y':
        test_real_time()
    
    print("\n✅ All tests completed! You can now run main.py to start the game.")

if __name__ == "__main__":
    main()