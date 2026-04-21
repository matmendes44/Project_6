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
"""data = {
    "shortcuts": [
        {
            "id": 1,
            "keys": "Ctrl+Alt+Y",
            "type": "Open a Web Page",
            "action": "https://youtube.com",
            "description": "Opens YouTube"
        },
        {
            "id": 2,
            "keys": "Ctrl+Alt+G",
            "type": "Open a Web Page",
            "action": "https://github.com",
            "description": "Opens GitHub"
        }
    ],
    "next_id": 3
}
"""
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
    for myDict in data["shortcuts"]:#if the keybind already exist you cant add another keybind with the same binding
        if myDict["keys"] == keys:
            print("shortcut "+keys+" already exists")
            return None
        if myDict["action"] == action:
            print("action " +action + " already exist")
            return None
    
    
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



def edit_shortcut(shortcut_id, keys=None, action_type=None, action=None, description=None):
    data=load_shortcuts()

    # each shortcut is stored as a dictionary inside data["shortcuts"] -> we are just inside the shortcuts index
    # example:
    # myDict = {
    #     "id": 1,                          <- unique ID number
    #     "keys": "Ctrl+Alt+Y",             <- keybind combination
    #     "type": "Open a Web Page",        <- action type
    #     "action": "https://youtube.com",  <- what gets executed
    #     "description": "Opens YouTube"    <- label for the user
    # }

    for myDict in data["shortcuts"]:
        if myDict["id"] == shortcut_id:
            if keys is not None: #is not empty 
                myDict["keys"] = keys
            if action_type is not None:
                myDict["type"] = action_type
            if action is not None:
                myDict["action"] = action
            if description is not None:
                myDict["discription"] = description
    save_shortcuts(data)
    print("")

def delete_shortcut(shortcut_id):
    data = load_shortcuts()

    #iterating over dictionary of data to search the key, "shortcuts" to iterate over the shortcuts
    for myDict in data["shortcuts"]:
        if myDict["id"] == shortcut_id:
            data["shortcuts"].remove(myDict)
            save_shortcuts(data)
            print("Shortcut " + str(shortcut_id) +" deleted.")
            return True
    print("No shortcut found with ID " + str(shortcut_id))
    return False

    

def main():
    #if needed for readablility add formatted print statements
    #keyword or value :>5 for each print statements varaibles and strings

    
    print("    Listing current shortcuts    ")
    list_shortcuts()

    #print adding new shortcut 
    
    #add shortcut for something like youtube.com 
    add_shortcut("Ctrl+Alt+Y", "Open a Web Page", "https://youtube.com", "Opens YouTube")
    add_shortcut("Ctrl+Alt+G", "Open a Web Page", "https://github.com", "Opens GitHub")

    #test adding a duplicate keybind but for a differnt link or action

    print("    Listing after add    ")
    list_shortcuts()

    print( "edit shortcut 1" )
    edit_shortcut(1, keys="ctrl+alt+z")
    #edit_shortcut

    #print remove shortcut id 2 
    #remove_shortcut(2)
    print( "removed shortcut 2" )
    delete_shortcut(2)

    print("    Final shortcut list    ")
    list_shortcuts()
    
if __name__ == "__main__":
    main()