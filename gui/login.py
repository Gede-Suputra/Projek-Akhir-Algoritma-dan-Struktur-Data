import tkinter as tk

from logic.authentication import login
from gui.dashboard import gui_dashboard
from gui.theme import (
    PRIMARY,
    PRIMARY_DARK,
    CARD_BG,
    TEXT_DARK,
    TEXT_MUTED,
    TEXT_WHITE,
    DANGER,
    BORDER,
    font,
    add_hover,
    styled_entry
)


def gui_login():
    window = tk.Tk()
    window.title("Login - Data Mahasiswa")
    center_window(window, 420, 480)
    window.resizable(False, False)
    window.configure(bg=PRIMARY)

    card = tk.Frame(
        window,
        bg=CARD_BG,
        highlightbackground=BORDER,
        highlightthickness=0
    )
    card.place(relx=0.5, rely=0.5, anchor="center", width=340, height=400)

    logo = tk.Label(
        card,
        text="🎓",
        font=("Segoe UI Emoji", 36),
        bg=CARD_BG
    )
    logo.pack(pady=(35, 5))

    title = tk.Label(
        card,
        text="Selamat Datang",
        font=font(18, "bold"),
        bg=CARD_BG,
        fg=TEXT_DARK
    )
    title.pack()

    subtitle = tk.Label(
        card,
        text="Masuk untuk melanjutkan",
        font=font(10),
        bg=CARD_BG,
        fg=TEXT_MUTED
    )
    subtitle.pack(pady=(0, 25))

    username_label = tk.Label(
        card,
        text="Username",
        font=font(9, "bold"),
        bg=CARD_BG,
        fg=TEXT_MUTED,
        anchor="w"
    )
    username_label.pack(fill="x", padx=40)

    username_entry = styled_entry(card, width=28, size=11)
    username_entry.pack(pady=(5, 15), padx=40, ipady=5)

    password_label = tk.Label(
        card,
        text="Password",
        font=font(9, "bold"),
        bg=CARD_BG,
        fg=TEXT_MUTED,
        anchor="w"
    )
    password_label.pack(fill="x", padx=40)

    password_entry = styled_entry(card, width=28, size=11)
    password_entry.config(show="•")
    password_entry.pack(pady=(5, 10), padx=40, ipady=5)

    message_label = tk.Label(
        card,
        text="",
        font=font(9),
        bg=CARD_BG,
        fg=DANGER,
        wraplength=280
    )
    message_label.pack(pady=(0, 5))

    def get_login(event=None):
        username = username_entry.get()
        password = password_entry.get()

        hasil = login(username, password)

        message_label.config(text=hasil[1])

        if hasil[0]:
            window.destroy()
            gui_dashboard()

    login_button = tk.Button(
        card,
        text="Login",
        width=25,
        bg=PRIMARY,
        fg=TEXT_WHITE,
        activebackground=PRIMARY_DARK,
        activeforeground=TEXT_WHITE,
        relief="flat",
        bd=0,
        cursor="hand2",
        font=font(11, "bold"),
        command=get_login
    )
    login_button.pack(pady=15, ipady=6)
    add_hover(login_button, PRIMARY, PRIMARY_DARK)

    window.bind("<Return>", get_login)
    username_entry.focus()

    window.mainloop()


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")


if __name__ == "__main__":
    gui_login()