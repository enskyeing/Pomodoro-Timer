import customtkinter
from settings_ui import SettingsUI
import json


class PomodoroTimerApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")

        with open("src/settings.json", "r") as f:
            settings = json.load(f)
            self.work_duration = settings["work_duration"]
            self.break_duration = settings["break_duration"]

        self.minutes = self.work_duration
        self.seconds = 0

        self.on_break = False
        self.paused = False

        self.settings_btn = customtkinter.CTkButton(self, width=30, height=30, text="⚙️", command=self.settings_button_callback)

        self.btn_frame = customtkinter.CTkFrame(self, width=100, height=50)
        self.play_btn = customtkinter.CTkButton(self.btn_frame, width=30, height=30, text="▶️", command=self.play_button_callback)
        self.pause_btn = customtkinter.CTkButton(self.btn_frame, width=30, height=30, text="⏸️", command=self.pause_button_callback)
        self.skip_btn = customtkinter.CTkButton(self.btn_frame, width=30, height=30, text="⏭️", command=self.skip_button_callback)
        self.reset_btn = customtkinter.CTkButton(self.btn_frame, width=30, height=30, text="🔄", command=self.reset_button_callback)

        self.timer_frame = customtkinter.CTkFrame(self, width=100, height=50)
        self.timer_text = customtkinter.CTkLabel(self.timer_frame, text=f"{self.minutes:02d}:{self.seconds:02d}", font=("Arial", 24))

        self.rs_spacer_frame = customtkinter.CTkFrame(self, width=30, height=30)

        # Build layout
        self.settings_btn.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.timer_frame.grid(row=1, column=1, columnspan=6, padx=10, pady=10)
        self.timer_text.grid(row=0, column=0)

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
        SettingsUI(self)

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
        self.timer_text.configure(text=f"{self.minutes:02d}:{self.seconds:02d}")

    def reset_button_callback(self):
        pass

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
        self.timer_text.configure(text=f"{self.minutes:02d}:{self.seconds:02d}")

        # Schedule the next countdown call after 1 second (1000 milliseconds)
        self.after(1000, self.count_down)