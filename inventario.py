from logicapi import *

conexion=logicap()

def entrada():
    conexion.registraentrada(nombrei.get(),areai.get(),noserie.get(),cantidadi.get(),fechaentrada.get())

#ventana inventario 

ventana = Tk()
ventana.title("base de datos Frames")
ventana.geometry("600x400")

note= ttk.Notebook(ventana)
note.pack()


# registrar entrada

inventario = Frame(note,width=400,height=400)
inventario.pack(expand=True,fill='both')
note.add(inventario,text="registrar en el inventario")

texto=Label(inventario,text="nombre")
texto.place(x=20, y=20)
nombrei=StringVar()
nombre5=Entry(inventario,textvariable=nombrei)
nombre5.place(x=110, y=20)

texto=Label(inventario,text="area")
texto.place(x=20, y=60)
areai=StringVar()
areai1=Entry(inventario,textvariable=areai)
areai1.place(x=110, y=60)

texto=Label(inventario,text="no. de serie")
texto.place(x=20, y=100)
noserie=StringVar()
noserie1=Entry(inventario,textvariable=noserie)
noserie1.place(x=110, y=100)

texto=Label(inventario,text="cantidad")
texto.place(x=20, y=140)
cantidadi=StringVar()
cantidad1=Entry(inventario,textvariable=cantidadi)
cantidad1.place(x=110, y=140)

texto=Label(inventario,text="fecha entrada")
texto.place(x=20, y=180)
fechaentrada=StringVar()
fechae=Entry(inventario,textvariable=fechaentrada)
fechae.place(x=110, y=180)


boton=Button(inventario,text="agregar",command=entrada)
boton.place(x=150, y=220)





ventana.mainloop()