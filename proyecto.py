from logicapi import *


acciones=logicap()


def guardarc():
   acciones.guardarcliente(nombrec.get(),productoc.get(),cantidadc.get())
   
def guardare():
   acciones.guardarempleado(nombree.get(),areae.get(),puestoe.get())
   
def guardarp():
   acciones.guardarprovedor(nombrep.get(),productop.get(),cantidadp.get())


# ventanas base de datos

ventana = Tk()
ventana.title("base de datos Frames")
ventana.geometry("600x400")

note= ttk.Notebook(ventana)
note.pack()


#registro clientes
    
    
clientes = Frame(note,width=400,height=400)
clientes.pack(expand=True,fill='both')
note.add(clientes,text="clientes")
texto=Label(clientes,text="registro de clientes")


texto=Label(clientes,text="nombre")
texto.place(x=20, y=20)
nombrec=StringVar()
nombre1=Entry(clientes,textvariable=nombrec)
nombre1.place(x=110, y=20)

texto=Label(clientes,text="id de producto")
texto.place(x=20, y=60)
productoc=StringVar()
producto1=Entry(clientes,textvariable=productoc)
producto1.place(x=110, y=60)

texto=Label(clientes,text="cantidad:")
texto.place(x=20, y=100)
cantidadc=StringVar()
cantidad1=Entry(clientes,textvariable=cantidadc)
cantidad1.place(x=110, y=100)

boton=Button(clientes,text="registrar",command=guardarc)
boton.place(x=150, y=140)





#registrar empleados 

    
empleados = Frame(note,width=400,height=400)
empleados.pack(expand=True,fill='both')
note.add(empleados,text="empleados")
texto=Label(empleados,text="registro de empleados")

texto=Label(empleados,text="nombre")
texto.place(x=20, y=20)
nombree=StringVar()
nombre2=Entry(empleados,textvariable=nombree)
nombre2.place(x=110, y=20)

texto=Label(empleados,text="area")
texto.place(x=20, y=60)
areae=StringVar()
area1=Entry(empleados,textvariable=areae)
area1.place(x=110, y=60)

texto=Label(empleados,text="puesto")
texto.place(x=20, y=100)
puestoe=StringVar()
puesto1=Entry(empleados,textvariable=puestoe)
puesto1.place(x=110, y=100)

boton=Button(empleados,text="registrar",command=guardare)
boton.place(x=150, y=140)


#provedores 


provedores= Frame(note,width=400,height=280)
provedores.pack(expand=True,fill='both')
note.add(provedores,text="provedores")
texto=Label(provedores,text="registrar provedores")

texto=Label(provedores,text="nombre")
texto.place(x=20, y=20)
nombrep=StringVar()
nombre3=Entry(provedores,textvariable=nombrep)
nombre3.place(x=110, y=20)

texto=Label(provedores,text="id productos")
texto.place(x=20, y=60)
productop=StringVar()
producto2=Entry(provedores,textvariable=productop)
producto2.place(x=110, y=60)

texto=Label(provedores,text="cantidad")
texto.place(x=20, y=100)
cantidadp=StringVar()
cantidad2=Entry(provedores,textvariable=cantidadp)
cantidad2.place(x=110, y=100)

boton=Button(provedores,text="registrar",command=guardarp)
boton.place(x=150, y=140)





ventana.mainloop()

