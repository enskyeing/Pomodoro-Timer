import customtkinter
import widgets as cw
from theme.thememanager import ThemeManager


class SettingsUI(customtkinter.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Settings")
        self.geometry("300x300")

        self.theme = ThemeManager.theme

        self.configure(fg_color=self.theme["CTk"]["fg_color"])

        # WIDGETS
        self.work_duration_frame = cw.TFrame(self)
        self.work_duration_frame.configure(fg_color=self.theme["CTkFrame"]["settings"])
        self.work_duration_holding_frame = cw.PlaceholderFrame(self.work_duration_frame)
        self.work_duration_label = cw.TLabel(self.work_duration_holding_frame, text="Work Duration (minutes):")
        self.work_duration_label.configure(text_color=self.theme["CTkLabel"]["settings"])
        self.work_duration_entry = cw.TEntry(self.work_duration_holding_frame)

        self.break_duration_frame = cw.TFrame(self)
        self.break_duration_frame.configure(fg_color=self.theme["CTkFrame"]["settings"])
        self.break_duration_holding_frame = cw.PlaceholderFrame(self.break_duration_frame)
        self.break_duration_label = cw.TLabel(self.break_duration_holding_frame, text="Break Duration (minutes):")
        self.break_duration_label.configure(text_color=self.theme["CTkLabel"]["settings"])
        self.break_duration_entry = cw.TEntry(self.break_duration_holding_frame)

        self.theme_frame = cw.TFrame(self)
        self.theme_frame.configure(fg_color=self.theme["CTkFrame"]["settings"])
        self.theme_holding_frame = cw.PlaceholderFrame(self.theme_frame)
        self.theme_label = cw.TLabel(self.theme_holding_frame, text="Theme:")
        self.theme_label.configure(text_color=self.theme["CTkLabel"]["settings"])
        self.theme_selector = cw.TOptionMenu(self.theme_holding_frame, values=["Light", "Dark"])

        self.save_button = cw.TButton(self, text="Save", command=self.save_settings)

        # LAYOUT
        self.work_duration_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        self.work_duration_holding_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")
        self.work_duration_label.grid(row=0, column=0, sticky="w")
        self.work_duration_entry.grid(row=1, column=0, sticky="ew")
        self.work_duration_frame.columnconfigure(0, weight=1)
        self.work_duration_holding_frame.columnconfigure(0, weight=1)
        self.work_duration_holding_frame.rowconfigure(0, weight=1)

        self.break_duration_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.break_duration_holding_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")
        self.break_duration_label.grid(row=0, column=0, sticky="w")
        self.break_duration_entry.grid(row=1, column=0, sticky="ew")
        self.break_duration_frame.columnconfigure(0, weight=1)
        self.break_duration_holding_frame.columnconfigure(0, weight=1)
        self.break_duration_holding_frame.rowconfigure(0, weight=1)

        self.theme_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        self.theme_holding_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nesw")
        self.theme_label.grid(row=0, column=0, sticky="w")
        self.theme_selector.grid(row=1, column=0, sticky="ew")
        self.theme_frame.columnconfigure(0, weight=1)
        self.theme_holding_frame.columnconfigure(0, weight=1)
        self.theme_holding_frame.rowconfigure(0, weight=1)

        self.save_button.grid(row=3, column=0, pady=5)

        self.columnconfigure(0, weight=1)

    def save_settings(self):
        # Here you would save the settings to a file or update the main app's settings
        work_duration = self.work_duration_entry.get()
        break_duration = self.break_duration_entry.get()
        print(f"Saved settings: Work Duration = {work_duration}, Break Duration = {break_duration}")