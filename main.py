import threading
import time
from emotion_predictor import start_real_time_detection
from game_engine import EmotionBalloonGame

def main():
    print("🎈 Starting Emotion Balloon Game...")
    print("\n🎮 How to Play:")
    print("- Use ARROW KEYS to move the balloon")
    print("- Collect yellow stars to score points")
    print("- Your emotions change the balloon's color and speed!")
    print("- Press ESC to quit the game")
    print("- Press 'q' to quit emotion detection")
    print("\n😊 Emotions affect the balloon:")
    print("- HAPPY: Yellow balloon, fast movement")
    print("- SAD: Blue balloon, slow movement")
    print("- ANGRY: Red balloon, very fast")
    print("- SURPRISE: Orange balloon, super fast")
    print("- FEAR: Purple balloon, medium speed")
    print("- DISGUST: Green balloon, slow")
    print("- NEUTRAL: Pink balloon, normal speed")
    print("\nInitializing...")
    
    # Create game instance
    game = EmotionBalloonGame()
    
    # Create emotion detection thread
    def emotion_callback(emotion):
        """Callback function to update game with detected emotion"""
        game.update_emotion(emotion)
    
    # Start emotion detection in a separate thread
    emotion_thread = threading.Thread(
        target=start_real_time_detection, 
        args=(emotion_callback,),
        daemon=True
    )
    
    try:
        # Start emotion detection
        print("📷 Starting emotion detection...")
        emotion_thread.start()
        
        # Give emotion detection a moment to initialize
        time.sleep(2)
        
        print("🎈 Starting balloon game...")
        print("Game is now running! Show different emotions to see how the balloon changes!")
        
        # Run the game
        game.run()
        
    except KeyboardInterrupt:
        print("\n🛑 Stopping game...")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        # Clean up
        game.stop()
        print("👋 Game stopped. Thanks for playing!")

if __name__ == "__main__":
    main()