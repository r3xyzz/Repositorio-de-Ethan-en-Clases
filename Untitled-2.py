resp = "s"
cpriamria = 0

while(resp != "n"):
    print("Ingresando.....")
    primaria = input("Tiene estudios primarios: (S/N)")
    if (primaria == "s"):
        cpriamria = cpriamria + 1 #Contadores

    resp = input("Desea ingresar otra persona? (S/N)").lower()

print("Gracias por usar Sistema Censo Nacional")

