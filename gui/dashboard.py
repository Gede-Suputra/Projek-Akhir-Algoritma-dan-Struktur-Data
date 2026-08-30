import tkinter as tk

from gui.input import gui_input_data
from gui.show import gui_show_data
from gui.theme import (
    SIDEBAR_BG,
    SIDEBAR_HOVER,
    SIDEBAR_ACTIVE,
    BG_LIGHT,
    TEXT_WHITE,
    TEXT_MUTED,
    DANGER,
    DANGER_DARK,
    font,
    add_hover,
    setup_ttk_style
)


def gui_dashboard():
    window = tk.Tk()
    window.title("Dashboard - Data Mahasiswa")
    center_window(window, 1050, 640)
    window.resizable(False, False)
    window.configure(bg=BG_LIGHT)

    setup_ttk_style()

    sidebar = tk.Frame(
        window,
        width=230,
        bg=SIDEBAR_BG
    )
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)

    content = tk.Frame(
        window,
        bg=BG_LIGHT
    )
    content.pack(side="right", fill="both", expand=True)

    # ==================== SIDEBAR HEADER ====================

    header_frame = tk.Frame(sidebar, bg=SIDEBAR_BG)
    header_frame.pack(pady=(35, 15), fill="x")

    logo = tk.Label(
        header_frame,
        text="🎓",
        font=("Segoe UI Emoji", 30),
        bg=SIDEBAR_BG,
        fg=TEXT_WHITE
    )
    logo.pack()

    title = tk.Label(
        header_frame,
        text="DASHBOARD",
        font=font(17, "bold"),
        bg=SIDEBAR_BG,
        fg=TEXT_WHITE
    )
    title.pack(pady=(6, 0))

    subtitle = tk.Label(
        header_frame,
        text="Data Mahasiswa",
        font=font(9),
        bg=SIDEBAR_BG,
        fg=TEXT_MUTED
    )
    subtitle.pack()

    separator = tk.Frame(sidebar, bg=SIDEBAR_HOVER, height=1)
    separator.pack(fill="x", padx=20, pady=15)

    # ==================== CONTENT SWITCHING ====================

    def clear_content():
        for widget in content.winfo_children():
            widget.destroy()

    menu_buttons = {}

    def set_active(name):
        for key, btn in menu_buttons.items():
            btn.config(bg=SIDEBAR_ACTIVE if key == name else SIDEBAR_BG)

    def show_input():
        clear_content()
        set_active("input")
        gui_input_data(content)

    def show_data():
        clear_content()
        set_active("data")
        gui_show_data(content, center_window)

    def menu_button(key, icon, text, command):
        btn = tk.Button(
            sidebar,
            text=f"   {icon}   {text}",
            anchor="w",
            width=22,
            height=2,
            bg=SIDEBAR_BG,
            fg=TEXT_WHITE,
            activebackground=SIDEBAR_ACTIVE,
            activeforeground=TEXT_WHITE,
            relief="flat",
            bd=0,
            cursor="hand2",
            font=font(11, "bold"),
            command=command
        )
        btn.pack(pady=3, padx=15)

        def on_enter(_event):
            if btn.cget("bg") != SIDEBAR_ACTIVE:
                btn.config(bg=SIDEBAR_HOVER)

        def on_leave(_event):
            if btn.cget("bg") != SIDEBAR_ACTIVE:
                btn.config(bg=SIDEBAR_BG)

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

        menu_buttons[key] = btn
        return btn

    menu_button("input", "📝", "Input Data", show_input)
    menu_button("data", "📋", "Show Data", show_data)

    # ==================== EXIT BUTTON (RED) ====================

    bottom_frame = tk.Frame(sidebar, bg=SIDEBAR_BG)
    bottom_frame.pack(side="bottom", pady=25, fill="x", padx=15)

    exit_button = tk.Button(
        bottom_frame,
        text="   🚪   Exit",
        anchor="w",
        width=22,
        height=2,
        bg=DANGER,
        fg=TEXT_WHITE,
        activebackground=DANGER_DARK,
        activeforeground=TEXT_WHITE,
        relief="flat",
        bd=0,
        cursor="hand2",
        font=font(11, "bold"),
        command=window.destroy
    )
    exit_button.pack(fill="x")
    add_hover(exit_button, DANGER, DANGER_DARK)

    show_data()

    window.mainloop()


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(
        f"{width}x{height}+{x}+{y}"
    )


if __name__ == "__main__":
    gui_dashboard()