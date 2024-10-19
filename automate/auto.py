import pyautogui
import schedule
import time

def move_mouse_up():
    # Get the current mouse position
    current_x, current_y = pyautogui.position()

    # Define the number of steps for the gradual movement
    num_steps = 100

    # Calculate the distance to move in each step
    step_distance = current_y // num_steps

    # Move the mouse cursor gradually upwards
    for _ in range(num_steps):
        current_y -= step_distance
        pyautogui.moveTo(current_x, current_y)
        time.sleep(0.1)  # Adjust this delay as needed for smooth movement

# Schedule the task to run at 3:00 PM every day
schedule.every().day.at("10:19").do(move_mouse_up)

# Run the scheduler loop
while True:
    schedule.run_pending()
    time.sleep(1)  # Sleep for 1 second to avoid high CPU usage
