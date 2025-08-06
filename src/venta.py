N = 1
ventas=[]
while N==1:
    
    print("Opciones:")
    print("1. Crear nueva venta")    
    print("2. Listar ventas")
    print("3. Busqueda por ID")
    print("4. Modificar una lista")
    print ("5. Eliminar una lista")
    print("6. Para salir")
    Op = int(input())
    while Op>6 or Op<1:
        print("por favor ingrese una opcion valida")
        Op = int(input())
    if Op==1: 
  #Crear venta  
     print("Digite el ID")
     id = int(input())
     print("Digite el producto")
     p = input()
     print("Digite la cantidad")
     c = int(input())
     print("Digite el precio del producto")
     pu = float(input())
     venta = [id,p,c,pu]
     ventas.append(venta)
     print(venta)
     print("Los ingresos totales de estas ventas son: ",(pu*c))
    elif Op==2:
      print(ventas)

       
    elif Op==3:
     #Busqueda por id   
       print("Digite el ID del producto deseado:")
       for venta in ventas:
         bsq=int(input())
         if bsq==venta[0] in ventas:
          print(venta)
         else:
          print("No se encuentra un producto con el ID ingresado") 

    elif Op==4:
     #Modificar 
       print("Que elemento desea modificar:")
       print("1. ID")
       print("2. Producto")
       print("3. Cantidad")
       print("4. Precio Unitario")
       md = int(input())
       while md>5 or md<1:
        print("por favor ingrese una opcion valida")
        md = int(input())
       if md==1:
         id= int(input())
       elif md==2:
          p =input()
       elif md==3:
          c= int(input())
       else: pu=float(input) 
       print(venta)    

       
    elif Op==6:
   #Salir    
       N = 2
       print("Hasta la proxima")
       print(ventas)
