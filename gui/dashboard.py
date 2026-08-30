import tkinter as tk
from tkinter import ttk
import json

from logic.inputData import add_mahasiswa

def gui_dashboard():
    window = tk.Tk()
    window.title("Dashboard")
    center_window(window, 1000, 600)
    window.resizable(False, False)

    sidebar = tk.Frame(
        window,
        width=220,
        bg="#2196F3"
    )
    sidebar.pack(side="left", fill="y")
    sidebar.pack_propagate(False)

    content = tk.Frame(
        window,
        bg="white"
    )
    content.pack(side="right", fill="both", expand=True)

    title = tk.Label(
        sidebar,
        text="DASHBOARD",
        font=("Arial", 20, "bold"),
        bg="#2196F3",
        fg="white"
    )
    title.pack(pady=30)

    def clear_content():
        for widget in content.winfo_children():
            widget.destroy()

    def show_data():
        clear_content()

        title = tk.Label(
            content,
            text="DATA MAHASISWA",
            font=("Arial", 22, "bold"),
            fg="black",
            bg="white"
        )
        title.pack(pady=(25, 15))

        filter_frame = tk.Frame(
            content,
            bg="white"
        )
        filter_frame.pack(pady=10)

        tk.Label(
            filter_frame,
            text="Urutan:",
            bg="white",
            fg="black"
        ).grid(row=0, column=0, padx=5)

        order_combo = ttk.Combobox(
            filter_frame,
            values=[
                "Ascending (A-Z)",
                "Descending (Z-A)"
            ],
            state="readonly",
            width=20
        )
        order_combo.current(0)
        order_combo.grid(row=0, column=1, padx=5)

        tk.Label(
            filter_frame,
            text="Berdasarkan:",
            bg="white",
            fg="black"
        ).grid(row=0, column=2, padx=5)

        sort_combo = ttk.Combobox(
            filter_frame,
            values=[
                "Nama",
                "Kelas",
                "Jurusan",
                "IPK"
            ],
            state="readonly",
            width=15
        )
        sort_combo.current(0)
        sort_combo.grid(row=0, column=3, padx=5)

        sort_button = tk.Button(
            filter_frame,
            text="Sort",
            width=10,
            bg="#2196F3",
            fg="white",
            activebackground="#2196F3",
            activeforeground="white"
        )
        sort_button.grid(row=0, column=4, padx=10)

        search_entry = tk.Entry(
            filter_frame,
            width=20,
            font=("Arial", 10)
        )
        search_entry.grid(
            row=1,
            column=0,
            columnspan=3,
            pady=15
        )

        search_button = tk.Button(
            filter_frame,
            text="Search",
            width=10,
            bg="#2196F3",
            fg="white",
            activebackground="#2196F3",
            activeforeground="white"
        )
        search_button.grid(
            row=1,
            column=3,
            padx=10
        )

        table_frame = tk.Frame(content)
        table_frame.pack(
            padx=20,
            pady=10
        )

        columns = (
            "nama",
            "kelas",
            "jurusan",
            "ipk"
        )

        table = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            height=13
        )

        table.heading(
            "nama",
            text="Nama"
        )

        table.heading(
            "kelas",
            text="Kelas"
        )

        table.heading(
            "jurusan",
            text="Jurusan"
        )

        table.heading(
            "ipk",
            text="IPK"
        )

        table.column(
            "nama",
            width=180
        )

        table.column(
            "kelas",
            width=80
        )

        table.column(
            "jurusan",
            width=250
        )

        table.column(
            "ipk",
            width=80
        )

        table.pack()

        with open("data/mahasiswa.json", "r") as file:
            data = json.load(file)

        for mahasiswa in data["mahasiswa"]:
            table.insert(
                "",
                "end",
                values=(
                    mahasiswa["nama"],
                    mahasiswa["kelas"],
                    mahasiswa["jurusan"],
                    mahasiswa["ipk"]
                )
            )

    def input_data():
        clear_content()

        title = tk.Label(
            content,
            text="INPUT DATA MAHASISWA",
            font=("Arial", 22, "bold"),
            fg="black",
            bg="white"
        )
        title.pack(pady=25)

        form_frame = tk.Frame(
            content,
            bg="white"
        )
        form_frame.pack()

        nama_label = tk.Label(
            form_frame,
            text="Nama",
            font=("Arial", 11),
            fg="black",
            bg="white"
        )
        nama_label.grid(
            row=0,
            column=0,
            sticky="w",
            pady=10
        )

        nama_entry = tk.Entry(
            form_frame,
            width=30,
            font=("Arial", 12)
        )
        nama_entry.grid(
            row=0,
            column=1,
            padx=20,
            pady=10
        )

        kelas_label = tk.Label(
            form_frame,
            text="Kelas",
            font=("Arial", 11),
            fg="black",
            bg="white"
        )
        kelas_label.grid(
            row=1,
            column=0,
            sticky="w",
            pady=10
        )

        kelas_combo = ttk.Combobox(
            form_frame,
            width=28,
            values=[
                "A",
                "B",
                "C"
            ],
            state="readonly",
            font=("Arial", 12)
        )
        kelas_combo.grid(
            row=1,
            column=1,
            padx=20,
            pady=10
        )

        jurusan_label = tk.Label(
            form_frame,
            text="Jurusan",
            font=("Arial", 11),
            fg="black",
            bg="white"
        )
        jurusan_label.grid(
            row=2,
            column=0,
            sticky="w",
            pady=10
        )

        jurusan_combo = ttk.Combobox(
            form_frame,
            width=28,
            values=[
                "Sistem Informasi",
                "Teknik Informatika",
                "Bisnis Digital"
            ],
            state="readonly",
            font=("Arial", 12)
        )
        jurusan_combo.grid(
            row=2,
            column=1,
            padx=20,
            pady=10
        )

        ipk_label = tk.Label(
            form_frame,
            text="IPK",
            font=("Arial", 11),
            fg="black",
            bg="white"
        )
        ipk_label.grid(
            row=3,
            column=0,
            sticky="w",
            pady=10
        )

        ipk_entry = tk.Entry(
            form_frame,
            width=30,
            font=("Arial", 12)
        )
        ipk_entry.grid(
            row=3,
            column=1,
            padx=20,
            pady=10
        )

        message_label = tk.Label(
            content,
            text="",
            font=("Arial", 10),
            fg="black",
            bg="white"
        )
        message_label.pack(pady=5)

        def save_data():
            nama = nama_entry.get()
            kelas = kelas_combo.get()
            jurusan = jurusan_combo.get()
            ipk = ipk_entry.get()

            berhasil, message = add_mahasiswa(
                nama,
                kelas,
                jurusan,
                ipk
            )

            message_label.config(
                text=message
            )

            if berhasil:
                nama_entry.delete(0, tk.END)
                kelas_combo.set("")
                jurusan_combo.set("")
                ipk_entry.delete(0, tk.END)

        save_button = tk.Button(
            content,
            text="Simpan",
            width=25,
            height=2,
            bg="#2196F3",
            fg="white",
            activebackground="#2196F3",
            activeforeground="white",
            font=("Arial", 10, "bold"),
            command=save_data
        )
        save_button.pack(pady=20)

    def menu_button(text, command):
        button = tk.Button(
            sidebar,
            text=text,
            width=20,
            height=2,
            bg="#2196F3",
            fg="white",
            activebackground="#2196F3",
            activeforeground="white",
            relief="flat",
            font=("Arial", 11, "bold"),
            command=command
        )
        button.pack(pady=5)

    menu_button(
        "Input Data",
        input_data
    )

    menu_button(
        "Show Data",
        show_data
    )

    exit_button = tk.Button(
        sidebar,
        text="Exit",
        width=20,
        height=2,
        bg="#2196F3",
        fg="white",
        activebackground="#2196F3",
        activeforeground="white",
        relief="flat",
        font=("Arial", 11, "bold"),
        command=window.destroy
    )
    exit_button.pack(pady=20)

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