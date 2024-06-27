import tkinter as tk
from PIL import ImageGrab
from ocr import perform_ocr
from clipboard import copy_to_clipboard

class ScreenshotTool:
    def __init__(self, root, callback):
        self.root = root
        self.callback = callback
        self.screenshot_window = None
        self.canvas = None
        self.rect = None
        self.start_x = None
        self.start_y = None

    def start_snip(self):
        self.screenshot_window = tk.Toplevel(self.root)
        self.screenshot_window.attributes('-fullscreen', True)
        self.screenshot_window.attributes('-alpha', 0.3)
        self.screenshot_window.bind("<ButtonPress-1>", self.on_button_press)
        self.screenshot_window.bind("<B1-Motion>", self.on_mouse_drag)
        self.screenshot_window.bind("<ButtonRelease-1>", self.on_button_release)
        self.canvas = tk.Canvas(self.screenshot_window, cursor="cross")
        self.canvas.pack(fill="both", expand=True)

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        if self.rect:
            self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red', dash=(2, 2))

    def on_mouse_drag(self, event):
        curX, curY = (event.x, event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, curX, curY)

    def on_button_release(self, event):
        x1 = min(self.start_x, event.x)
        y1 = min(self.start_y, event.y)
        x2 = max(self.start_x, event.x)
        y2 = max(self.start_y, event.y)
        self.screenshot_window.withdraw()
        self.take_screenshot(x1, y1, x2, y2)
        self.screenshot_window.destroy()
        self.callback()

    def take_screenshot(self, x1, y1, x2, y2):
        im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        text = perform_ocr(im)
        copy_to_clipboard(text)
