
import tkinter as tk

window = tk.Tk()
window.title("My Calculator")
window.geometry("340x480")
window.resizable(False, False)
window.configure(bg="#1e1e2e")

display = tk.Entry(
    window,
    font=("Arial", 26),
    bg="#313244",
    fg="white",
    insertbackground="white",
    justify="right",
    bd=0
)
display.pack(fill="x", padx=15, pady=20, ipady=15)

def press(value):
    display.insert(tk.END, value)

def clear():
    display.delete(0, tk.END)

def calculate():
    try:
        expression = display.get()
        allowed = "0123456789+-*/.() "
        if not expression or any(c not in allowed for c in expression):
            raise ValueError
        result = eval(expression, {"__builtins__": {}}, {})
        clear()
        display.insert(0, str(result))
    except Exception:
        clear()
        display.insert(0, "Error")

buttons = [
    ["C", "(", ")", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "⌫", "="]
]

frame = tk.Frame(window, bg="#1e1e2e")
frame.pack(expand=True, fill="both", padx=10, pady=5)

for r, row in enumerate(buttons):
    for c, value in enumerate(row):
        if value == "C":
            command = clear
        elif value == "=":
            command = calculate
        elif value == "⌫":
            command = lambda: display.delete(
                len(display.get()) - 1, tk.END
            ) if display.get() else None
        else:
            command = lambda v=value: press(v)

        color = "#89b4fa" if value in "+-*/=" else "#45475a"
        if value == "C":
            color = "#f38ba8"

        tk.Button(
            frame,
            text=value,
            font=("Arial", 17, "bold"),
            bg=color,
            fg="white",
            activebackground="#b4befe",
            activeforeground="#1e1e2e",
            bd=0,
            command=command
        ).grid(row=r, column=c, sticky="nsew", padx=4, pady=4)

for i in range(4):
    frame.grid_columnconfigure(i, weight=1)

for i in range(5):
    frame.grid_rowconfigure(i, weight=1)

window.mainloop()
