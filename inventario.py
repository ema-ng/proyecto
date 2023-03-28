from logicapi import *

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


boton=Button(inventario,text="agregar")
boton.place(x=150, y=220)

#acciones 

    
inventario1 = Frame(note,width=400,height=400)
inventario1.pack(expand=True,fill='both')
note.add(inventario1,text="objeto")

texto=Label(inventario1,text="eliminar del inventario")
texto.pack()


texto=Label(inventario1,text="nombre: ")
texto.place(x=20, y=60)
eliminari=StringVar()
eliminar1=Entry(inventario1,textvariable=eliminari)
eliminar1.place(x=110, y=60)

texto=Label(inventario1,text="id del objeto: ")
texto.place(x=20, y=100)
eliminar2=StringVar()
elimina2=Entry(inventario1,textvariable=eliminar2)
elimina2.place(x=110, y=100)

boton=Button(inventario1,text="eliminar")
boton.place(x=80, y=140)

#buscar


texto=Label(inventario1,text="buscar")
texto.place(x=150, y=180)

texto=Label(inventario1,text="id de objeto")
texto.place(x=20, y=220)
buscara=StringVar()
buscara2= Entry(inventario1,textvariable=buscara)
buscara2.place(x=110, y=220)

texto=Label(inventario1,text="nombre")
texto.place(x=20, y=260)
buscara3=StringVar()
buscara4= Entry(inventario1 ,textvariable=buscara3)
buscara4.place(x=110, y=260)

boton=Button(inventario1,text="buscar")
boton.place(x=150, y=300)

texto=Label(inventario1,text="")
texto.place(x=20, y=310)



ventana.mainloop()