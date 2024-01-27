from tkinter import *

ventana =  Tk()
ventana.title("Calculadora")

#Entrada
e_texto = Entry(ventana, font= ("Calibri 20"))
e_texto.grid(row = 0, column= 0, columnspan= 4, padx =5, pady=5)

ventana.mainloop()