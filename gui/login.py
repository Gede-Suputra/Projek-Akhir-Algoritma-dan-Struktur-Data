import tkinter as tk
from logic.authentication import login
from gui.dashboard import gui_dashboard


def gui_login():
    window = tk.Tk()
    window.title("Login")
    center_window(window, 400, 300)
    window.resizable(False, False)

    title = tk.Label(
        window,
        text="LOGIN",
        font=("Arial", 24, "bold")
    )
    title.pack(pady=20)

    username_label = tk.Label(
        window,
        text="Username"
    )
    username_label.pack()

    username_entry = tk.Entry(
        window,
        width=25,
        font=("Arial", 14)
    )
    username_entry.pack(pady=5)

    password_label = tk.Label(
        window,
        text="Password"
    )
    password_label.pack(pady=(10, 0))

    password_entry = tk.Entry(
        window,
        width=25,
        font=("Arial", 14),
        show="*"
    )
    password_entry.pack(pady=5)

    message_label = tk.Label(
        window,
        text="",
        font=("Arial", 10),
        fg="red"
    )
    message_label.pack()

    def get_login():
        username = username_entry.get()
        password = password_entry.get()

        hasil = login(username, password)

        message_label.config(text=hasil[1])

        if hasil[0]:
            window.destroy()
            gui_dashboard()

    login_button = tk.Button(
        window,
        text="Login",
        width=25,
        bg="#2196F3",
        fg="white",
        activebackground="#2196F3",
        activeforeground="white",
        command=get_login
    )
    login_button.pack(pady=20)

    window.mainloop()


def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    window.geometry(f"{width}x{height}+{x}+{y}")


if __name__ == "__main__":
    gui_login()