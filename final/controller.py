import pygame
import app

# Initialize Pygame and the joystick module
pygame.init()
pygame.joystick.init()

# Check for connected joysticks
if pygame.joystick.get_count() == 0:
    print("No joystick connected.")
    exit()

# Initialize the first joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Connected to joystick: {joystick.get_name()}")

# Main loop to read input
try:
    while True:
        for event in pygame.event.get():
            # Handle button presses
            if event.type == pygame.JOYBUTTONDOWN:
                if event.button == 7:
                    app.right_turn()
                if event.button == 6:
                    app.left_turn()
                if event.button == 12:
                    pygame.quit()
                print(f"Button {event.button} pressed.")
            if event.type == pygame.JOYBUTTONUP:
                if event.button == 7:
                    app.stop()
                if event.button == 6:
                    app.stop()
                print(f"Button {event.button} released.")

            # Handle axis movement (e.g., sticks or triggers)
            if event.type == pygame.JOYAXISMOTION:
                if event.axis == 4:
                    app.forward_turn()
                if event.axis == 5:
                    app.backward_turn()
                print(f"Axis {event.axis} moved to {event.value:.2f}")

except KeyboardInterrupt:
    print("\nExiting program.")

finally:
    pygame.quit()
