import customtkinter
from settings_ui import SettingsUI


class PomodoroTimerApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x400")

        self.settings_btn = customtkinter.CTkButton(self, width=30, height=30, text="⚙️", command=self.settings_button_callback)

        self.btn_frame = customtkinter.CTkFrame(self, width=100, height=50)
        self.play_btn = customtkinter.CTkButton(self.btn_frame, width=30, height=30, text="▶️", command=self.play_button_callback)
        self.pause_btn = customtkinter.CTkButton(self.btn_frame, width=30, height=30, text="⏸️", command=self.pause_button_callback)
        self.stop_btn = customtkinter.CTkButton(self.btn_frame, width=30, height=30, text="⏹️", command=self.stop_button_callback)
        self.reset_btn = customtkinter.CTkButton(self.btn_frame, width=30, height=30, text="🔄", command=self.reset_button_callback)

        self.timer_frame = customtkinter.CTkFrame(self, width=100, height=50)
        self.timer_text = customtkinter.CTkLabel(self.timer_frame, text="25:00", font=("Arial", 24))

        self.rs_spacer_frame = customtkinter.CTkFrame(self, width=30, height=30)

        # Build layout
        self.settings_btn.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

        self.timer_frame.grid(row=1, column=1, columnspan=6, padx=10, pady=10)
        self.timer_text.grid(row=0, column=0)

        self.btn_frame.grid(row=2, column=2, columnspan=4, padx=10, pady=10)
        self.reset_btn.grid(row=0, column=0, padx=5, pady=5)
        self.play_btn.grid(row=0, column=1, padx=5, pady=5)
        self.pause_btn.grid(row=0, column=2, padx=5, pady=5)
        self.stop_btn.grid(row=0, column=3, padx=5, pady=5)

        self.rs_spacer_frame.grid(row=0, column=7, padx=10, pady=10)

        # Make columns expand equally
        for i in range(7):
            self.columnconfigure(i, weight=1)

    def settings_button_callback(self):
        SettingsUI(self)

    def play_button_callback(self):
        pass

    def pause_button_callback(self):
        pass

    def stop_button_callback(self):
        pass

    def reset_button_callback(self):
        pass

    