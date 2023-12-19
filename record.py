from pynput.keyboard import Key, Listener
import logging
import keyboard, sys, os
import time

on_press_previous = time.time()
current_key = ""
log_dir = ""
file_base = "keyboard_macro"
file_extension = ".txt"
index = 1

while os.path.exists(f"{log_dir}{file_base}{index}{file_extension}"):
    index += 1
file_name = f"{log_dir}{file_base}{index}{file_extension}"

#os.isdir(log_dir + 'keyboard_macro.txt'
#os.remove(log_dir + 'keyboard_macro.txt')
logging.basicConfig(filename=file_name, level=logging.DEBUG, format='%(message)s')


def on_press(key):
    global on_press_previous
    global current_key
    if (current_key != str(key)+" down") and ("scroll_lock" not in str(key)) and ("pause" not in str(key))):
        current_key = str(key)+" down"
        on_press_current = time.time()
        delta = round(on_press_current - on_press_previous, 5)
        on_press_previous = on_press_current
        logging.info('delay,{0}'.format(delta))
        if "ctrl" in str(key):
            logging.info('down,ctrl')
        else:
            logging.info('down,{0}'.format(str(key).replace("'", "").replace("Key.", "")))
    
    if keyboard.is_pressed("pause break"):
        sys.exit()


def on_release(key):
    global on_press_previous
    global current_key
    if (current_key != str(key)+" up") and ("scroll_lock" not in str(key)) and ("pause" not in str(key))):
        current_key = str(key)+" up"
        on_press_current = time.time()
        delta = round(on_press_current - on_press_previous, 5)
        on_press_previous = on_press_current
        logging.info('delay,{0}'.format(delta))
        if "ctrl" in str(key):
            logging.info('down,ctrl')
        else:
            logging.info('up,{0}'.format(str(key).replace("'", "").replace("Key.", "")))
    
    if keyboard.is_pressed("scrlk"):
        sys.exit()


if __name__ == "__main__":
    print("Press 'scroll lock' to start the listener and pause to stop it")
    keyboard.wait("scrlk")  # Wait for 'scroll lock' key press
    print("Starting recording")

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    print("Macro execution stopped.")

