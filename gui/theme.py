import tkinter as tk
from tkinter import ttk

# ==================== COLOR PALETTE ====================

PRIMARY = "#2563EB"
PRIMARY_DARK = "#1E40AF"
PRIMARY_LIGHT = "#DBEAFE"

SIDEBAR_BG = "#1E293B"
SIDEBAR_HOVER = "#334155"
SIDEBAR_ACTIVE = "#2563EB"

BG_LIGHT = "#F1F5F9"
CARD_BG = "#FFFFFF"

TEXT_DARK = "#0F172A"
TEXT_MUTED = "#64748B"
TEXT_WHITE = "#FFFFFF"

BORDER = "#E2E8F0"

SUCCESS = "#16A34A"
DANGER = "#EF4444"
DANGER_DARK = "#DC2626"

FONT_FAMILY = "Segoe UI"


def font(size=11, weight="normal"):
    return (FONT_FAMILY, size, weight)


# ==================== HELPERS ====================

def add_hover(widget, normal_bg, hover_bg):
    """Bind a simple color-swap hover effect to a tk.Button."""
    widget.bind("<Enter>", lambda e: widget.config(bg=hover_bg))
    widget.bind("<Leave>", lambda e: widget.config(bg=normal_bg))


def styled_button(parent, text, command, bg=PRIMARY, hover=PRIMARY_DARK,
                   fg=TEXT_WHITE, width=20, height=2, size=11):
    btn = tk.Button(
        parent,
        text=text,
        command=command,
        width=width,
        height=height,
        bg=bg,
        fg=fg,
        activebackground=hover,
        activeforeground=fg,
        relief="flat",
        bd=0,
        cursor="hand2",
        font=font(size, "bold")
    )
    add_hover(btn, bg, hover)
    return btn


def styled_entry(parent, width=30, size=12):
    entry = tk.Entry(
        parent,
        width=width,
        font=font(size),
        relief="solid",
        bd=1,
        highlightthickness=1,
        highlightcolor=PRIMARY,
        highlightbackground=BORDER,
        bg="white",
        fg=TEXT_DARK,
        insertbackground=TEXT_DARK
    )
    return entry


def setup_ttk_style():
    """Call once per window to style ttk.Treeview / ttk.Combobox consistently."""
    style = ttk.Style()
    try:
        style.theme_use("clam")
    except tk.TclError:
        pass

    style.configure(
        "Treeview",
        background="white",
        fieldbackground="white",
        foreground=TEXT_DARK,
        rowheight=30,
        font=font(10),
        borderwidth=0
    )
    style.configure(
        "Treeview.Heading",
        background=PRIMARY,
        foreground="white",
        font=font(10, "bold"),
        relief="flat",
        padding=6
    )
    style.map(
        "Treeview.Heading",
        background=[("active", PRIMARY_DARK)]
    )
    style.map(
        "Treeview",
        background=[("selected", PRIMARY_LIGHT)],
        foreground=[("selected", TEXT_DARK)]
    )

    style.configure(
        "TCombobox",
        fieldbackground="white",
        background="white",
        foreground=TEXT_DARK,
        arrowcolor=PRIMARY,
        font=font(10)
    )