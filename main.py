import tkinter as tk
from tkinter import ttk
from screenshot import ScreenshotTool

class SnippingTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Snap OCR")
        self.root.geometry("400x150")
        self.root.configure(bg="#f0f0f0")
        self.create_widgets()
        self.snip_active = False

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TButton", font=("Segoe UI", 14), padding=10)

        header_frame = ttk.Frame(self.root)
        header_frame.pack(pady=10)

        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)

        # Create custom styles for the buttons
        style.configure("New.TButton", font=("Segoe UI", 16))
        style.configure("Cancel.TButton", font=("Segoe UI", 14))

        self.new_button = ttk.Button(button_frame, text=" ✂ New", style="New.TButton", command=self.start_snip)
        self.new_button.pack(side="left", padx=20)

        self.cancel_button = ttk.Button(button_frame, text=" ❌ Cancel", style="Cancel.TButton", command=self.root.quit)
        self.cancel_button.pack(side="right", padx=20)

    def start_snip(self):
        self.root.withdraw()
        self.snip_active = True
        self.screenshot_tool = ScreenshotTool(self.root, self.on_screenshot_complete)
        self.screenshot_tool.start_snip()

    def on_screenshot_complete(self):
        self.snip_active = False
        self.root.deiconify()

if __name__ == "__main__":
    root = tk.Tk()
    app = SnippingTool(root)
    root.mainloop()
