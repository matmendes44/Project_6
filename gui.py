import tkinter as tk

class ShortcutApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Shortcut Manager")
        self.root.geometry("600x500")

        # --- Action Input Section for Users ---
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