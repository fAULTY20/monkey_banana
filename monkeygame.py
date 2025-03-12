import pygame
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Monkey-Banana Problem 🍌🐵")

# Load images
room_img = pygame.image.load("room.png")
room_img = pygame.transform.scale(room_img, (WIDTH, HEIGHT))

monkey_img = pygame.image.load("monkey.png")
monkey_img = pygame.transform.scale(monkey_img, (80, 80))  # Adjusted size

box_img = pygame.image.load("box.png")
box_img = pygame.transform.scale(box_img, (80, 60))  # Adjusted size

banana_img = pygame.image.load("banana.png")
banana_img = pygame.transform.scale(banana_img, (50, 50))  # Adjusted size

# Initial state
monkey_x, monkey_y = 100, 500  # Monkey starts at the door
box_x, box_y = 600, 500  # Box starts at the window
banana_x, banana_y = 400, 180  # Adjusted banana position
on_box = False
has_banana = False

# Game state flags
moving_to_box = True
pushing_box = False
climbing_box = False
grabbed_banana = False

# Main loop
running = True
while running:
    screen.fill((255, 255, 255))  # Clear screen
    screen.blit(room_img, (0, 0))  # Draw room background

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move monkey towards the box
    if moving_to_box:
        if monkey_x < box_x - 10:
            monkey_x += 5  # Increased speed
        elif monkey_x > box_x + 10:
            monkey_x -= 5  # Increased speed
        else:
            moving_to_box = False
            pushing_box = True
            time.sleep(0.3)

    # Push the box to the middle
    if pushing_box:
        if box_x > banana_x - 20:
            box_x -= 5  # Increased speed
            monkey_x -= 5  # Move monkey with box
        elif box_x < banana_x - 20:
            box_x += 5  # Increased speed
            monkey_x += 5  # Move monkey with box
        else:
            pushing_box = False
            climbing_box = True
            time.sleep(0.3)

    # Monkey climbs the box
    if climbing_box:
        if monkey_y > box_y - 50:
            monkey_y -= 5  # Climb gradually
        else:
            climbing_box = False
            grabbed_banana = True
            time.sleep(0.3)

    # Monkey grabs the banana
    if grabbed_banana:
        if monkey_y > banana_y:
            monkey_y -= 5  # Move monkey up towards the banana
        else:
            has_banana = True
            running = False

    # Draw images
    screen.blit(box_img, (box_x, box_y))  # Draw box
    screen.blit(banana_img, (banana_x, banana_y))  # Draw banana
    screen.blit(monkey_img, (monkey_x, monkey_y))  # Draw monkey

    pygame.display.update()  # Refresh screen
    pygame.time.delay(30)  # Increased speed

pygame.quit()

if has_banana:
    print("Monkey reached the bananas...")
else:
    print("Game exited.")