import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Style

root = tk.Tk()
root.geometry('430x160')
root.title('Replace')
root.resizable(0, 0)
root.config(bg='#d9d9d9')

root.columnconfigure(0, weight=6)
root.columnconfigure(1, weight=1)

"""
Colored the frames to find fix spacing problems.

s1 = Style()
s1.configure('style1.TFrame', background='red')
s2 = Style()
s2.configure('style2.TFrame', background='green')
"""

input_frame = ttk.Frame(root, style='style1.TFrame')
input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=3)
input_frame.rowconfigure(0, weight=1)
input_frame.rowconfigure(1, weight=1)
input_frame.rowconfigure(2, weight=1)
input_frame.rowconfigure(3, weight=1)
input_frame.grid(column=0, row=0, sticky='ns')

button_frame = ttk.Frame(root, style='style2.TFrame')
button_frame.columnconfigure(0, weight=1)
button_frame.grid(column=1, row=0, sticky='ns')

label_findwhat = ttk.Label(input_frame, text='Find:')
label_findwhat.grid(column=0, row=0, padx=5, pady=5, sticky='w')
label_replace = ttk.Label(input_frame, text='Replace with:')
label_replace.grid(column=0, row=1, padx=5, pady=5, sticky='w')
match_case = tk.StringVar()
match_case_checkbox = ttk.Checkbutton(input_frame, text='Match case', variable=match_case)
match_case_checkbox.grid(column=0, row=2, padx=5, pady=5, sticky='w')
wrap_around = tk.StringVar()
wrap_around_checkbox = ttk.Checkbutton(input_frame, text='Wrap around', variable=wrap_around)
wrap_around_checkbox.grid(column=0, row=3, padx=5, pady=5, sticky='w')

entry_findwhat = ttk.Entry(input_frame, width=32)
entry_findwhat.grid(column=1, row=0, sticky='ew')
entry_replace = ttk.Entry(input_frame, width=32)
entry_replace.grid(column=1, row=1, sticky='ew')

btn_find = ttk.Button(button_frame, text='Find Next').grid(column=0, row=0, padx=5, pady=5)
btn_replace = ttk.Button(button_frame, text='Replace').grid(column=0, row=1, padx=5, pady=5)
btn_replace_all = ttk.Button(button_frame, text='Replace All').grid(column=0, row=2, padx=5, pady=5)
btn_cancel = ttk.Button(button_frame, text='Cancel').grid(column=0, row=3, padx=5, pady=5)

root.mainloop()