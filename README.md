# Project_6
Advanced Customizable Keyboard Shortcut Mapping Device Driver

April 14th - Progress Report 

* Set up the project structure with a GitHub repo, .gitignore, and Python 3.13 with tkinter configured on Mac

* Built shortcut_manager.py to handle data operations — loading, saving, adding, editing, and deleting shortcuts stored in a        shortcuts.json config file with auto-incrementing IDs

* Built a tkinter GUI with input fields, an action type dropdown, Save and Delete buttons, and a Listbox that displays all registered shortcuts and refreshes automatically after every change

* Separated the app into main.py (entry point, owns the window) and gui.py (all UI logic), structured so additional modules like a keyboard listener can be plugged in later
