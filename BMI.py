from tkinter import *
from tkinter import messagebox

def reset_entry():
    age_tf.delete(0, 'end')
    height_tf.delete(0, 'end')
    weight_tf.delete(0, 'end')

def calculate_bmi():
    unit_type = unit_var.get()
    height = float(height_tf.get())
    weight = float(weight_tf.get())
    
    if unit_type == 1:  # Metric: cm, kg
        m = height / 100
        kg = weight
    else:  # Imperial: inches, lbs
        m = height * 0.0254
        kg = weight * 0.453592

    bmi = kg / (m * m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('BMI Result', f'BMI = {bmi} is Underweight')
    elif 18.5 <= bmi <= 24.9:
        messagebox.showinfo('BMI Result', f'BMI = {bmi} is Normal')
    elif 24.9 < bmi <= 29.9:
        messagebox.showinfo('BMI Result', f'BMI = {bmi} is Overweight')
    elif bmi > 29.9:
        messagebox.showinfo('BMI Result', f'BMI = {bmi} is Obesity') 
    else:
        messagebox.showerror('BMI Result', 'Something went wrong!')

ws = Tk()
ws.title('BMI Calculator')
ws.geometry('400x350')
ws.config(bg='#686e70')

var = IntVar()
unit_var = IntVar(value=1)  # Default to metric units

frame = Frame(ws, padx=10, pady=10)
frame.pack(expand=True)

age_lb = Label(frame, text="Enter Age (2 - 120)")
age_lb.grid(row=1, column=1)

age_tf = Entry(frame)
age_tf.grid(row=1, column=2, pady=5)

gen_lb = Label(frame, text='Select Gender')
gen_lb.grid(row=2, column=1)

frame2 = Frame(frame)
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(frame2, text='Male', variable=var, value=1)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(frame2, text='Female', variable=var, value=2)
female_rb.pack(side=RIGHT)

unit_lb = Label(frame, text='Select Units')
unit_lb.grid(row=3, column=1)

frame3 = Frame(frame)
frame3.grid(row=3, column=2, pady=5)

metric_rb = Radiobutton(frame3, text='cm/kg', variable=unit_var, value=1)
metric_rb.pack(side=LEFT)

imperial_rb = Radiobutton(frame3, text='inches/lbs', variable=unit_var, value=2)
imperial_rb.pack(side=RIGHT)

height_lb = Label(frame, text="Enter Height")
height_lb.grid(row=4, column=1)

height_tf = Entry(frame)
height_tf.grid(row=4, column=2, pady=5)

weight_lb = Label(frame, text="Enter Weight")
weight_lb.grid(row=5, column=1)

weight_tf = Entry(frame)
weight_tf.grid(row=5, column=2, pady=5)

frame4 = Frame(frame)
frame4.grid(row=6, columnspan=3, pady=10)

cal_btn = Button(frame4, text='Calculate', command=calculate_bmi)
cal_btn.pack(side=LEFT)

reset_btn = Button(frame4, text='Reset', command=reset_entry)
reset_btn.pack(side=LEFT)

exit_btn = Button(frame4, text='Exit', command=lambda: ws.destroy())
exit_btn.pack(side=RIGHT)

ws.mainloop()