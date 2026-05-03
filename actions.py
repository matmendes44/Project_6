#actions.py executes the registered shortcut's action (executes the shortcuts keybind and works)

import subprocess #runs outer programs like launching the app or running a script
import webbrowser #opens URLS in the users defualt browser

#
def execute_action (action_type, action_val):
    if action_type == "url":
        webbrowser.open(action_type)
    elif action_type == "app":
        subprocess.Popen([action_val])
    elif action_type == "command":
        subprocess.Popen(action_val, shell=True)
    else:
        raise ValueError("Unknown action type: ", action_type)
    

def main():
    execute_action("url", "https://www.youtube.com")


if __name__ == "__main__":
    main()