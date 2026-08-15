import customtkinter
import widgets as cw
import pyglet
from theme.thememanager import ThemeManager

from settings_view import SettingsView
import settings

pyglet.options['win32_gdi_font'] = True  # Fixes font rendering issues on Windows
font_directory = "src/assets/fonts"
pyglet.font.add_directory(font_directory)


class PomodoroTimerApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x400")

        self.settings = settings.controller

        self.theme = ThemeManager.theme

        self.configure(fg_color=self.theme["CTk"]["fg_color"])

        self.work_duration = self.settings.settings["work_duration"]
        self.break_duration = self.settings.settings["break_duration"]

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

        self.rs_spacer_frame = cw.PlaceholderFrame(self, width=30, height=30)

        x, y = 180, 80
        self.timer_frame = cw.TFrame(self, width=x*2, height=y*2)
        self.timer_frame.configure(fg_color=self.theme["CTkFrame"]["border_color"])
        self.timer_canvas = cw.TCanvas(self.timer_frame, width=x*2, height=y*2)

        # Add extra padding to Canvas corners
        rounded_corner_coords = [
            (0, 0, 0.4, 1), # top left
            (0, 0, 1, 0.4),
            (0, 0, 0.2, 2),
            (0, 0, 2, 0.2),
            (0, y*2, 0.4, y*2 - 1), # bottom left
            (0, y*2, 1, y*2 - 0.4),
            (0, y*2, 0.2, y*2 - 2),
            (0, y*2, 2, y*2 - 0.2),
            (x*2, 0, x*2 - 0.4, 1), # top right
            (x*2, 0, x*2 - 1, 0.4),
            (x*2, 0, x*2 - 0.2, 2),
            (x*2, 0, x*2 - 2, 0.2),
            (x*2, y*2, x*2 - 0.4, y*2 - 1), # bottom right
            (x*2, y*2, x*2 - 1, y*2 - 0.4),
            (x*2, y*2, x*2 - 0.2, y*2 - 2),
            (x*2, y*2, x*2 - 2, y*2 - 0.2),
        ]
        self.timer_canvas_rounded_corners = []
        for coords in rounded_corner_coords:
            self.timer_canvas_rounded_corners.append(
                self.timer_canvas.create_rectangle(*coords, fill=self.theme["CTkFrame"]["border_color"])
            )
        
        # Add text with outline effect
        timer_text_ouline_coords = [
            (x - 2, y),
            (x + 2, y),
            (x, y - 2),
            (x, y + 2),
            (x - 1, y - 1),
            (x + 1, y - 1),
            (x - 1, y + 1),
            (x + 1, y + 1)
        ]
        self.timer_text_outline = []
        for coords in timer_text_ouline_coords:
            self.timer_text_outline.append(
                self.timer_canvas.create_text(*coords, text=f"{self.minutes:02d}:{self.seconds:02d}", font=("Arial", 98), fill=self.theme["CTkLabel"]["border_color"])
            )
        self.timer_text = self.timer_canvas.create_text(x, y, text=f"{self.minutes:02d}:{self.seconds:02d}", font=("Arial", 98), fill=self.theme["CTkLabel"]["secondary_text_color"])

        # Build layout
        self.settings_btn.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.timer_frame.grid(row=1, column=1, columnspan=6, padx=10, pady=10)
        self.timer_canvas.pack(padx=self.theme["CTkFrame"]["border_width"], pady=self.theme["CTkFrame"]["border_width"])

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
        self.settings_window = SettingsView(self)
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
        updated_text = f"{self.minutes:02d}:{self.seconds:02d}"
        for item in self.timer_text_outline:
            self.timer_canvas.itemconfig(item, text=updated_text)

        self.timer_canvas.itemconfig(self.timer_text, text=updated_text)