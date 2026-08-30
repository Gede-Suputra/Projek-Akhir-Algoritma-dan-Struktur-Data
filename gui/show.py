import tkinter as tk
from tkinter import ttk
import json

from logic.sorting import bubble_sort
from logic.searchData import linear_search
from gui.theme import (
    BG_LIGHT,
    CARD_BG,
    TEXT_DARK,
    TEXT_MUTED,
    PRIMARY,
    PRIMARY_DARK,
    DANGER,
    DANGER_DARK,
    BORDER,
    font,
    styled_entry,
    styled_button
)


def gui_show_data(content, center_window):
    title = tk.Label(
        content,
        text="Data Mahasiswa",
        font=font(16, "bold"),
        fg=TEXT_DARK,
        bg=BG_LIGHT
    )
    title.pack(pady=(12, 0), padx=25, anchor="w")

    subtitle = tk.Label(
        content,
        text="Kelola, urutkan, dan cari data mahasiswa",
        font=font(9),
        fg=TEXT_MUTED,
        bg=BG_LIGHT
    )
    subtitle.pack(padx=25, anchor="w", pady=(0, 8))

    with open("data/mahasiswa.json", "r") as file:
        data = json.load(file)

    mahasiswa_data = data["mahasiswa"]

    berdasarkan = {
        "NIM": "nim",
        "Nama": "nama",
        "Kelas": "kelas",
        "Jurusan": "jurusan",
        "IPK": "ipk"
    }

    # ==================== TOOLBAR CARD ====================

    toolbar = tk.Frame(
        content,
        bg=CARD_BG,
        highlightbackground=BORDER,
        highlightthickness=1
    )
    toolbar.pack(padx=25, fill="x")

    filter_frame = tk.Frame(
        toolbar,
        bg=CARD_BG
    )
    filter_frame.pack(
        padx=15,
        pady=8,
        fill="x"
    )

    # ==================== SORT ====================

    tk.Label(
        filter_frame,
        text="Urutan",
        font=font(8, "bold"),
        bg=CARD_BG,
        fg=TEXT_MUTED
    ).grid(
        row=0,
        column=0,
        sticky="w",
        padx=(0, 5)
    )

    order_combo = ttk.Combobox(
        filter_frame,
        values=[
            "Ascending (A-Z)",
            "Descending (Z-A)"
        ],
        state="readonly",
        width=15,
        font=font(9)
    )

    order_combo.current(0)

    order_combo.grid(
        row=1,
        column=0,
        padx=(0, 8),
        sticky="w"
    )

    tk.Label(
        filter_frame,
        text="Berdasarkan",
        font=font(8, "bold"),
        bg=CARD_BG,
        fg=TEXT_MUTED
    ).grid(
        row=0,
        column=1,
        sticky="w",
        padx=(0, 5)
    )

    sort_combo = ttk.Combobox(
        filter_frame,
        values=list(berdasarkan.keys()),
        state="readonly",
        width=12,
        font=font(9)
    )

    sort_combo.current(0)

    sort_combo.grid(
        row=1,
        column=1,
        padx=(0, 8),
        sticky="w"
    )

    # ==================== SEARCH ====================

    tk.Label(
        filter_frame,
        text="Cari",
        font=font(8, "bold"),
        bg=CARD_BG,
        fg=TEXT_MUTED
    ).grid(
        row=0,
        column=2,
        sticky="w",
        padx=(0, 5)
    )

    search_entry = styled_entry(
        filter_frame,
        width=20,
        size=9
    )

    search_entry.grid(
        row=1,
        column=2,
        padx=(0, 8),
        sticky="w",
        ipady=2
    )

    button_col = tk.Frame(
        filter_frame,
        bg=CARD_BG
    )

    button_col.grid(
        row=1,
        column=3,
        sticky="w"
    )

    # ==================== TABLE CARD ====================

    table_card = tk.Frame(
        content,
        bg=CARD_BG,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    table_card.pack(
        padx=25,
        pady=8,
        fill="both",
        expand=True
    )

    table_frame = tk.Frame(
        table_card,
        bg=CARD_BG
    )

    table_frame.pack(
        padx=10,
        pady=8,
        fill="both",
        expand=True
    )

    columns = (
        "nim",
        "nama",
        "kelas",
        "jurusan",
        "ipk"
    )

    headers = {
        "nim": "NIM",
        "nama": "Nama",
        "kelas": "Kelas",
        "jurusan": "Jurusan",
        "ipk": "IPK"
    }

    widths = {
        "nim": 100,
        "nama": 150,
        "kelas": 50,
        "jurusan": 200,
        "ipk": 55
    }

    table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings",
        height=10
    )

    for col in columns:
        table.heading(
            col,
            text=headers[col]
        )

        table.column(
            col,
            width=widths[col],
            anchor="center"
            if col in ("kelas", "ipk")
            else "w"
        )

    table.tag_configure(
        "oddrow",
        background="#F8FAFC"
    )

    table.tag_configure(
        "evenrow",
        background="#FFFFFF"
    )

    table.pack(
        fill="both",
        expand=True
    )

    # ==================== DISPLAY DATA ====================

    def tampilkan_data(data_mahasiswa):
        for item in table.get_children():
            table.delete(item)

        for i, mahasiswa in enumerate(data_mahasiswa):
            tag = (
                "evenrow"
                if i % 2 == 0
                else "oddrow"
            )

            table.insert(
                "",
                "end",
                values=(
                    mahasiswa["nim"],
                    mahasiswa["nama"],
                    mahasiswa["kelas"],
                    mahasiswa["jurusan"],
                    mahasiswa["ipk"]
                ),
                tags=(tag,)
            )

    tampilkan_data(mahasiswa_data)

    # ==================== SORT FUNCTION ====================

    def sort_data():
        field = berdasarkan[sort_combo.get()]

        ascending = (
            order_combo.get()
            == "Ascending (A-Z)"
        )

        hasil_sort = bubble_sort(
            mahasiswa_data.copy(),
            field,
            ascending
        )

        tampilkan_data(
            hasil_sort
        )

    # ==================== SEARCH FUNCTION ====================

    def search_data():
        keyword = search_entry.get().strip()

        if not keyword:
            return

        field = berdasarkan[
            sort_combo.get()
        ]

        hasil_search = linear_search(
            mahasiswa_data,
            keyword,
            field
        )

        popup = tk.Toplevel(content)

        popup.title(
            "Hasil Linear Search"
        )

        popup.resizable(
            False,
            False
        )

        popup.configure(
            bg=BG_LIGHT
        )

        center_window(
            popup,
            700,
            380
        )

        popup.transient(
            content.winfo_toplevel()
        )

        header = tk.Frame(
            popup,
            bg=PRIMARY,
            height=55
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(
            False
        )

        tk.Label(
            header,
            text="Hasil Linear Search",
            font=font(13, "bold"),
            bg=PRIMARY,
            fg="white"
        ).pack(
            pady=15
        )

        if len(hasil_search) == 0:
            message = tk.Label(
                popup,
                text="😕  Data tidak ditemukan",
                font=font(11),
                bg=BG_LIGHT,
                fg=TEXT_MUTED
            )

            message.pack(
                pady=40
            )

            close_button = styled_button(
                popup,
                "Tutup",
                popup.destroy,
                bg=PRIMARY,
                hover=PRIMARY_DARK,
                width=15,
                height=1,
                size=9
            )

            close_button.pack(
                pady=10
            )

            return

        result_card = tk.Frame(
            popup,
            bg=CARD_BG,
            highlightbackground=BORDER,
            highlightthickness=1
        )

        result_card.pack(
            padx=15,
            pady=10,
            fill="both",
            expand=True
        )

        result_frame = tk.Frame(
            result_card,
            bg=CARD_BG
        )

        result_frame.pack(
            padx=8,
            pady=8
        )

        result_columns = (
            "index",
            "nim",
            "nama",
            "kelas",
            "jurusan",
            "ipk"
        )

        result_headers = {
            "index": "Index",
            "nim": "NIM",
            "nama": "Nama",
            "kelas": "Kelas",
            "jurusan": "Jurusan",
            "ipk": "IPK"
        }

        result_widths = {
            "index": 50,
            "nim": 90,
            "nama": 125,
            "kelas": 50,
            "jurusan": 170,
            "ipk": 55
        }

        result_table = ttk.Treeview(
            result_frame,
            columns=result_columns,
            show="headings",
            height=7
        )

        for col in result_columns:
            result_table.heading(
                col,
                text=result_headers[col]
            )

            result_table.column(
                col,
                width=result_widths[col],
                anchor="center"
                if col in (
                    "index",
                    "kelas",
                    "ipk"
                )
                else "w"
            )

        result_table.tag_configure(
            "oddrow",
            background="#F8FAFC"
        )

        result_table.tag_configure(
            "evenrow",
            background="#FFFFFF"
        )

        result_table.pack()

        for i, mahasiswa in enumerate(
            hasil_search
        ):
            index = mahasiswa_data.index(
                mahasiswa
            )

            tag = (
                "evenrow"
                if i % 2 == 0
                else "oddrow"
            )

            result_table.insert(
                "",
                "end",
                values=(
                    index,
                    mahasiswa["nim"],
                    mahasiswa["nama"],
                    mahasiswa["kelas"],
                    mahasiswa["jurusan"],
                    mahasiswa["ipk"]
                ),
                tags=(tag,)
            )

        close_button = styled_button(
            popup,
            "Tutup",
            popup.destroy,
            bg=PRIMARY,
            hover=PRIMARY_DARK,
            width=15,
            height=1,
            size=9
        )

        close_button.pack(
            pady=10
        )

    # ==================== TOOLBAR BUTTONS ====================

    sort_button = styled_button(
        button_col,
        "⇅ Sort",
        sort_data,
        bg=PRIMARY,
        hover=PRIMARY_DARK,
        width=8,
        height=1,
        size=8
    )

    sort_button.pack(
        side="left",
        padx=(0, 6)
    )

    search_button = styled_button(
        button_col,
        "🔍 Cari",
        search_data,
        bg=PRIMARY,
        hover=PRIMARY_DARK,
        width=8,
        height=1,
        size=8
    )

    search_button.pack(
        side="left"
    )

    # ==================== STACK & QUEUE CARD ====================

    structure_card = tk.Frame(
        content,
        bg=CARD_BG,
        highlightbackground=BORDER,
        highlightthickness=1
    )

    structure_card.pack(
        padx=25,
        pady=(0, 10),
        fill="x"
    )

    tk.Label(
        structure_card,
        text="Simulasi Struktur Data",
        font=font(9, "bold"),
        bg=CARD_BG,
        fg=TEXT_DARK
    ).pack(
        anchor="w",
        padx=15,
        pady=(8, 0)
    )

    structure_frame = tk.Frame(
        structure_card,
        bg=CARD_BG
    )

    structure_frame.pack(
        pady=8
    )

    # Salinan data untuk Stack dan Queue
    stack_data = mahasiswa_data.copy()
    queue_data = mahasiswa_data.copy()

    # ==================== STACK POP ====================

    def proses_stack():
        if len(stack_data) == 0:
            return

        stack_data.pop()

        tampilkan_data(
            stack_data
        )

    # ==================== QUEUE DEQUEUE ====================

    def proses_queue():
        if len(queue_data) == 0:
            return

        queue_data.pop(0)

        tampilkan_data(
            queue_data
        )

    # ==================== STACK DISPLAY ====================

    def tampilkan_stack():
        hasil_stack = list(
            reversed(mahasiswa_data)
        )

        tampilkan_data(
            hasil_stack
        )

    # ==================== QUEUE DISPLAY ====================

    def tampilkan_queue():
        hasil_queue = mahasiswa_data.copy()

        tampilkan_data(
            hasil_queue
        )

    # ==================== RESET ====================

    def reset_data():
        stack_data.clear()
        stack_data.extend(
            mahasiswa_data
        )

        queue_data.clear()
        queue_data.extend(
            mahasiswa_data
        )

        search_entry.delete(
            0,
            tk.END
        )

        tampilkan_data(
            mahasiswa_data
        )

    # ==================== STACK POP BUTTON ====================

    stack_button = styled_button(
        structure_frame,
        "📦 STACK (POP)",
        proses_stack,
        bg=PRIMARY,
        hover=PRIMARY_DARK,
        width=17,
        height=1,
        size=11
    )

    stack_button.grid(
        row=0,
        column=0,
        padx=6,
        pady=3
    )

    # ==================== QUEUE DEQUEUE BUTTON ====================

    queue_button = styled_button(
        structure_frame,
        "🚶 QUEUE (DEQUEUE)",
        proses_queue,
        bg=PRIMARY,
        hover=PRIMARY_DARK,
        width=19,
        height=1,
        size=11
    )

    queue_button.grid(
        row=0,
        column=1,
        padx=6,
        pady=3
    )

    # ==================== STACK DISPLAY BUTTON ====================

    stack_view_button = styled_button(
        structure_frame,
        "🔃 STACK (LIFO)",
        tampilkan_stack,
        bg=PRIMARY,
        hover=PRIMARY_DARK,
        width=17,
        height=1,
        size=11
    )

    stack_view_button.grid(
        row=1,
        column=0,
        padx=6,
        pady=3
    )

    # ==================== QUEUE DISPLAY BUTTON ====================

    queue_view_button = styled_button(
        structure_frame,
        "➡ QUEUE (FIFO)",
        tampilkan_queue,
        bg=PRIMARY,
        hover=PRIMARY_DARK,
        width=19,
        height=1,
        size=11
    )

    queue_view_button.grid(
        row=1,
        column=1,
        padx=6,
        pady=3
    )

    # ==================== RESET BUTTON ====================

    reset_button = styled_button(
        structure_frame,
        "🔄 RESET",
        reset_data,
        bg=DANGER,
        hover=DANGER_DARK,
        width=15,
        height=1,
        size=11
    )

    reset_button.grid(
        row=0,
        column=2,
        rowspan=2,
        padx=8,
        pady=3
    )