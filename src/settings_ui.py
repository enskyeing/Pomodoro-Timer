import customtkinter


class SettingsUI(customtkinter.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Settings")
        self.geometry("300x250")

        # WIDGETS
        self.work_duration_frame = customtkinter.CTkFrame(self)
        self.work_duration_label = customtkinter.CTkLabel(self.work_duration_frame, text="Work Duration (minutes):")
        self.work_duration_entry = customtkinter.CTkEntry(self.work_duration_frame)

        self.break_duration_frame = customtkinter.CTkFrame(self)
        self.break_duration_label = customtkinter.CTkLabel(self.break_duration_frame, text="Break Duration (minutes):")
        self.break_duration_entry = customtkinter.CTkEntry(self.break_duration_frame)

        self.theme_frame = customtkinter.CTkFrame(self)
        self.theme_label = customtkinter.CTkLabel(self.theme_frame, text="Theme:")
        self.theme_selector = customtkinter.CTkOptionMenu(self.theme_frame, values=["Light", "Dark"])

        self.save_button = customtkinter.CTkButton(self, text="Save", command=self.save_settings)

        # LAYOUT
        self.work_duration_frame.grid(row=0, column=0, padx=10, pady=5, sticky="ew")
        self.work_duration_label.grid(row=0, column=0, sticky="w")
        self.work_duration_entry.grid(row=1, column=0, sticky="ew")
        self.work_duration_frame.columnconfigure(0, weight=1)

        self.break_duration_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
        self.break_duration_label.grid(row=0, column=0, sticky="w")
        self.break_duration_entry.grid(row=1, column=0, sticky="ew")
        self.break_duration_frame.columnconfigure(0, weight=1)

        self.theme_frame.grid(row=2, column=0, padx=10, pady=5, sticky="ew")
        self.theme_label.grid(row=0, column=0, sticky="w")
        self.theme_selector.grid(row=1, column=0, sticky="ew")
        self.theme_frame.columnconfigure(0, weight=1)

        self.save_button.grid(row=3, column=0, pady=5)

        self.columnconfigure(0, weight=1)

    def save_settings(self):
        # Here you would save the settings to a file or update the main app's settings
        work_duration = self.work_duration_entry.get()
        break_duration = self.break_duration_entry.get()
        print(f"Saved settings: Work Duration = {work_duration}, Break Duration = {break_duration}")