import customtkinter
from theme.thememanager import ThemeManager


class TButton(customtkinter.CTkButton):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            fg_color=ThemeManager.theme["CTkButton"]["fg_color"],
            hover_color=ThemeManager.theme["CTkButton"]["hover_color"],
            text_color=ThemeManager.theme["CTkButton"]["text_color"],
            corner_radius=ThemeManager.theme["CTkButton"]["corner_radius"],
            border_width=ThemeManager.theme["CTkButton"]["border_width"],
            border_color=ThemeManager.theme["CTkButton"]["border_color"]
        )


class TFrame(customtkinter.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            fg_color=ThemeManager.theme["CTkFrame"]["primary_fg_color"],
            corner_radius=ThemeManager.theme["CTkFrame"]["corner_radius"],
            border_width=ThemeManager.theme["CTkFrame"]["border_width"],
            border_color=ThemeManager.theme["CTkFrame"]["border_color"]
        )


class TLabel(customtkinter.CTkLabel):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            text_color=ThemeManager.theme["CTkLabel"]["primary_text_color"],
            corner_radius=ThemeManager.theme["CTkLabel"]["corner_radius"],
            border_width=ThemeManager.theme["CTkLabel"]["border_width"],
            border_color=ThemeManager.theme["CTkLabel"]["border_color"],
            fg_color=ThemeManager.theme["CTkLabel"]["fg_color"]
        )


class TEntry(customtkinter.CTkEntry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            fg_color=ThemeManager.theme["CTkEntry"]["fg_color"],
            text_color=ThemeManager.theme["CTkEntry"]["text_color"],
            corner_radius=ThemeManager.theme["CTkEntry"]["corner_radius"],
            border_width=ThemeManager.theme["CTkEntry"]["border_width"],
            border_color=ThemeManager.theme["CTkEntry"]["border_color"]
        )


class TCanvas(customtkinter.CTkCanvas):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            bg=ThemeManager.theme["CTkCanvas"]["bg"],
            highlightthickness=ThemeManager.theme["CTkCanvas"]["highlightthickness"],
            borderwidth=ThemeManager.theme["CTkCanvas"]["borderwidth"]
        )


class TOptionMenu(customtkinter.CTkOptionMenu):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            fg_color=ThemeManager.theme["CTkOptionMenu"]["fg_color"],
            text_color=ThemeManager.theme["CTkOptionMenu"]["text_color"],
            button_color=ThemeManager.theme["CTkOptionMenu"]["button_color"],
            button_hover_color=ThemeManager.theme["CTkOptionMenu"]["button_hover_color"],
            corner_radius=ThemeManager.theme["CTkOptionMenu"]["corner_radius"]
        )


class TCheckBox(customtkinter.CTkCheckBox):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            fg_color=ThemeManager.theme["CTkCheckBox"]["fg_color"],
            text_color=ThemeManager.theme["CTkCheckBox"]["text_color"],
            corner_radius=ThemeManager.theme["CTkCheckBox"]["corner_radius"],
            border_width=ThemeManager.theme["CTkCheckBox"]["border_width"],
            border_color=ThemeManager.theme["CTkCheckBox"]["border_color"],
            hover_color=ThemeManager.theme["CTkCheckBox"]["hover_color"],
            checkmark_color=ThemeManager.theme["CTkCheckBox"]["checkmark_color"],
            text_color_disabled=ThemeManager.theme["CTkCheckBox"]["text_color_disabled"]
        )


class PlaceholderFrame(customtkinter.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            fg_color=ThemeManager.theme["PlaceholderFrame"]["fg_color"]
        )
