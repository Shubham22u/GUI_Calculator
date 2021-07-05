import tkinter as tk

app = tk.Tk()
app.title("Basic Calci")
app.geometry("360x500")

result = tk.Variable(app)
result.set("Result")

tk.Label(app, textvariable = result).place(x=160,y=460)

first_val = tk.Variable(app)
second_val =tk.Variable(app)

tk.Entry(app, textvariable = first_val).place(x=40,y=80)
tk.Entry(app, textvariable = second_val).place(x=180,y=80)

def operate(e):
    first = first_val.get()
    second = second_val.get()
    exp = first + e + second

    result.set(str(eval(exp)))


tk.Button(app, text = "+", width = 5, command = lambda :operate("+")).place(x=40,y=200)
tk.Button(app, text = "-", width = 5, command = lambda :operate("-")).place(x=120,y=200)
tk.Button(app, text = "*", width = 5, command = lambda :operate("*")).place(x=200,y=200)
tk.Button(app, text = "/", width = 5, command = lambda :operate("/")).place(x=280,y=200)






app.mainloop()