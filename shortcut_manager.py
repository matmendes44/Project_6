"""
shortcut_manager.py

handles loading, saving, adding, editing, and deleting keyboard
shortcuts from the config file, shortcuts.json

"""

import json
import os

config_file = "shortcuts.json"


def load_shortcuts():
    if not(os.path.exists(config_file)):
        #create a new config if none exist
        default = {"shortcuts": [], "next_id": 1}
        save_shortcuts(default)
        return default
    
    with open(config_file, "r") as file:
        return json.load(file)

#data is dictionary
def save_shortcuts(data):
    #save shortcuts to the json config file
    with open(config_file, "w") as file:
        json.dump(data, file, indent=4)

def list_shortcuts():
    #print all shortcuts to the console
    data = load_shortcuts()
    shortcuts= data["shortcuts"]

    if not(shortcuts):
        print("No shortcuts found.\n")
        return None
    print("\nID | Keys | Type | Action | Description")
    print("-" * 50)
    
    for i in shortcuts:#add format printing for better communication
        print(str(i["id"]) + " | " + i["keys"] + " | " + i["type"] + " | " + i["action"] + " | " + i["description"])
    print()

# Adds shortcuts to the JSON file 
def add_shortcut(keys, action_type, action, description=""):
    data = load_shortcuts()
    
    new_shortcut = {
        "id": data["next_id"],
        "keys": keys,
        "type": action_type,
        "action": action,
        "description": description
    }
    
    data["shortcuts"].append(new_shortcut)
    data["next_id"] += 1
    
    save_shortcuts(data)
    print(f"Shortcut '{keys}' added with ID {new_shortcut['id']}")



#def edit_shortcut(shortcut_id, keys=None, action_type=None, action=None, discription=None):

#def delete_shortcut(shortcut_id):

def main():
    print("    Listing current shortcuts    ")
    list_shortcuts()

    #print adding new shortcut 
    
    #add shortcut for something like youtube.com 
    add_shortcut("Ctrl+Alt+Y", "Open a Web Page", "https://youtube.com", "Opens YouTube")
    add_shortcut("Ctrl+Alt+G", "Open a Web Page", "https://github.com", "Opens GitHub")

    #test adding a duplicate keybind but for a differnt link or action

    print("    Listing after add    ")
    list_shortcuts()

    #print edit shortcut 1 
    #edit_shortcut

    #print remove shortcut id 2 
    #remove_shortcut(2)

    print("    Final shortcut list    ")
    list_shortcuts()

if __name__ == "__main__":
    main()