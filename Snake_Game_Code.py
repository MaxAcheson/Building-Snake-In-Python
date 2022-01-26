import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()
score_font = pygame.font.Font('Retro Gaming.ttf', 25)

# Use all caps to create constant variables that cannot be altered in the future
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4
    
Point = namedtuple('Point', 'x, y')

# Color selection using RGP configuration
WHITE = (255, 255, 255)
RED = (200,0,0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 120, 255)
BLACK = (0,0,0)

BLOCK_SIZE = 20
SPEED = 12

class SnakeGame:
    
    def __init__(self, w=700, h=500):
        self.w = w
        self.h = h
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake in Python!')
        self.clock = pygame.time.Clock()
        
        # init game state
        self.direction = Direction.RIGHT
        
        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head, 
                      Point(self.head.x-BLOCK_SIZE, self.head.y),
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)]
        
        self.score = 0
        self.snack = None
        self.place_snack()
        
    def place_snack(self):
        x = random.randint(0, (self.w-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE 
        y = random.randint(0, (self.h-BLOCK_SIZE )//BLOCK_SIZE )*BLOCK_SIZE
        self.snack = Point(x, y)
        if self.snack in self.snake:
            self.place_snack()
        
    def play_step(self):
        # User Controls for Snake movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN
        
        # Snake Movement
        self.move(self.direction) # update the head
        self.snake.insert(0, self.head)
        
        # End game after collision
        game_over = False
        if self.is_collision():
            game_over = True
            return game_over, self.score
            
        # Place new food after collection + move food if it generates within the snake body
        if self.head == self.snack:
            self.score += 1
            self.place_snack()
        else:
            self.snake.pop()
        
        # update ui and clock
        self.update_ui()
        self.clock.tick(SPEED)
        # 6. return game over and score
        return game_over, self.score
    
    def is_collision(self):
        # Boundary collision controls
        if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h - BLOCK_SIZE or self.head.y < 0:
            return True
        # Snake self-collision controls
        if self.head in self.snake[1:]:
            return True
        
        return False
        
    def update_ui(self):
        self.display.fill(BLACK)
        # Define snake coloration, with lighter blue (BLUE2) inside the snake cubes
        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, 12, 12))
        #Define snack color to be solid red    
        pygame.draw.rect(self.display, RED, pygame.Rect(self.snack.x, self.snack.y, BLOCK_SIZE, BLOCK_SIZE))
        
        text = score_font.render("Score: " + str(self.score), True, WHITE)
        self.display.blit(text, [0, 0])
        pygame.display.flip()
        
    def move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
            
        self.head = Point(x, y)
            

if __name__ == '__main__':
    game = SnakeGame()
    
    # game loop
    while True:
        game_over, score = game.play_step()
        
        if game_over == True:
            break
        
    print('Final Score', score)
        
        
    pygame.quit()
