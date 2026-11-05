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

        def create_widgets(self):
        """Создание элементов интерфейса при помощи вкладок Notebook."""
        # Заголовок приложения
        title_label = tk.Label(
            self.root,
            text="Финансовый калькулятор",
            font=("Arial", 16, "bold"),
            bg=settings.BG_PRIMARY,
            fg=settings.COLOR_ACCENT
        )
        title_label.pack(pady=15)

        # Создание панели вкладок
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=15, pady=10)

        # Вкладка 1: Кредитный калькулятор
        self.loan_frame = tk.Frame(self.notebook, bg=settings.BG_CARD)
        self.notebook.add(self.loan_frame, text=" Кредит (Аннуитет) ")
        self.setup_loan_tab()

        # Вкладка 2: Депозитный калькулятор
        self.deposit_frame = tk.Frame(self.notebook, bg=settings.BG_CARD)
        self.notebook.add(self.deposit_frame, text=" Депозит (Вклад) ")
        self.setup_deposit_frame()

    def setup_loan_tab(self):
        """Элементы управления для вкладки Кредит."""
        container = tk.Frame(self.loan_frame, bg=settings.BG_CARD)
        container.pack(pady=20, padx=20, fill=tk.BOTH)

        # Поля ввода
        tk.Label(container, text="Сумма кредита (руб.):", font=("Arial", 10), bg=settings.BG_CARD).grid(row=0, column=0, sticky="w", pady=5)
        self.loan_amount = tk.Entry(container, font=("Arial", 11))
        self.loan_amount.grid(row=0, column=1, pady=5, padx=10, sticky="we")

        tk.Label(container, text="Срок кредита (месяцев):", font=("Arial", 10), bg=settings.BG_CARD).grid(row=1, column=0, sticky="w", pady=5)
        self.loan_term = tk.Entry(container, font=("Arial", 11))
        self.loan_term.grid(row=1, column=1, pady=5, padx=10, sticky="we")

        tk.Label(container, text="Годовая ставка (%):", font=("Arial", 10), bg=settings.BG_CARD).grid(row=2, column=0, sticky="w", pady=5)
        self.loan_rate = tk.Entry(container, font=("Arial", 11))
        self.loan_rate.grid(row=2, column=1, pady=5, padx=10, sticky="we")

        # Кнопка расчета
        btn_calc = tk.Button(container, text="Рассчитать", command=self.calculate_loan, bg=settings.COLOR_ACCENT, fg="white", font=("Arial", 10, "bold"))
        btn_calc.grid(row=3, column=0, columnspan=2, pady=15, sticky="we")

        # Блок вывода результатов
        self.loan_result = tk.Label(container, text="", font=("Arial", 11), bg=settings.BG_CARD, justify=tk.LEFT, anchor="w")
        self.loan_result.grid(row=4, column=0, columnspan=2, pady=10, sticky="w")

        container.grid_columnconfigure(1, weight=1)

        def setup_deposit_frame(self):
        """Элементы управления для вкладки Депозит."""
        container = tk.Frame(self.deposit_frame, bg=settings.BG_CARD)
        container.pack(pady=20, padx=20, fill=tk.BOTH)

        # Поля ввода
        tk.Label(container, text="Сумма вклада (руб.):", font=("Arial", 10), bg=settings.BG_CARD).grid(row=0, column=0, sticky="w", pady=5)
        self.dep_amount = tk.Entry(container, font=("Arial", 11))
        self.dep_amount.grid(row=0, column=1, pady=5, padx=10, sticky="we")

        tk.Label(container, text="Срок вклада (месяцев):", font=("Arial", 10), bg=settings.BG_CARD).grid(row=1, column=0, sticky="w", pady=5)
        self.dep_term = tk.Entry(container, font=("Arial", 11))
        self.dep_term.grid(row=1, column=1, pady=5, padx=10, sticky="we")

        tk.Label(container, text="Годовая ставка (%):", font=("Arial", 10), bg=settings.BG_CARD).grid(row=2, column=0, sticky="w", pady=5)
        self.dep_rate = tk.Entry(container, font=("Arial", 11))
        self.dep_rate.grid(row=2, column=1, pady=5, padx=10, sticky="we")

        # Флаг капитализации процентов
        self.cap_var = tk.BooleanVar()
        self.cap_check = tk.Checkbutton(container, text="Ежемесячная капитализация", variable=self.cap_var, bg=settings.BG_CARD, font=("Arial", 10))
        self.cap_check.grid(row=3, column=0, columnspan=2, pady=5, sticky="w")

        # Кнопка расчета
        btn_calc = tk.Button(container, text="Рассчитать", command=self.calculate_deposit, bg=settings.COLOR_ACCENT, fg="white", font=("Arial", 10, "bold"))
        btn_calc.grid(row=4, column=0, columnspan=2, pady=15, sticky="we")

        # Блок вывода результатов
        self.dep_result = tk.Label(container, text="", font=("Arial", 11), bg=settings.BG_CARD, justify=tk.LEFT, anchor="w")
        self.dep_result.grid(row=5, column=0, columnspan=2, pady=10, sticky="w")

        container.grid_columnconfigure(1, weight=1)

    def calculate_loan(self):
        """Логика расчета аннуитетного кредита с обработкой ошибок ввода."""
        try:
            p = float(self.loan_amount.get())
            n = int(self.loan_term.get())
            r = float(self.loan_rate.get()) / 100 / 12  # Месячная процентная ставка

            if p <= 0 or n <= 0 or r <= 0:
                raise ValueError

            # Формула аннуитетного платежа: A = P * (r * (1 + r)^n) / ((1 + r)^n - 1)
            monthly_payment = p * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
            total_payment = monthly_payment * n
            overpayment = total_payment - p

            self.loan_result.config(
                text=f"Ежемесячный платеж:  {monthly_payment:,.2f} руб.\n"
                     f"Общая сумма выплат:  {total_payment:,.2f} руб.\n"
                     f"Переплата по кредиту:  {overpayment:,.2f} руб.",
                fg=settings.COLOR_TEXT
            )
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные положительные числа.")

    def calculate_deposit(self):
        """Логика расчета процентов по вкладу."""
        try:
            p = float(self.dep_amount.get())
            n = int(self.dep_term.get())
            r = float(self.dep_rate.get()) / 100

            if p <= 0 or n <= 0 or r <= 0:
                raise ValueError

            if self.cap_var.get():
                # Сложные проценты (капитализация каждый месяц): S = P * (1 + r/12)^n
                final_amount = p * (1 + r / 12) ** n
            else:
                # Простые проценты (начисление в конце срока): S = P * (1 + r * (n/12))
                final_amount = p * (1 + r * (n / 12))

            profit = final_amount - p

            self.dep_result.config(
                text=f"Итоговая сумма:  {final_amount:,.2f} руб.\n"
                     f"Начисленные проценты:  {profit:,.2f} руб.",
                fg=settings.COLOR_TEXT
            )
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Пожалуйста, введите корректные положительные числа.")

    def clear_all(self):
        """Сброс всех полей ввода и результатов."""
        for entry in [self.loan_amount, self.loan_term, self.loan_rate, self.dep_amount, self.dep_term, self.dep_rate]:
            entry.delete(0, tk.END)
        self.loan_result.config(text="")
        self.dep_result.config(text="")
        self.cap_var.set(False)

    def show_formulas_info(self):
        """Справочное окно с описанием формул."""
        messagebox.showinfo(
            "Информация о расчетах",
            "1. Кредит рассчитывается по стандартной аннуитетной формуле (равные платежи каждый месяц).\n\n"
            "2. Капитализация вклада — это начисление сложных процентов, когда ежемесячный доход прибавляется к основной сумме вклада и в следующем месяце тоже приносит процент."
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = FinancialCalculator(root)
    root.mainloop()