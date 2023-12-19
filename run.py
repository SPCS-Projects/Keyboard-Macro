import keyboard
import time
import random
import threading

variation_range = 0.01


def pause():
    keyboard.wait("scrlk")
    return


def run_keyboard_macro(file_path):
    print("Press 'scroll' to start the macro and 'pause' to stop it")

    try:

        keyboard.wait("scrlk")  # Wait for 'scroll lock' key press
        print("Starting macro")
        # thread = threading.Thread(target=feed_pet)
        # thread.start()
        with open(file_path, 'r') as file:
            events = [line.strip().split(',') for line in file]
            keys_held_down = set()
            while True:
                for event_type, key in events:
                    if event_type == 'down':
                        keyboard.press(key)
                        keys_held_down.add(key)
                    elif event_type == 'up':
                        keyboard.release(key)
                        keys_held_down.discard(key)
                    elif event_type == 'delay':
                        time.sleep(float(key))
                    if keyboard.is_pressed("pause break"):
                        print("Pausing Script, start again by holding scrlk")
                        for key in keys_held_down:
                            keyboard.release(key)
                        pause()
                        print("Continuing Script")
                        break


    except KeyboardInterrupt:
        print("Keyboard macro execution stopped.")
        # thread.join() #wait for the pet feed thread to finish


if __name__ == "__main__":
    keyboard_macro_file = "keyboard_macro.txt"
    run_keyboard_macro(keyboard_macro_file)

