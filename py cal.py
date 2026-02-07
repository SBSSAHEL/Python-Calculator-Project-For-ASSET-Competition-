import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.expression = ""

        # Entry widget to display the current expression
        self.entry = tk.Entry(root, width=25, font=("Arial", 18), borderwidth=2, relief="solid", justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Button layout
        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            'C', '0', '=', '/'
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(root, text=button, width=5, height=2, font=("Arial", 14),
                      command=lambda b=button: self.on_button_click(b)).grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        if button == "C":
            self.expression = ""
        elif button == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"
        else:
            self.expression += button
        self.update_entry()

    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

