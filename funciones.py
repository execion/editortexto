# -*- coding: utf-8 -*-
def cargar():
    with open(nombreArchivo.get()) as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())
def guardar():
    with open(nombreArchivo.get(), 'w') as file:
        file.write(contents.get('1.0', END))
