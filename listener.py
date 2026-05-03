from pynput import keyboard
from shortcut_manager import load_shortcuts
from actions import execute_action

held_keys = set()
data=load_shortcuts()


#converts ctrl alt y into a set we can compare against held keys 
def parse_shortcut(keys_str):
    parsed_result = set()
    for part in keys_str.lower().split("+"):
        part = part.strip()
        if part =="ctrl":
            parsed_result.add(keyboard.Key.ctrl_l)

        elif part == "alt":
            parsed_result.add(keyboard.Key.alt_l)
        
        elif part == "shift":
            parsed_result.add(keyboard.Key.shift_l)
        
        else:#might need more of these cases if we add more key binds
            parsed_result.add(keyboard.KeyCode.from_char(part))
        return parsed_result

#on press of a key add it to the set of held keys 
#if the keys held == parsed_shortcuts so if you hold 
#ctrl + n + W the parsed version would be ctrl n w 
#if they are equal i.e. [ctrl n w] == [ctrl n w]
#execute the action
def on_press(key):
    held_keys.add(key)
    for shortcut in data["shortcuts"]:
        if held_keys == parse_shortcut(shortcut["keys"]):
            execute_action(shortcut["type"], shortcut["action"])

#once you lift your finger off that key we do not care about it 
#becuase it can not be used for a shortcut 
#so remove the key from the set. 
def on_release(key):
    held_keys.discard(key)#cant use remove becuase it can cauase an error i believe


def main():
    listen = keyboard.Listener(on_press=on_press, on_release=on_release)
    listen.start()

    while listen.is_alive():
        pass

if __name__ == "__main__":
    main()