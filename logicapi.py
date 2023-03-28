
from tkinter import * 
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import bcrypt


objeto=[]

class logica:
    
    def __init__(self) -> None:
        pass
    
    
    #conexion 
    
    def conexionBD(self):
        
        try:
            conexion= sqlite3.connect("C:/Users/EMMANUEL NORIEGA/Desktop/github/POO181/practica 15/DBU usuarios.db")
            print("conectado a la base BD")
            return conexion
        
        except sqlite3.OperationalError:
            print("no se pudo conectar")