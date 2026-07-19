import customtkinter


class PomodoroTimerApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")

        self.settings_btn = customtkinter.CTkButton(self, width=20, height=20, command=self.settings_button_callback)
        self.play_pause_btn = customtkinter.CTkButton(self, width=60, height=20, command=self.play_pause_button_callback)
        self.reset_btn = customtkinter.CTkButton(self, width=60, height=20, command=self.reset_button_callback)
    
    def settings_button_callback(self):
        pass

    def play_pause_button_callback(self):
        pass

    def reset_button_callback(self):
        pass

    