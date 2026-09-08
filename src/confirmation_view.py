import customtkinter
import widgets as cw
from theme.thememanager import ThemeManager


class ConfirmationView(customtkinter.CTkToplevel):
    def __init__(self, parent, question: str):
        self.main_app = parent
        super().__init__(self.main_app)

        self.theme = ThemeManager.theme

        self.configure(fg_color=self.theme["CTk"]["fg_color"])

        self.confirmation_text = cw.TLabel(self, text=question, wraplength=300, font=(None, 12, "bold"))

        self.confirm_btn = cw.TButton(self, text="Confirm", command=self.confirm_btn_callback)
        self.deny_btn = cw.TButton(self, text="Deny", command=self.deny_btn_callback)

        self.confirmation_text.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
        self.deny_btn.grid(row=1, column=1, padx=10, pady=(0, 10))
        self.confirm_btn.grid(row=1, column=3, padx=10, pady=(0, 10))

        self.confirmed_state = False

        self.grab_set()  # Make the confirmation window modal
    
    def deny_btn_callback(self):
        self.destroy()
        self.confirmed_state = False

    def confirm_btn_callback(self):
        self.destroy()
        self.confirmed_state = True
