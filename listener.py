from pynput import keyboard
from shortcut_manager import load_shortcuts
from actions import execute_action

held_keys = set()

def on_press(key):
    held_keys.add(key)
    print("keys pressed: "+ held_keys)

def on_release(key):
    held_keys.discard(key)#cant use remove becuase it can cauase an error i believe


def main():
    data=load_shortcuts()
    listen = keyboard.Listener(on_press=on_press, on_release=on_release)
    listen.start()

    while listen.is_alive():
        pass

if __name__ == "__main__":
    main()