from tkinter import font

import customtkinter
from settings_ui import SettingsUI
import json
import widgets as cw
from theme.thememanager import ThemeManager


class PomodoroTimerApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x400")

        with open("src/settings.json", "r") as f:
            settings = json.load(f)
            self.work_duration = settings["work_duration"]
            self.break_duration = settings["break_duration"]

        self.theme = ThemeManager.theme

        self.configure(fg_color=self.theme["CTk"]["fg_color"])

        self.minutes = self.work_duration
        self.seconds = 0

        self.on_break = False
        self.paused = False

        self.settings_btn = cw.TButton(self, width=30, height=30, text="⚙️", command=self.settings_button_callback)

        self.btn_frame = cw.TFrame(self, width=100, height=50)
        self.play_btn = cw.TButton(self.btn_frame, width=30, height=30, text="▶️", command=self.play_button_callback)
        self.pause_btn = cw.TButton(self.btn_frame, width=30, height=30, text="⏸️", command=self.pause_button_callback)
        self.skip_btn = cw.TButton(self.btn_frame, width=30, height=30, text="⏭️", command=self.skip_button_callback)
        self.reset_btn = cw.TButton(self.btn_frame, width=30, height=30, text="🔄", command=self.reset_button_callback)

        x, y = 180, 80
        self.timer_frame = cw.PlaceholderFrame(self, width=x*2, height=y*2)
        self.timer_canvas = cw.TCanvas(self.timer_frame, width=x*2, height=y*2)
        self.timer_text_outline = [
            self.timer_canvas.create_text(x - 2, y, text=f"{self.minutes:02d}:{self.seconds:02d}", font=("Arial", 98), fill=self.theme["CTkLabel"]["border_color"]),
            self.timer_canvas.create_text(x + 2, y, text=f"{self.minutes:02d}:{self.seconds:02d}", font=("Arial", 98), fill=self.theme["CTkLabel"]["border_color"]),
            self.timer_canvas.create_text(x, y - 2, text=f"{self.minutes:02d}:{self.seconds:02d}", font=("Arial", 98), fill=self.theme["CTkLabel"]["border_color"]),
            self.timer_canvas.create_text(x, y + 2, text=f"{self.minutes:02d}:{self.seconds:02d}", font=("Arial", 98), fill=self.theme["CTkLabel"]["border_color"]),
        ]
        self.timer_text = self.timer_canvas.create_text(x, y, text=f"{self.minutes:02d}:{self.seconds:02d}", font=("Arial", 98), fill=self.theme["CTkLabel"]["secondary_text_color"])

        self.rs_spacer_frame = cw.PlaceholderFrame(self, width=30, height=30)

        # Build layout
        self.settings_btn.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.timer_frame.grid(row=1, column=1, columnspan=6, padx=10, pady=10)
        self.timer_canvas.pack()

        self.btn_frame.grid(row=2, column=2, columnspan=4, padx=10, pady=10)
        self.reset_btn.grid(row=0, column=0, padx=5, pady=5)
        self.play_btn.grid(row=0, column=1, padx=5, pady=5)
        self.pause_btn.grid(row=0, column=2, padx=5, pady=5)
        self.skip_btn.grid(row=0, column=3, padx=5, pady=5)

        self.rs_spacer_frame.grid(row=0, column=7, padx=10, pady=10)

        # Make columns expand equally
        for i in range(7):
            self.columnconfigure(i, weight=1)

    def settings_button_callback(self):
        self.settings_window = SettingsUI(self)
        self.settings_window.after(10, self.settings_window.lift)  # Focus on the settings window

    def play_button_callback(self):
        self.paused = False
        self.count_down()

    def pause_button_callback(self):
        self.paused = True

    def skip_button_callback(self):
        if self.on_break:
            self.on_break = False
            self.minutes = self.work_duration
        else:
            self.on_break = True
            self.minutes = self.break_duration
        self.seconds = 0
        self.update_timer_text()

    def reset_button_callback(self):
        self.paused = True
        if self.on_break:
            self.minutes = self.break_duration
        else:
            self.minutes = self.work_duration
        self.seconds = 0
        self.update_timer_text()

    def count_down(self):
        if self.paused:
            return
        
        if self.seconds == 0:
            if self.minutes == 0:
                # Timer finished
                if self.on_break:
                    self.on_break = False
                    self.minutes = self.work_duration
                else:
                    self.on_break = True
                    self.minutes = self.break_duration
                self.seconds = 0
            else:
                self.minutes -= 1
                self.seconds = 59
        else:
            self.seconds -= 1

        # Update the timer display
        self.update_timer_text()

        # Schedule the next countdown call after 1 second (1000 milliseconds)
        self.after(1000, self.count_down)

    def update_timer_text(self):
        for item in self.timer_text_outline:
            self.timer_canvas.itemconfig(item, text=f"{self.minutes:02d}:{self.seconds:02d}")

        self.timer_canvas.itemconfig(self.timer_text, text=f"{self.minutes:02d}:{self.seconds:02d}")