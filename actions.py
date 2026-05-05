#actions.py executes the registered shortcut's action (executes the shortcuts keybind and works)


import subprocess
import webbrowser
import platform


def execute_action(action_type, action_val):
    if action_type in ("url", "Open a Web Page"):
        webbrowser.open(action_val)
    elif action_type in ("app", "Launch an Application"):
        if platform.system() == "Darwin":
            # macOS: 'open -a' launches an app by name (e.g., "Terminal", "Firefox")
            subprocess.Popen(["open", "-a", action_val])
        else:
            subprocess.Popen([action_val])
    elif action_type in ("command", "Run a Custom Command"):
        subprocess.Popen(action_val, shell=True)
    else:
        raise ValueError(f"Unknown action type: {action_type}")

#def main():
    #execute_action("url", "https://www.youtube.com")
    #execute_action("app", "firefox")
    #execute_action("command", "echo hello")


#if __name__ == "__main__":
    #main()