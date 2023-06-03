resp = "s"
cprimaria = 0
csecundario = 0
ctecnico = 0
cprofesionales = 0
cpostgrado = 0
contadorPersonas = 0
operacion = 0

print("ingresando....")

while(resp != "n"):

    try:

    

      while operacion==0:

        primaria = str(input("Tiene estudios Primarios (S/N): ")).lower()

        if primaria != ("s" or "n"):

          raise TypeError

        if (primaria == "s"):

            cprimaria = cprimaria + 1 #contador 1

        operacion +=1

      while operacion==1:

        secundario = input("Tiene estudios Secundarios (S/N): ").lower()

        if secundario != ("s" or "n"):

          raise TypeError

        if (secundario == "s"):

            csecundario = csecundario + 1 #contador 2

        operacion +=1

      while operacion==2:

        tecnico = input("Tiene estudios Tecnicos (S/N): ").lower()

        if tecnico != ("s" or "n"):

          raise TypeError

        if (tecnico == "s"):

            ctecnico = ctecnico + 1 #contador 3

            operacion +=1

      while operacion==3:

        profesionales = input("Tiene estudios Profesionales (S/N): ").lower()

        if profesionales != ("s" or "n"):

          raise TypeError

        if (profesionales == "s"):

          cprofesionales = cprofesionales + 1 #contador 4

        operacion +=1

      while operacion==4:

        postgrado = input("Tiene estudios Posgrado (S/N): ").lower()

        if postgrado != ("s" or "n"):

          raise TypeError

        if (postgrado == "s"):

            cpostgrado = cpostgrado + 1 #contador 5

            operacion +=1

      while operacion==5:

        contadorPersonas = contadorPersonas + 1

        resp = input("desea ingresar otra persona ? (S/N): ").lower() #lower todo en minuscula

        if resp != ("s" or "n"):

            raise TypeError

        if resp == "s":

          operacion = 0

    except TypeError:

        print("solo (s/n)")

print()
print("-----------------------------------------------------")
print("Se entrevisto a :", contadorPersonas, "personas")
pPrimarios = (cprimaria*100)/contadorPersonas
psecundarios =(csecundario*100)/contadorPersonas
ptecnicos = (ctecnico*100)/contadorPersonas
pprofesionales = (cprofesionales*100)/contadorPersonas
ppostgrado = (cpostgrado*100)/contadorPersonas
print("Tiene estudios primarios: ", pPrimarios,"%" )
print("Tiene estudios secundarios: ", psecundarios,"%"  )
print("Tiene estudios tecnico: ", ptecnicos,"%"  )
print("Tiene estudios profecionales: ", pprofesionales,"%" )
print("Tiene estudios posgrado: ", ppostgrado,"%" )
print("-----------------------------------------------------")



'''

print("Tiene estudios primarios: ", cprimaria )

print("Tiene estudios secundarios: ", csecundario )

print("Tiene estudios tecnico: ", ctecnico )

print("Tiene estudios profecionales: ", cprofesionales)

print("Tiene estudios posgrado: ", cposgrado )

'''

print()
print("gracias por usar sistema censo nacional")