import tkinter as tk
import math

root = tk.Tk()
root.geometry("175x180")
root.title("Calculator")
root.resizable(False, False)

def button(btn, entry):
    txt = btn.cget("text")

    entry.insert(tk.END, txt)

def solve(entry):
    try:
        answer = eval(entry.get())

        entry.delete(0, tk.END)
        entry.insert(tk.END, str(answer))
    except SyntaxError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "The expression has invalid syntax.")
    except NameError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "The expression references a variable or function that does not exist.")
    except TypeError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "The expression contains an invalid operation for the data types used.")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"An unexpected error occurred during evaluation: {e}")

def clearButton(entry):
    entry.delete(0, tk.END)

entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, padx=2, pady=5, columnspan=5)

oneButton = tk.Button(root, text="1", command=lambda : button(oneButton, entry))
oneButton.grid(row=1, column=0, padx=0, pady=1)

twoButton = tk.Button(root, text="2", command=lambda : button(twoButton, entry))
twoButton.grid(row=1, column=1, padx=0, pady=1)

threeButton = tk.Button(root, text="3", command=lambda : button(threeButton, entry))
threeButton.grid(row=1, column=2, padx=0, pady=1)

fourButton = tk.Button(root, text="4", command=lambda : button(fourButton, entry))
fourButton.grid(row=2, column=0, padx=0, pady=1)

fiveButton = tk.Button(root, text="5", command=lambda : button(fiveButton, entry))
fiveButton.grid(row=2, column=1, padx=0, pady=1)

sixButton = tk.Button(root, text="6", command=lambda : button(sixButton, entry))
sixButton.grid(row=2, column=2, padx=0, pady=1)

sevenButton = tk.Button(root, text="7", command=lambda : button(sevenButton, entry))
sevenButton.grid(row=3, column=0, padx=0, pady=1)

eightButton = tk.Button(root, text="8", command=lambda : button(eightButton, entry))
eightButton.grid(row=3, column=1, padx=0, pady=1)

nineButton = tk.Button(root, text="9", command=lambda : button(nineButton, entry))
nineButton.grid(row=3, column=2, padx=0, pady=1)

zeroButton = tk.Button(root, text="0", command=lambda : button(zeroButton, entry))
zeroButton.grid(row=4, column=1, padx=0, pady=1)

dotButton = tk.Button(root, text=".", command=lambda : button(dotButton, entry))
dotButton.grid(row=4, column=2, padx=0, pady=1)

submitButton = tk.Button(root, text="Go", command=lambda : solve(entry))
submitButton.grid(row=0, column=4, padx=5, pady=1)

plusButton = tk.Button(root, text="+", command=lambda : button(plusButton, entry))
plusButton.grid(row=1, column=4, padx=3, pady=1)

minusButton = tk.Button(root, text="-", command=lambda : button(minusButton, entry))
minusButton.grid(row=2, column=4, padx=3, pady=1)

timesButton = tk.Button(root, text="*", command=lambda : button(timesButton, entry))
timesButton.grid(row=3, column=4, padx=3, pady=1)

dividedButton = tk.Button(root, text="/", command=lambda : button(dividedButton, entry))
dividedButton.grid(row=4, column=4, padx=3, pady=1)

clearButtonB = tk.Button(root, text="CE", command=lambda : clearButton(entry))
clearButtonB.grid(row=4, column=0, padx=3, pady=1)

root.mainloop()
