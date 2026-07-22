import customtkinter


class SettingsUI(customtkinter.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Settings")
        self.geometry("300x200")

        # Create a label and entry for the work duration
        self.work_duration_label = customtkinter.CTkLabel(self, text="Work Duration (minutes):")
        self.work_duration_entry = customtkinter.CTkEntry(self)

        # Create a label and entry for the break duration
        self.break_duration_label = customtkinter.CTkLabel(self, text="Break Duration (minutes):")
        self.break_duration_entry = customtkinter.CTkEntry(self)

        # Create a save button
        self.save_button = customtkinter.CTkButton(self, text="Save", command=self.save_settings)

        # Layout the widgets
        self.work_duration_label.grid(row=0, column=0, padx=10, pady=10)
        self.work_duration_entry.grid(row=0, column=1, padx=10, pady=10)
        self.break_duration_label.grid(row=1, column=0, padx=10, pady=10)
        self.break_duration_entry.grid(row=1, column=1, padx=10, pady=10)
        self.save_button.grid(row=2, columnspan=2, pady=20)

    def save_settings(self):
        # Here you would save the settings to a file or update the main app's settings
        work_duration = self.work_duration_entry.get()
        break_duration = self.break_duration_entry.get()
        print(f"Saved settings: Work Duration = {work_duration}, Break Duration = {break_duration}")