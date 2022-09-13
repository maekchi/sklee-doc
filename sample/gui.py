import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext, messagebox
from .parser import Parser, ParserException
import pyperclip as clip


class GuiScreen:
    def run_with_text(self):
        text = self.text_area.get("1.0", tk.END)
        try:
            self.parser.parse(text)
            messagebox.showerror(title="Error", message=str(self.parser))
        except ParserException as ex:
            messagebox.showerror(title="Error", message=str(ex))

    def paste(self, event):
        self.text_area.insert(tk.END, clip.paste())

    def set_gui(self, version, width, height):
        window = tk.Tk()
        window.title = f"sample program - {version}"
        window.wm_geometry(f"{width}x{height}")

        ttk.Label(window, text="Copy and paste in here").grid(column=0, padx=10, pady=10)

        text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=52, height=20)

        # textbox = ttk.Entry(window, width=200, textvariable=str)
        text_area.grid(column=0, row=1, padx=5, pady=5)
        text_area.bind("<Control-v>", self.paste)
        text_area.bind("<Command-v>", self.paste)
        action = ttk.Button(window, text="Add", command=self.run_with_text)
        action.grid(column=0, row=2, padx=5, pady=5)
        self.window = window
        self.text_area = text_area

    def __init__(self, version, width, height):
        self.window = None
        self.text_area = None
        self.version = version
        self.parser: Parser | None = None
        self.set_gui(version, width, height)

    def set_parser(self, parser: Parser):
        self.parser = parser

    def open(self):
        self.window.mainloop()
