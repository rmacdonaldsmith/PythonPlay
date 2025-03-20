import pygame
import random

# Initialize pygame
pygame.init()

# Constants
GRID_SIZE = 20
CELL_SIZE = 20
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (0, 0, 0)
SNAKE_SPEED = 5

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Initialize window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

def generate_food(snake_body):
    while True:
        food = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        if food not in snake_body:
            return food

def draw_snake(snake_body):
    for segment in snake_body:
        pygame.draw.rect(screen, SNAKE_COLOR, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_food(food):
    pygame.draw.rect(screen, FOOD_COLOR, (food[0] * CELL_SIZE, food[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def main():
    snake = [(GRID_SIZE // 2, GRID_SIZE // 2)]
    direction = RIGHT
    food = generate_food(snake)
    running = True

    while running:
        screen.fill(BACKGROUND_COLOR)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w) and direction != DOWN:
                    direction = UP
                elif event.key in (pygame.K_DOWN, pygame.K_s) and direction != UP:
                    direction = DOWN
                elif event.key in (pygame.K_LEFT, pygame.K_a) and direction != RIGHT:
                    direction = LEFT
                elif event.key in (pygame.K_RIGHT, pygame.K_d) and direction != LEFT:
                    direction = RIGHT
        
        # Move snake
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        
        # Check collisions
        if new_head in snake or not (0 <= new_head[0] < GRID_SIZE and 0 <= new_head[1] < GRID_SIZE):
            running = False  # Game over
        else:
            snake.insert(0, new_head)
            if new_head == food:
                food = generate_food(snake)  # Generate new food
            else:
                snake.pop()  # Remove tail
        
        # Draw everything
        draw_snake(snake)
        draw_food(food)
        pygame.display.flip()
        clock.tick(SNAKE_SPEED)
    
    pygame.quit()

if __name__ == "__main__":
    main()
