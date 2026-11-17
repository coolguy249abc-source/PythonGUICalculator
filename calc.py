from tkinter import messagebox
import tkinter as tk
import math

root = tk.Tk()
root.geometry("175x180")
root.title("Calculator")
root.resizable(False, False)

menu = tk.Menu(root)

modemenu = tk.Menu(menu, tearoff=0, font=("Helvetica", 9))
modemenu.add_command(label="Basic  ", command=lambda:toBasic())
modemenu.add_command(label="Scientific", command=lambda:toAdvanced())

exitmenu = tk.Menu(menu, tearoff=0, font=("Helvetica", 9))
exitmenu.add_command(label="Exit", command=root.destroy)

helpmenu = tk.Menu(menu, tearoff=0, font=("Helvetica", 9))
helpmenu.add_command(label="Help  ", command=lambda:openHelp())
helpmenu.add_separator()
helpmenu.add_command(label="About", command=lambda:openAbout())

menu.add_cascade(label="Exit", menu=exitmenu, font=("Helvetica", 9))
menu.add_cascade(label="Mode", menu=modemenu, font=("Helvetica", 9))
menu.add_cascade(label="Help", menu=helpmenu, font=("Helvetica", 9))

root.config(menu=menu)

def button(btn, entry):
    txt = btn.cget("text")

    if txt == "mod":
        current_text = entry.get()
        entry.delete(0, tk.END)
        #entry.insert(tk.END, f"math.fmod({current_text})")
    elif txt == "tan":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.tan({current_text})")
    elif txt == "sin":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.sin({current_text})")
    elif txt == "cos":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.cos({current_text})")
    elif txt == "log":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.log({current_text})")
    elif txt == "e":
        current_text = entry.get()
        entry.insert(tk.END, "2.71828182845904523536")
    elif txt == "abs":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.abs({current_text})")
    elif txt == "√":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.sqrt({current_text})")
    elif txt == "π":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, "3.141592653589793238462")
    elif txt == "floor":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.floor({current_text})")
    elif txt == "ceil":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.ceil({current_text})")
    elif txt == "trunc":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.trunc({current_text})")
    elif txt == "fabs":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.fabs({current_text})")
    elif txt == "e^x":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.exp({current_text})")
    elif txt == "sin^-1":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.asin({current_text})")
    elif txt == "cos^-1":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.acos({current_text})")
    elif txt == "tan^-1":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.atan({current_text})")
    elif txt == "deg":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.deg({current_text})")
    elif txt == "rad":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.rad({current_text})")
    elif txt == "!":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.factorial({current_text})")
    elif txt == "log10":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.log10({current_text})")
    elif txt == "log2":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"math.log2({current_text})")
    else:   
        entry.insert(tk.END, txt)

def toAdvanced():
    root.resizable(True, True)
    root.geometry("550x180")
    root.resizable(False, False)

def toBasic():
    root.resizable(True, True)
    root.geometry("175x180")
    root.resizable(False, False)

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

def openAbout():
    messagebox.showinfo("About", "Made by XXXXX\nv1.0\nNov 2026")

def openHelp():
    messagebox.showinfo("Help", "To use the advanced functions, first choose the number you want to use the function with, and then choose the function. Or you can write math.func(x, y)\nOther functions such as mod(x, y) and pow(x, y) are also available. look through all the functions in the python math module")

# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)
# root.columnconfigure(2, weight=1)
# root.columnconfigure(4, weight=1)

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

modButton = tk.Button(root, text="mod", command=lambda : button(modButton, entry))
modButton.grid(row=0, column=5, padx=5, pady=1)

tanButton = tk.Button(root, text="tan", command=lambda : button(tanButton, entry))
tanButton.grid(row=1, column=5, padx=3, pady=1)

cosButton = tk.Button(root, text="cos", command=lambda : button(cosButton, entry))
cosButton.grid(row=2, column=5, padx=3, pady=1)

sinButton = tk.Button(root, text="sin", command=lambda : button(sinButton, entry))
sinButton.grid(row=3, column=5, padx=3, pady=1)

absButton = tk.Button(root, text="abs", command=lambda : button(absButton, entry))
absButton.grid(row=4, column=5, padx=5, pady=1)

sqrtButton = tk.Button(root, text="√", command=lambda : button(sqrtButton, entry))
sqrtButton.grid(row=0, column=6, padx=3, pady=1)

piButton = tk.Button(root, text="π", command=lambda : button(piButton, entry))
piButton.grid(row=1, column=6, padx=3, pady=1)

logButton = tk.Button(root, text="log", command=lambda : button(logButton, entry))
logButton.grid(row=2, column=6, padx=3, pady=1)

eulerButton = tk.Button(root, text="e", command=lambda : button(eulerButton, entry))
eulerButton.grid(row=3, column=6, padx=5, pady=1)

floorButton = tk.Button(root, text="floor", command=lambda : button(floorButton, entry))
floorButton.grid(row=4, column=6, padx=5, pady=1)

ceilButton = tk.Button(root, text="ceil", command=lambda : button(ceilButton, entry))
ceilButton.grid(row=0, column=7, padx=5, pady=1)

truncButton = tk.Button(root, text="trunc", command=lambda : button(truncButton, entry))
truncButton.grid(row=1, column=7, padx=5, pady=1)

fabsButton = tk.Button(root, text="fabs", command=lambda : button(fabsButton, entry))
fabsButton.grid(row=2, column=7, padx=5, pady=1)

expButton = tk.Button(root, text="e^x", command=lambda : button(expButton, entry))
expButton.grid(row=3, column=7, padx=5, pady=1)

asinButton = tk.Button(root, text="sin^-1", command=lambda : button(asinButton, entry))
asinButton.grid(row=4, column=7, padx=5, pady=1)

acosButton = tk.Button(root, text="cos^-1", command=lambda : button(acosButton, entry))
acosButton.grid(row=0, column=8, padx=5, pady=1)

atanButton = tk.Button(root, text="tan^-1", command=lambda : button(atanButton, entry))
atanButton.grid(row=1, column=8, padx=5, pady=1)

degButton = tk.Button(root, text="deg", command=lambda : button(degButton, entry))
degButton.grid(row=2, column=8, padx=5, pady=1)

radButton = tk.Button(root, text="rad", command=lambda : button(radButton, entry))
radButton.grid(row=3, column=8, padx=5, pady=1)

facButton = tk.Button(root, text="!", command=lambda : button(facButton, entry))
facButton.grid(row=4, column=8, padx=5, pady=1)

log10Button = tk.Button(root, text="log10", command=lambda : button(log10Button, entry))
log10Button.grid(row=0, column=9, padx=5, pady=1)

log2Button = tk.Button(root, text="log2", command=lambda : button(log2Button, entry))
log2Button.grid(row=1, column=9, padx=5, pady=1)

minusButton = tk.Button(root, text="-", command=lambda : button(minusButton, entry))
minusButton.grid(row=2, column=4, padx=3, pady=1)

timesButton = tk.Button(root, text="*", command=lambda : button(timesButton, entry))
timesButton.grid(row=3, column=4, padx=3, pady=1)

dividedButton = tk.Button(root, text="/", command=lambda : button(dividedButton, entry))
dividedButton.grid(row=4, column=4, padx=3, pady=1)

clearButtonB = tk.Button(root, text="CE", command=lambda : clearButton(entry))
clearButtonB.grid(row=4, column=0, padx=3, pady=1)

root.mainloop()