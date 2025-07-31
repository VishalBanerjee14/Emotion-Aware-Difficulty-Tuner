import pygame
import threading
import time
import random

class EmotionBalloonGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Emotion Balloon Game")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Colors
        self.WHITE = (255, 255, 255)
        self.BLUE = (0, 128, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.YELLOW = (255, 255, 0)
        self.PURPLE = (128, 0, 128)
        self.ORANGE = (255, 165, 0)
        self.PINK = (255, 192, 203)
        self.BLACK = (0, 0, 0)
        
        # Balloon properties
        self.balloon_x = 400
        self.balloon_y = 500
        self.balloon_radius = 30
        self.balloon_color = self.BLUE
        self.balloon_speed = 2
        
        # Emotion properties
        self.current_emotion = "neutral"
        self.emotion_lock = threading.Lock()
        self.emotion_colors = {
            'happy': self.YELLOW,
            'sad': self.BLUE,
            'angry': self.RED,
            'surprise': self.ORANGE,
            'fear': self.PURPLE,
            'disgust': self.GREEN,
            'neutral': self.PINK
        }
        
        # Game state
        self.score = 0
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
        
        # Stars (collectibles)
        self.stars = []
        self.star_timer = 0
        
        # Background
        self.bg_color = self.WHITE

    def update_emotion(self, emotion):
        """Update current emotion from emotion detection thread"""
        with self.emotion_lock:
            self.current_emotion = emotion
            self.update_balloon_behavior(emotion)

    def update_balloon_behavior(self, emotion):
        """Update balloon behavior based on emotion"""
        # Change balloon color based on emotion
        self.balloon_color = self.emotion_colors.get(emotion, self.PINK)
        
        # Change balloon speed based on emotion
        if emotion == 'happy':
            self.balloon_speed = 4  # Fast and bouncy
        elif emotion == 'sad':
            self.balloon_speed = 1  # Slow and heavy
        elif emotion == 'angry':
            self.balloon_speed = 5  # Very fast
        elif emotion == 'surprise':
            self.balloon_speed = 6  # Super fast
        elif emotion == 'fear':
            self.balloon_speed = 3  # Medium speed
        elif emotion == 'disgust':
            self.balloon_speed = 2  # Slow
        else:  # neutral
            self.balloon_speed = 2  # Normal speed

    def create_star(self):
        """Create a new star collectible"""
        star = {
            'x': random.randint(50, 750),
            'y': random.randint(50, 550),
            'radius': 15,
            'color': self.YELLOW
        }
        self.stars.append(star)

    def update_stars(self):
        """Update star positions and check collisions"""
        # Create new stars
        self.star_timer += 1
        if self.star_timer > 120:  # Create star every 2 seconds
            self.create_star()
            self.star_timer = 0
        
        # Check collision with stars
        balloon_rect = pygame.Rect(self.balloon_x - self.balloon_radius, 
                                 self.balloon_y - self.balloon_radius,
                                 self.balloon_radius * 2, self.balloon_radius * 2)
        
        for star in self.stars[:]:
            star_rect = pygame.Rect(star['x'] - star['radius'], 
                                  star['y'] - star['radius'],
                                  star['radius'] * 2, star['radius'] * 2)
            if balloon_rect.colliderect(star_rect):
                self.stars.remove(star)
                self.score += 10

    def draw_balloon(self):
        """Draw the balloon with string"""
        # Draw balloon
        pygame.draw.circle(self.screen, self.balloon_color, 
                         (self.balloon_x, self.balloon_y), self.balloon_radius)
        
        # Draw balloon highlight
        pygame.draw.circle(self.screen, self.WHITE, 
                         (self.balloon_x - 8, self.balloon_y - 8), 8)
        
        # Draw string
        pygame.draw.line(self.screen, self.BLACK, 
                        (self.balloon_x, self.balloon_y + self.balloon_radius),
                        (self.balloon_x, self.balloon_y + self.balloon_radius + 50), 3)

    def draw_stars(self):
        """Draw all stars"""
        for star in self.stars:
            pygame.draw.circle(self.screen, star['color'], 
                             (star['x'], star['y']), star['radius'])
            # Draw star points
            points = [
                (star['x'], star['y'] - star['radius']),
                (star['x'] + 5, star['y'] - 5),
                (star['x'] + star['radius'], star['y']),
                (star['x'] + 5, star['y'] + 5),
                (star['x'], star['y'] + star['radius']),
                (star['x'] - 5, star['y'] + 5),
                (star['x'] - star['radius'], star['y']),
                (star['x'] - 5, star['y'] - 5)
            ]
            pygame.draw.polygon(self.screen, star['color'], points)

    def draw_ui(self):
        """Draw user interface"""
        with self.emotion_lock:
            emotion_text = self.font.render(f"Emotion: {self.current_emotion.upper()}", True, self.BLACK)
            score_text = self.font.render(f"Score: {self.score}", True, self.BLACK)
            speed_text = self.font.render(f"Speed: {self.balloon_speed}", True, self.BLACK)
        
        self.screen.blit(emotion_text, (10, 10))
        self.screen.blit(score_text, (10, 50))
        self.screen.blit(speed_text, (10, 90))
        
        # Instructions
        instructions = [
            "Use ARROW KEYS to move the balloon",
            "Collect yellow stars to score points",
            "Your emotions change the balloon's behavior!",
            "Press ESC to quit"
        ]
        
        for i, instruction in enumerate(instructions):
            inst_text = self.font.render(instruction, True, self.BLACK)
            self.screen.blit(inst_text, (10, 500 + i * 30))

    def draw(self):
        """Draw all game elements"""
        self.screen.fill(self.bg_color)
        
        # Draw stars
        self.draw_stars()
        
        # Draw balloon
        self.draw_balloon()
        
        # Draw UI
        self.draw_ui()
        
        pygame.display.flip()

    def run(self):
        """Main game loop"""
        while self.running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            # Handle balloon movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.balloon_x > self.balloon_radius:
                self.balloon_x -= self.balloon_speed
            if keys[pygame.K_RIGHT] and self.balloon_x < 800 - self.balloon_radius:
                self.balloon_x += self.balloon_speed
            if keys[pygame.K_UP] and self.balloon_y > self.balloon_radius:
                self.balloon_y -= self.balloon_speed
            if keys[pygame.K_DOWN] and self.balloon_y < 600 - self.balloon_radius:
                self.balloon_y += self.balloon_speed

            # Update stars
            self.update_stars()

            # Draw everything
            self.draw()

            # Control frame rate
            self.clock.tick(60)

        # Game over screen
        self.show_game_over()
        pygame.quit()

    def show_game_over(self):
        """Show game over screen"""
        self.screen.fill(self.BLACK)
        
        game_over_text = self.big_font.render("GAME OVER!", True, self.WHITE)
        score_text = self.big_font.render(f"Final Score: {self.score}", True, self.WHITE)
        thanks_text = self.font.render("Thanks for playing!", True, self.WHITE)
        
        self.screen.blit(game_over_text, (200, 200))
        self.screen.blit(score_text, (200, 300))
        self.screen.blit(thanks_text, (300, 400))
        
        pygame.display.flip()
        pygame.time.wait(3000)  # Wait 3 seconds

    def stop(self):
        """Stop the game"""
        self.running = False

# Keep the old Game class for backward compatibility
class Game(EmotionBalloonGame):
    pass