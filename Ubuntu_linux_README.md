# Keyboard Shortcut Manage
## Ubuntu Linux compile instructions 

## Set up
- open git bash
- git clone <repo-url>
- cd Project_6
- python3 -m venv venv (create the venv)
- source venv/bin/activate (activate the venv)
- pip install pynput

## Run 
- python3 main.py

# Issues
If shortcuts only work when the app is focused, run:
- sudo usermod -a -G input $USER

then log out and back in 

