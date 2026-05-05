import tkinter as tk
from gui import ShortcutApplication
from listener import start_listener

if __name__ == "__main__":
    start_listener()  # background thread, doesn't block tkinter
    root = tk.Tk()
    app = ShortcutApplication(root)
    root.mainloop()