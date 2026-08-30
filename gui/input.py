import tkinter as tk
from tkinter import ttk

from logic.inputData import add_mahasiswa
from gui.theme import (
    BG_LIGHT,
    CARD_BG,
    TEXT_DARK,
    TEXT_MUTED,
    PRIMARY,
    PRIMARY_DARK,
    SUCCESS,
    DANGER,
    BORDER,
    font,
    styled_entry,
    styled_button
)


def gui_input_data(content):
    title = tk.Label(
        content,
        text="Input Data Mahasiswa",
        font=font(20, "bold"),
        fg=TEXT_DARK,
        bg=BG_LIGHT
    )
    title.pack(pady=(30, 5), padx=30, anchor="w")

    subtitle = tk.Label(
        content,
        text="Lengkapi form di bawah untuk menambahkan data mahasiswa baru",
        font=font(10),
        fg=TEXT_MUTED,
        bg=BG_LIGHT
    )
    subtitle.pack(padx=30, anchor="w", pady=(0, 20))

    card = tk.Frame(
        content,
        bg=CARD_BG,
        highlightbackground=BORDER,
        highlightthickness=1
    )
    card.pack(padx=30, fill="x")

    form_frame = tk.Frame(card, bg=CARD_BG)
    form_frame.pack(padx=35, pady=30, fill="x")
    form_frame.columnconfigure(1, weight=1)

    def field_label(text, row):
        lbl = tk.Label(
            form_frame,
            text=text,
            font=font(10, "bold"),
            fg=TEXT_DARK,
            bg=CARD_BG
        )
        lbl.grid(row=row, column=0, sticky="w", pady=12, padx=(0, 20))

    field_label("NIM", 0)
    nim_entry = styled_entry(form_frame, width=32, size=11)
    nim_entry.grid(row=0, column=1, sticky="ew", pady=12, ipady=5)

    field_label("Nama", 1)
    nama_entry = styled_entry(form_frame, width=32, size=11)
    nama_entry.grid(row=1, column=1, sticky="ew", pady=12, ipady=5)

    field_label("Kelas", 2)
    kelas_combo = ttk.Combobox(
        form_frame,
        width=30,
        values=["A", "B", "C"],
        state="readonly",
        font=font(11)
    )
    kelas_combo.grid(row=2, column=1, sticky="ew", pady=12)

    field_label("Jurusan", 3)
    jurusan_combo = ttk.Combobox(
        form_frame,
        width=30,
        values=["Sistem Informasi", "Teknik Informatika", "Bisnis Digital"],
        state="readonly",
        font=font(11)
    )
    jurusan_combo.grid(row=3, column=1, sticky="ew", pady=12)

    field_label("IPK", 4)
    ipk_entry = styled_entry(form_frame, width=32, size=11)
    ipk_entry.grid(row=4, column=1, sticky="ew", pady=12, ipady=5)

    message_label = tk.Label(
        content,
        text="",
        font=font(10, "bold"),
        fg=DANGER,
        bg=BG_LIGHT
    )
    message_label.pack(pady=(15, 0))

    def get_input():
        return (
            nim_entry.get(),
            nama_entry.get(),
            kelas_combo.get(),
            jurusan_combo.get(),
            ipk_entry.get()
        )

    def clear_form():
        nim_entry.delete(0, tk.END)
        nama_entry.delete(0, tk.END)
        kelas_combo.set("")
        jurusan_combo.set("")
        ipk_entry.delete(0, tk.END)

    def input_stack():
        nim, nama, kelas, jurusan, ipk = get_input()

        berhasil, message = add_mahasiswa(
            nim, nama, kelas, jurusan, ipk
        )

        if berhasil:
            message_label.config(
                fg=SUCCESS,
                text="✓ Data berhasil dimasukkan ke Stack"
            )
            clear_form()
        else:
            message_label.config(fg=DANGER, text=message)

    def input_queue():
        nim, nama, kelas, jurusan, ipk = get_input()

        berhasil, message = add_mahasiswa(
            nim, nama, kelas, jurusan, ipk
        )

        if berhasil:
            message_label.config(
                fg=SUCCESS,
                text="✓ Data berhasil dimasukkan ke Queue"
            )
            clear_form()
        else:
            message_label.config(fg=DANGER, text=message)

    button_frame = tk.Frame(content, bg=BG_LIGHT)
    button_frame.pack(pady=25)

    stack_button = styled_button(
        button_frame,
        "📥  Input Stack",
        input_stack,
        bg=PRIMARY,
        hover=PRIMARY_DARK,
        width=20,
        height=2
    )
    stack_button.grid(row=0, column=0, padx=10)

    queue_button = styled_button(
        button_frame,
        "📤  Input Queue",
        input_queue,
        bg=PRIMARY,
        hover=PRIMARY_DARK,
        width=20,
        height=2
    )
    queue_button.grid(row=0, column=1, padx=10)