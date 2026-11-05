import tkinter as tk
from tkinter import ttk, messagebox
import settings


class FinancialCalculator:
    """Класс графического приложения 'Финансовый калькулятор'."""

    def __init__(self, root):
        self.root = root
        self.root.title(settings.WINDOW_TITLE)
        self.root.geometry(settings.WINDOW_GEOMETRY)
        self.root.configure(bg=settings.BG_PRIMARY)
        self.root.minsize(450, 550)

        self.create_menu()
        self.create_widgets()

    def create_menu(self):
        """Создание верхнего меню приложения."""
        menubar = tk.Menu(self.root)

        # Меню "Программа"
        prog_menu = tk.Menu(menubar, tearoff=0)
        prog_menu.add_command(label="Очистить всё", command=self.clear_all)
        prog_menu.add_separator()
        prog_menu.add_command(label="Выход", command=self.root.quit)
        menubar.add_cascade(label="Программа", menu=prog_menu)

        # Меню "Справка"
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="О формулах", command=self.show_formulas_info)
        menubar.add_cascade(label="Справка", menu=help_menu)

        self.root.config(menu=menubar)