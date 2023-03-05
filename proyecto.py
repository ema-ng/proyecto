

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("que desas reaizar: "))
            correcto=True
        except ValueError:
            print('Error, introduce una opcion del menu')
     
    return num
 
salir = False
opcion = 0
 
while not salir:
    
    

    print("Seleccione una opcion ingresando un numero:")
    print ("1.cargar inventario.")
    print ("2.Añadir.")
    print ("3.Contar")
    print ("4.Eliminar")
    print ("5.Imprimir")
    print ("6.Ordenar")
    print ("7.Salir")
    print ("Elige una opcion")
    print("")

 
    opcion = pedirNumeroEntero()
    
    
    if opcion == 1:
        print("")
        lista=[]
        print("")
    
    elif opcion == 2:
        print("") 
        lista.append(input("ingresa el objeto: "))
        print("")
        
    elif opcion == 3:
        
        print("")
        lista.count
        print("")
        
    elif opcion == 4:
        print("")
        lista.remove(input("que deseas elimiar: "))
        print("")
        
    elif opcion == 5:
       print("")
       print(lista)
       print("")
    
    elif opcion ==6:
        print("")
        lista.sort
        print("")
    
    elif opcion ==7:
        salir = True
        
    else:
        print ("Introduce un numero entre 1 y 6")
 
print ("Fin")
