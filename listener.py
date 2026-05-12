from pynput import keyboard
from shortcut_manager import load_shortcuts
from actions import execute_action
import threading # add for the hold timer 

held_keys = set()
hold_timers = {}

# Each modifier name maps to ALL pynput keys that count as that modifier.
# Left/right variants are different objects in pynput so we make them the same characters here.
MODIFIERS = {
    "ctrl":  {keyboard.Key.ctrl_l,  keyboard.Key.ctrl_r},
    "alt":   {keyboard.Key.alt_l,   keyboard.Key.alt_r, keyboard.Key.alt_gr},
    "shift": {keyboard.Key.shift_l, keyboard.Key.shift_r},
    "cmd":   {keyboard.Key.cmd,     keyboard.Key.cmd_l, keyboard.Key.cmd_r},
}

# Convert a shortcut string into a list of "requirements".
# Each requirement is a SET of keys
# So "ctrl + y" becomes {ctrl_l, ctrl_r} and "y" becomes {KeyCode('y')}.
def parse_shortcut(keys_str):
    requirements = []
    for part in keys_str.lower().split("+"):
        part = part.strip()
        if part in MODIFIERS:
            requirements.append(MODIFIERS[part])
        else:
            requirements.append({keyboard.KeyCode.from_char(part)})
    return requirements

# Every requirement must have at least one of its keys currently held.
def matches(requirements, held):
    return all(req & held for req in requirements)

def on_press(key):
    held_keys.add(key)
    # Reload on every press so for GUI-added shortcuts to work we wont need to restart
    data = load_shortcuts()
    for shortcut in data["shortcuts"]:
        try:
            if matches(parse_shortcut(shortcut["keys"]), held_keys):
                execute_action(shortcut["type"], shortcut["action"])
            
            ##added for hold timer
            hold_seconds = shortcut.get("hold_seconds")
            if hold_seconds:
                sindex = shortcut["id"]
                if sindex not in hold_timers:
                    t=threading.Timer(float(hold_seconds), execute_action, args=[shortcut["type"], shortcut["action"]])

                    t.start()
                    hold_timers[sindex] = t
            else:
                execute_action(shortcut["type"], shortcut["action"])
        except Exception as e:
            # One bad shortcut won't kill the listener thread
            print(f"Error with shortcut {shortcut['keys']}: {e}")

def on_release(key):
    held_keys.discard(key)
    
    #added for hold timer 
    data=load_shortcuts()
    for shortcut in data["shortcut"]:
        sindex = shortcut["id"]
        if sindex in hold_timers:
            try:
                still_held = matches(parse_shortcut(shortcut["keys"]), held_keys)

            except Exception:
                still_held = False
            
            if not still_held:
                hold_timers[sindex].cancel()
                del hold_timers[sindex]

def start_listener():
    """Non-blocking - returns immediately, listener runs in background thread."""
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()
    return listener

def main():
    listener = start_listener()
    listener.join()  # blocks if you run this file standalone

if __name__ == "__main__":
    main()