KiloNaranja = 250
totalTienda = 0

for i in range(15):  #Ciclo que se repetira 15 veces 
    while True:  #La condicion del while true en este caso es que se REPETIRA hasta que la condicion (for i in reange(15) se termine o se ingrese todos los datos solicitados
        try:  #Este try / exept solo te pedira que ingresen dato de forma numerica, si pones letras salta el mensaje del exept que es medio obio
            print("Ingrese Kg a comprar por Persona:",(i+1)) #Aca te pedira que ingreses el numero de kilos a comprar por persona hasta la persona nro 15, luego break que lo termina
            kilos = float(input()) #Pedir numeros de kilos, solo numeros (por el float)
            break
           
        except:  #Si en los datos se ingresan numeros te devolvera hasta que ingreses nuemero o en este caso los kilos
            print("Solo Ingrese numeros")
            
    #Y si eso se cumple saltara estos siguientes mensajes que seguira el codigo hasta la vez nro15 en este caso
    print("Usted compro", kilos, "Kg")
    precio = kilos * KiloNaranja
    print("Su total a pagar es de: $",'{:,}'.format(precio).replace(",","."))  #Ya aca es pura estetica para que se vea bonito, pero son el format o replace se ve bien o es entendible realmente
    totalTienda = totalTienda + precio      #Ya aca el total tienda se va hasta arriba que esta definida como = 0 ya que asi una vez ingresados los datos empieza de 0 y va en aumento y guardando los datos que le damos sobre los kilos que ingresamos
print("---------------------------------------")
print("El total vendido es de: $",'{:,}'.format(totalTienda).replace(",","."))
print("---------------------------------------")
