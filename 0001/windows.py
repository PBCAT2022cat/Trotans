import tkinter as tk
from threading import Thread

def run(num):
    win = tk.Tk()
    win.geometry("500x500")
    print(num)
    lab = tk.Label(win,text="我是第"+str(num)+"窗口:)")
    lab.pack()
    win.mainloop()

a=[]
for num in range(20):
    th = Thread(target=run, args = (num,))
    th.start()
    a.append(th)
    th = None
