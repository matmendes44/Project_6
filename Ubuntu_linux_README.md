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

## Issues
Global keyboard listening is limited inside a VirtualBox VM, shortcuts only fire when the app window is focused. This is a VM-level restriction. Normally pynput captures keys globally in the background as intended.