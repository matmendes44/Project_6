import tkinter as tk
from tkinter import messagebox
import shortcut_manager as sm

class ShortcutApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Shortcut Manager")
        self.root.geometry("600x500")
       # self.root.eval('tk::PlaceWindow . center')

        #  Action Input Section for Users 
        tk.Label(root, text="Key Combination Input:").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.keyboard_input = tk.Entry(root, width=30)
        self.keyboard_input.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Action Type:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.action_var = tk.StringVar(value="Open a Web Page")
        action_dropdown = tk.OptionMenu(root, self.action_var, "Open a Web Page", "Launch an Application", "Run a Custom Command")
        action_dropdown.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        tk.Label(root, text="Action Value:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.action_entry = tk.Entry(root, width=30)
        self.action_entry.grid(row=2, column=1, padx=10, pady=10)

        #for hold timer
        tk.Label(root, text="Hold Duration (seconds):").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.hold_entry = tk.Entry(root, width=10)
        self.hold_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        tk.Label(root, text="(leave blank for normal shortcut)").grid(row=3, column=2, padx=5, sticky="w")

       # Save Button
        tk.Button(root, text="Save Shortcut", command=self.save_shortcut).grid(row=3, column=1, sticky="e", padx=10, pady=5)

        #  Shortcut List 
        tk.Label(root, text="Registered Shortcuts:").grid(row=4, column=0, padx=10, sticky="w")
        self.shortcut_list = tk.Listbox(root, width=70, height=10)
        self.shortcut_list.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

        #  Delete Button 
        tk.Button(root, text="Delete Selected", command=self.delete_shortcut).grid(row=6, column=1, sticky="e", padx=10, pady=5)

        # Load existing shortcuts on startup
        self.refresh_list()

    def save_shortcut(self):
        keys = self.keyboard_input.get().strip()
        action_type = self.action_var.get()
        action = self.action_entry.get().strip()


        #added for hold timer
        hold_raw = self.hold_entry.get().strip()
        hold_seconds = None
        if hold_raw:
            try:
                hold_seconds = float(hold_raw)
                if hold_seconds <= 0:
                    raise ValueError
            except ValueError:
                messagebox.showerror("Error", "Hold duration must be a positive number")
                return




        # Validation
        if not keys:
            messagebox.showerror("Error", "Please enter a key combination")
            return
        if not action:
            messagebox.showerror("Error", "Please enter an action value")
            return
        
        #hold secs can be a number like 2.0 or None so if they fill it in it gets updated like 2, hold_seconds=2 also if its blank it can be None
        sm.add_shortcut(keys, action_type, action, hold_seconds=hold_seconds)
        self.refresh_list()

        # Clearing the input fields
        self.keyboard_input.delete(0, tk.END)
        self.action_entry.delete(0, tk.END)
        self.hold_entry.delete(0, tk.END)

    def delete_shortcut(self):
        selection = self.shortcut_list.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select a shortcut to delete")
            return
        
        # Get the ID from the selected line
        selected_text = self.shortcut_list.get(selection[0])
        shortcut_id = int(selected_text.split("|")[0].strip())

        sm.delete_shortcut(shortcut_id)
        self.refresh_list()

    def refresh_list(self):
        # Clear and reload the listbox from JSON
        self.shortcut_list.delete(0, tk.END)
        data = sm.load_shortcuts()
        for s in data["shortcuts"]:
            hold_info = f" | hold: {s['hold_seconds']}s" if s.get("hold_seconds") else ""
            display = f"{s['id']} | {s['keys']} | {s['type']} | {s['action']}{hold_info}"
            self.shortcut_list.insert(tk.END, display)