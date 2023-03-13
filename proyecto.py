from logicapi import *


cliente=[]
empleado=[]
provedor=[]
administrativo=[]


    

# ventanas base de datos

ventana = Tk()
ventana.title("base de datos Frames")
ventana.geometry("600x400")

note= ttk.Notebook(ventana)
note.pack()

#registro clientes

def añadircliente():
    a=str(nombrec.get())
    b=int(idc.get())
    c=str(productoc.get())
    d=str(cantidadc.get())
    
    cliente.append([a,b,c,d])
    cliente.sort()
    
    messagebox.showinfo("registro","registro exitoso")
    
    
def buscarcliente():
    a=int(buscarc.get())
    b=cliente.pop(a)
    messagebox.showinfo("buscar",f'datos del cliente"{b}"')
    
    
clientes = Frame(note,width=400,height=400)
clientes.pack(expand=True,fill='both')
note.add(clientes,text="clientes")
texto=Label(clientes,text="registro de clientes")


texto=Label(clientes,text="nombre")
texto.place(x=20, y=20)
nombrec=StringVar()
nombre1=Entry(clientes,textvariable=nombrec)
nombre1.place(x=110, y=20)

texto=Label(clientes,text="id de cliente")
texto.place(x=20, y=60)
idc=StringVar()
id1=Entry(clientes,textvariable=idc)
id1.place(x=110, y=60)

texto=Label(clientes,text="id de producto")
texto.place(x=20, y=100)
productoc=StringVar()
producto1=Entry(clientes,textvariable=productoc)
producto1.place(x=110, y=100)

texto=Label(clientes,text="cantidad:")
texto.place(x=20, y=140)
cantidadc=StringVar()
cantidad1=Entry(clientes,textvariable=cantidadc)
cantidad1.place(x=110, y=140)

boton=Button(clientes,text="registrar",command=añadircliente)
boton.place(x=80, y=180)

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

boton=Button(clientes,text="buscar",command=buscarcliente)
boton.place(x=150, y=340)

texto=Label(clientes,text="")
texto.place(x=20, y=350)



#registrar empleados 

def añadirempleado():
    a=str(nombree.get())
    b=int(ide.get())
    c=str(areae.get())
    
    empleado.append([a,b,c])
    empleado.sort()
    
    messagebox.showinfo("registro","registro exitoso")
    
def buscarempleado():
    a=int(buscare.get())
    b=cliente.pop(a)
    messagebox.showinfo("buscar",f'datos del cliente"{b}"')
    
empleados = Frame(note,width=400,height=400)
empleados.pack(expand=True,fill='both')
note.add(empleados,text="empleados")
texto=Label(empleados,text="registro de empleados")

texto=Label(empleados,text="nombre")
texto.place(x=20, y=20)
nombree=StringVar()
nombre2=Entry(empleados,textvariable=nombree)
nombre2.place(x=110, y=20)

texto=Label(empleados,text="id de empleado")
texto.place(x=20, y=60)
ide=StringVar()
id2=Entry(empleados,textvariable=ide)
id2.place(x=110, y=60)

texto=Label(empleados,text="area")
texto.place(x=20, y=100)
areae=StringVar()
area1=Entry(empleados,textvariable=areae)
area1.place(x=110, y=100)

boton=Button(empleados,text="registrar",command=añadirempleado)
boton.place(x=80, y=140)

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

boton=Button(empleados,text="buscar",command=buscarempleado)
boton.place(x=150, y=300)

texto=Label(empleados,text="")
texto.place(x=20, y=310)


#provedores 

def añadirprovedor ():
    a=str(nombrep.get())
    b=int(idp.get())
    c=str(productop.get())
    d=str(cantidadp.get())
    
    provedor.append([a,b,c,d])
    provedor.sort()
    
    messagebox.showinfo("registro","registro exitoso")
    
def buscarprovedor():
    a=int(buscarp.get())
    b=cliente.pop(a)
    messagebox.showinfo("buscar",f'datos del cliente"{b}"')

provedores= Frame(note,width=400,height=280)
provedores.pack(expand=True,fill='both')
note.add(provedores,text="provedores")
texto=Label(provedores,text="registrar provedores")

texto=Label(provedores,text="nombre")
texto.place(x=20, y=20)
nombrep=StringVar()
nombre3=Entry(provedores,textvariable=nombrep)
nombre3.place(x=110, y=20)

texto=Label(provedores,text="id de empresa")
texto.place(x=20, y=60)
idp=StringVar()
id3=Entry(provedores,textvariable=idp)
id3.place(x=110, y=60)

texto=Label(provedores,text="id productos")
texto.place(x=20, y=100)
productop=StringVar()
producto2=Entry(provedores,textvariable=productop)
producto2.place(x=110, y=100)

texto=Label(provedores,text="cantidad")
texto.place(x=20, y=140)
cantidadp=StringVar()
cantidad2=Entry(provedores,textvariable=cantidadp)
cantidad2.place(x=110, y=140)

boton=Button(provedores,text="registrar",command=añadirprovedor)
boton.place(x=80, y=180)


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

boton=Button(provedores,text="buscar",command=buscarprovedor)
boton.place(x=150, y=340)

texto=Label(provedores,text="")
texto.place(x=20, y=30)

#administrativos 

def añadiradmin ():
    
    a=str(nombrea.get())
    b=int(ida.get())
    c=str(areaa.get())
    
    administrativo.append([a,b,c])
    administrativo.sort()
    
    messagebox.showinfo("registro","registro exitoso")
    
def buscaradmin():
    a=int(buscara.get())
    b=cliente.pop(a)
    messagebox.showinfo("buscar",f'datos del cliente"{b}"')
    
administrativos = Frame(note,width=400,height=280)
administrativos.pack(expand=True,fill='both')
note.add(administrativos,text="administrativos")
texto=Label(administrativos,text="registrar administrativos")

texto=Label(administrativos,text="nombre")
texto.place(x=20, y=20)
nombrea=StringVar()
nombre4=Entry(administrativos,textvariable=nombrea)
nombre4.place(x=110, y=20)

texto=Label(administrativos,text="id de admin")
texto.place(x=20, y=60)
ida=StringVar()
id4=Entry(administrativos,textvariable=ida)
id4.place(x=110, y=60)

texto=Label(administrativos,text="area")
texto.place(x=20, y=100)
areaa=StringVar()
area2=Entry(administrativos,textvariable=areaa)
area2.place(x=110, y=100)

boton=Button(administrativos,text="registrar",command=añadiradmin)
boton.place(x=80, y=140)


#buscar admin

texto=Label(administrativos,text="buscar")
texto.place(x=150, y=180)

texto=Label(administrativos,text="id admin")
texto.place(x=20, y=220)
buscara=StringVar()
buscara2= Entry(administrativos,textvariable=buscara)
buscara2.place(x=110, y=220)

texto=Label(administrativos,text="nombre")
texto.place(x=20, y=260)
buscara3=StringVar()
buscara4= Entry(administrativos ,textvariable=buscara3)
buscara4.place(x=110, y=260)

boton=Button(administrativos,text="buscar",command=buscaradmin)
boton.place(x=150, y=300)

texto=Label(administrativos,text="")
texto.place(x=20, y=310)


ventana.mainloop()

