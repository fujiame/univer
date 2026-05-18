import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from generators import Igenerator, SinusGenerator, SawGenerator, MeanderGenerator, HalfSawGenerator

def genSignal(generator: Igenerator, A: float, t: float, F: float):
    generator.setParams(A, t, F)
    x, y = generator.genSignal()


    chart.clear()
    chart.plot(x, y)
    chart.set_xlabel("Time, [s]")
    chart.set_ylabel("Amplitude, [V]")
    canvas.draw()
    
root = tk.Tk()
root.geometry("800x600+240+25")
root.title("Signal generator")
root.iconbitmap("generative-image.ico")

## Tk variables ##

generators = [
    SinusGenerator(),
    MeanderGenerator(),
    SawGenerator(),
    HalfSawGenerator()
    ]

A = tk.DoubleVar(value=1)
F = tk.DoubleVar(value=1)
t = tk.DoubleVar(value=1)

## BASE FRAMES ##

frameManage = ttk.LabelFrame(root, text="Manage: ", width=300, height=550)
frameChart = ttk.LabelFrame(root, text="Chart: ", width=470, height=550)

frameManage.pack(side=tk.LEFT, fill=tk.Y, padx=[0, 10])
frameChart.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
frameChart.pack_propagate(False)

## FRAME MANAGE ##

lblSignal = ttk.Label(frameManage, text="Signal")
lblA = ttk.Label(frameManage, text="A")
lblF = ttk.Label(frameManage, text="F")
lblt = ttk.Label(frameManage, text="t")
btnGenerate = ttk.Button(frameManage, text="Generate", command=lambda: genSignal(generators[comboSignal.current()], A.get(), t.get(), F.get()))

comboSignal = ttk.Combobox(frameManage, values=generators)
comboSignal.current(0)
entryA = ttk.Entry(frameManage, textvariable=A)
entryF = ttk.Entry(frameManage, textvariable=F)
entryt = ttk.Entry(frameManage, textvariable=t)

lblSignal.grid(row=0, column=0, padx=10,pady=5)
lblA.grid(row=1, column=0)
lblF.grid(row=2, column=0)
lblt.grid(row=3, column=0)
btnGenerate.grid(row=4, column=0, columnspan=2, sticky=tk.EW)

comboSignal.grid(row=0, column=1, padx=10, pady=5)
entryA.grid(row=1, column=1, pady=5)
entryF.grid(row=2, column=1, pady=5)
entryt.grid(row=3, column=1, pady=5)

## FRAME CHART ##

figure = Figure(layout="constrained", figsize=(2,1))
chart = figure.add_subplot()

canvas = FigureCanvasTkAgg(figure, master=frameChart)

toolbar = NavigationToolbar2Tk(canvas, frameChart)
toolbar.update()

toolbar.pack(fill=tk.X)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

canvas.draw()

root.mainloop()