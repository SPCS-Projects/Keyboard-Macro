# Keyboard Macro

## Introduction
This repository contains Python scripts for recording and playing back keyboard macros. The project consists of three main files:

1. **record.py**: Records keyboard inputs, delays between key presses, and up/down states. It saves recordings to files named "keyboard_macro1.txt," "keyboard_macro2.txt," and so on, incrementing with each recording.

2. **run.py**: Reads a specified keyboard macro file (default is "keyboard_macro.txt") and executes the recorded key presses and delays using the keyboard library.

3. **keyboard_inputs.py**: Provides a list of all valid key names recognized by the keyboard library, useful for manual editing of the recorded macro file.

## Dependencies
- This project requires the `pynput` and `keyboard` libraries, you can install them using the command `pip install -r requirements.txt` with the requirements.txt provided in this repository

## Usage

### Recording a Macro
1. Run `record.py`.
2. Press the scroll key to start recording.
3. Press the pause key to stop recording.
4. The recording is saved to a file named "keyboard_macro1.txt," "keyboard_macro2.txt," and so on, incrementally.

### Playing Back a Macro
1. Edit the "keyboard_macro.txt" file if needed.
2. Run `run.py` to execute the recorded macro.
4. Press the scroll key to start playing the macro.
5. Press the pause key to stop it, and scroll key again to restart.

### Valid Key Names
Run `keyboard_inputs.py` to print a list of valid key names recognized by the keyboard library.

## Notes
- Feel free to rename the macro file or specify a different file name in the scripts.

- Be cautious when recording or executing macros, especially in sensitive environments.

