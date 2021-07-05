import tkinter as tk

app = tk.Tk()
app.title("Calculator")
app.geometry("282x350")

app.configure(bg="#4f4f4f")
result = tk.Variable(app)
tk.Label(app, textvariable=result, font=('calibre', 20, 'normal')).grid(row=1, columnspan=4, padx=3, pady=3, sticky="E")

exp = ""


def operate(self):
    global exp
    if self == '':
        exp = ""
        result.set(exp)
    elif self == '=':
        total = str(eval(exp))
        result.set(total)
        exp = ""
    else:
        exp = exp + self
        result.set(exp)


tk.Button(app, text="CLR", bg="blue", width=9, height=1, command=lambda: operate("")).grid(row=0, column=0, padx=0, pady=3)
tk.Button(app, text="7", bg="yellow", width=5, height=2, font=2, command=lambda: operate("7")).grid(row=2, column=0, padx=2, pady=2)
tk.Button(app, text="8", bg="yellow", width=5, height=2, font=2, command=lambda: operate("8")).grid(row=2, column=1, padx=2, pady=2)
tk.Button(app, text="9", bg="yellow", width=5, height=2, font=2, command=lambda: operate("9")).grid(row=2, column=2, padx=2, pady=2)
tk.Button(app, text="+", bg="yellow", width=5, height=2, font=2, command=lambda: operate("+")).grid(row=2, column=3, padx=2, pady=2)
tk.Button(app, text="4", bg="yellow", width=5, height=2, font=2, command=lambda: operate("4")).grid(row=3, column=0, padx=2, pady=2)
tk.Button(app, text="5", bg="yellow", width=5, height=2, font=2, command=lambda: operate("5")).grid(row=3, column=1, padx=2, pady=2)
tk.Button(app, text="6", bg="yellow", width=5, height=2, font=2, command=lambda: operate("6")).grid(row=3, column=2, padx=2, pady=2)
tk.Button(app, text="-", bg="yellow", width=5, height=2, font=2, command=lambda: operate("-")).grid(row=3, column=3, padx=2, pady=2)
tk.Button(app, text="3", bg="yellow", width=5, height=2, font=2, command=lambda: operate("3")).grid(row=4, column=0, padx=2, pady=2)
tk.Button(app, text="2", bg="yellow", width=5, height=2, font=2, command=lambda: operate("2")).grid(row=4, column=1, padx=2, pady=2)
tk.Button(app, text="1", bg="yellow", width=5, height=2, font=2, command=lambda: operate("1")).grid(row=4, column=2, padx=2, pady=2)
tk.Button(app, text="x", bg="yellow", width=5, height=2, font=2, command=lambda: operate("*")).grid(row=4, column=3, padx=2, pady=2)
tk.Button(app, text=".", bg="yellow", width=5, height=2, font=2, command=lambda: operate(".")).grid(row=5, column=0, padx=2, pady=2)
tk.Button(app, text="0", bg="yellow", width=5, height=2, font=2, command=lambda: operate("0")).grid(row=5, column=1, padx=2, pady=2)
tk.Button(app, text="=", bg="yellow", width=5, height=2, font=2, command=lambda: operate("=")).grid(row=5, column=2, padx=2, pady=2)
tk.Button(app, text="/", bg="yellow", width=5, height=2, font=2, command=lambda: operate("/")).grid(row=5, column=3, padx=2, pady=2)

app.mainloop()