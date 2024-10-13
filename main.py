from tkinter import *
from tkinter import ttk


bmi = int

def Hesapla():
        try:
                label_sonuc = Label(text=" ")
                print("Calculation started..")
                global bmi
                height = float(myEntry_1.get())
                weight = float(myEntry_2.get())
                bmi = height / weight
                if bmi < 18.5 :
                        label_sonuc.config(text=f"Your BMI is : {bmi}  --> Underweight ")
                elif 18.5 <= bmi < 24.9:
                        label_sonuc.config(text=f"Your BMI is : {bmi}  --> healthy range ")

                elif 25 <= bmi < 29.9:
                        label_sonuc.config(text=f"Your BMI is : {bmi}  --> overweight ")
                elif 30 <= bmi < 39.9:
                        label_sonuc.config(text=f"Your BMI is : {bmi}  --> obesity ")
                elif bmi >= 40:
                        label_sonuc.config(text=f"Your BMI is : {bmi}  --> severe obesity ")

                label_sonuc.pack()
        except:
                label_sonuc.config(text= " ")
                label_sonuc.config(text="Please Enter Your Weight Or KG !!")
                label_sonuc.pack()

#Window parameters
root = Tk()
root.title("BMI Calculator")
root.minsize(400,350)

#Label

myLabel = Label(text="Enter your height:",font=('Arial',11))
myLabel.pack()

#Entry

myEntry_1 = Entry(width=15)
myEntry_1.pack()

#Label

myLabel_2 = Label(text="Enter your kg:",font=('Arial',11))
myLabel_2.pack()

#text
myEntry_2 = Entry(width=15)
myEntry_2.pack()






myButton = Button(text="Hesapla",command=Hesapla)
myButton.pack()


root.mainloop()