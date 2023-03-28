from logicapi import *


acciones=logicap()


def guardarc():
   acciones.guardarcliente(nombrec.get(),productoc.get(),cantidadc.get())
   
def guardare():
   acciones.guardarempleado()
   
def guardarp():
   acciones.guardarprovedor()


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

#buscar clientes 

texto=Label(clientes,text="buscar")
texto.place(x=150, y=220)

texto=Label(clientes,text="id de orden")
texto.place(x=20, y=260)
buscarc=StringVar()
buscar1= Entry(clientes,textvariable=buscarc)
buscar1.place(x=110, y=260)

texto=Label(clientes,text="nombre")
texto.place(x=20, y=300)
buscarc2=StringVar()
buscar2= Entry(clientes,textvariable=buscarc2)
buscar2.place(x=110, y=300)

boton=Button(clientes,text="buscar")
boton.place(x=150, y=340)

texto=Label(clientes,text="")
texto.place(x=20, y=350)



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

#buscar empleados 

texto=Label(empleados,text="buscar")
texto.place(x=150, y=180)

texto=Label(empleados,text="id empleado")
texto.place(x=20, y=220)
buscare=StringVar()
buscar3= Entry(empleados,textvariable=buscare)
buscar3.place(x=110, y=220)

texto=Label(empleados,text="nombre")
texto.place(x=20, y=260)
buscare2=StringVar()
buscar4= Entry(empleados ,textvariable=buscare2)
buscar4.place(x=110, y=260)

boton=Button(empleados,text="buscar")
boton.place(x=150, y=300)

texto=Label(empleados,text="")
texto.place(x=20, y=310)


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


# buscar provedor


texto=Label(provedores,text="buscar")
texto.place(x=150, y=220)

texto=Label(provedores,text="id de orden")
texto.place(x=20, y=260)
buscarp=StringVar()
buscarp1= Entry(provedores,textvariable=buscarp)
buscarp1.place(x=110, y=260)

texto=Label(provedores,text="id producto")
texto.place(x=20, y=300)
buscarp2=StringVar()
buscarp3= Entry(provedores ,textvariable=buscarp2)
buscarp3.place(x=110, y=300)

boton=Button(provedores,text="buscar")
boton.place(x=150, y=340)

texto=Label(provedores,text="")
texto.place(x=20, y=30)




ventana.mainloop()

