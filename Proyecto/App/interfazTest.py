# pip install pygame, tkinter
import tkinter as tk; import time, random, rich
from tkinter import *
import baseDeDatos
def botonClick():
	print(":0")
	time.sleep(1)
	time.sleep(1)
	ventana.destroy()
	time.sleep(1)
	print("CHAOOOOOOOOOO")
# Test mejorado de Gemini que funciona
ventana = Tk() # <-- Crea la pantalla que se va a mostrar
ventana.title("Mi primera ventana") # <-- Le da un nombre a la barra superior
etiqueta = tk.Label(ventana, text="¡Hola, Tkinter!") # <-- Imprime texto en la pantalla. Debe ser una variable o no se mostrará
boton = tk.Button(ventana, 
	text="Hola",
	command=botonClick, # <-- Que va a pasar si se presiona el botón 
	activebackground="#ff0080", # <-- Color del botón cuando se presiona 
	activeforeground="#090909", # <-- Color de texto cuando se presiona el botón 
	anchor="center", # <-- Posición del texto 
	disabledforeground="blue",
	fg="black",
	font=("Arial", 12),
	height=2,
	width=20,
	justify="center",
	overrelief="sunken", # <-- Cómo se verá el botón al pasar el cursor sobre este 
	padx=10, # <-- padding izquierda-derecha 
	pady=5, # <-- padding arriba-abajo 
	wraplength=100)
etiqueta.pack()
boton.pack(padx=100, pady=50)
ventana.geometry("1280x720") #<-- Establecer tamaño de la ventana
ventana.mainloop() # <-- Muestra la pantalla