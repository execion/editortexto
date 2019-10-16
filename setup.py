# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.scrolledtext import ScrolledText
from funciones import *

top = Tk()
top.title("Editor de Texto")
top.configure(background = "Grey")

contenido = ScrolledText()
contenido.pack(side=BOTTOM, expand=True, fill=BOTH)

nombreArchivo = Entry()
nombreArchivo.pack(side=LEFT, expand = True, fill=X)

Button(text='Abrir', command=cargar, background = "Grey").pack(side=LEFT)

Button(text='Guardar', command=guardar, background = "Grey").pack(side=LEFT)

mainloop()