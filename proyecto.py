
from tkinter import * 
from tkinter import messagebox

lista=[]

def menu():
     
    if (str(opcion1.get())) == str(1):
        messagebox.showinfo("aviso","se cargo el inventario")
  
    elif (str(opcion.get())) == str(2):
        ventana1 = Tk()
        ventana1.title("practica 11:3 Frames")
        ventana1.geometry("600x400")
        seccion2 = Frame(ventana1, bg="white")
        seccion2.pack(expand=True,fill='both')
        tituloa=Label(seccion2,text="ingresa el objeto:",bg="white")
        tituloa.pack()
        opcion13=StringVar()
        opcionb= Entry(seccion2,textvariable=opcion13)
        opcionb.pack()
        boton2=Button (seccion2,text="guardar",bg="white",command=menu)
        boton2.pack()
        
        messagebox.showinfo("aviso","se registro una entrada")
        lista.append(str("objeto 1"))
      
        
    elif (str(opcion.get())) == str(3):
        messagebox.showinfo("aviso","se registro una salida")
        lista.remove(str("objeto 1"))

        
    elif (str(opcion.get())) == str(5):
       messagebox.showinfo("aviso","este mensaje es para avisar algo")
       print(lista)
    
    elif (str(opcion.get())) == str(6):
        messagebox.showinfo("aviso","se ordenaron los objetos")
        lista.sort

    
ventana = Tk()
ventana.title("practica 11:3 Frames")
ventana.geometry("600x400")


seccion1 = Frame(ventana, bg="white")
seccion1.pack(expand=True,fill='both')

titulo=Label(seccion1,text="seleccione una opcion:",bg="white")
titulo.pack()
titulo=Label(seccion1,text="1.cargar",bg="white")
titulo.pack()
titulo=Label(seccion1,text="2.añadir",bg="white")
titulo.pack()
titulo=Label(seccion1,text="3.eliminar",bg="white")
titulo.pack()
titulo=Label(seccion1,text="5.imprimir",bg="white")
titulo.pack()
titulo=Label(seccion1,text="6.ordenar",bg="white")
titulo.pack()
opcion=StringVar()
opcion1= Entry(seccion1,textvariable=opcion)
opcion1.pack()

boton1=Button (seccion1,text="elegir",bg="white",command=menu)
boton1.pack()

   

ventana.mainloop()