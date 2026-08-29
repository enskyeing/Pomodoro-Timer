import customtkinter
import widgets as cw
from theme.thememanager import ThemeManager


class ConfirmationView(customtkinter.CTkToplevel):
    def __init__(self, parent, question: str):
        self.main_app = parent
        super().__init__(self.main_app)

        self.theme = ThemeManager.theme

        self.configure(fg_color=self.theme["CTk"]["fg_color"])

        self.confirmation_text = cw.TLabel(self, text=question)

        self.confirm_btn = cw.TButton(self, text="Confirm")
        self.deny_btn = cw.TButton(self, text="Deny")

        self.confirmation_text.grid(row=0, col=0, columnspan=5)
        self.deny_btn.grid(row=1, column=1)
        self.confirm_btn.grid(row=1, column=3)
    
    def deny_btn_callback(self):
        pass 

    def confirm_btn_callback(self):
        pass
