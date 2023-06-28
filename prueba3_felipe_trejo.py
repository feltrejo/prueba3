pacientes = []
sw = 1
def menu():
    print("¿Qué desea hacer?")
    print("(1) Grabar")
    print("(2) Buscar")
    print("(3) Imprimir Certificado de Vacunación")
    print("(4) Salir")

def grabar():
    rut = int(input("Ingrese RUT del paciente(SIN PUNTOS NI DIGITO VERIFICADOR): "))
    if rut < 10000000 or rut > 22000000:
        print("RUT incorrecto, intente nuevamente.")
    dv = input("Ingrese Digito Verificador: ")
    nombre = input("Ingrese nombre del paciente: ")
    lote = input("Ingrese lote de la vacuna administrada: ")
    fecha_vacunacion = input("Ingrese la fecha de vacunación: ")
    vacunatorio = input("Ingrese el lugar de vacunación: ")
    vacuna = input("Ingrese nombre de la vacuna administrada: ")

    paciente = {
        "rut": rut,
        "dv" : dv,
        "nombre" : nombre,
        "lote": lote,
        "fecha": fecha_vacunacion,
        "vacunatorio": vacunatorio,
        "vacuna": vacuna
    }
    pacientes.append(paciente)
    print("Se ha registrado el paciente.")

def buscar():
    rut = int(input("Ingrese el RUT del paciente(SIN PUNTOS NI DIGITO VERIFICADOR): "))
    for paciente in pacientes:
        if paciente["rut"] == rut:
            print("Información del paciente:")
            print("RUT:", paciente["rut"],"-",paciente["dv"])
            print("Nombre Paciente:", paciente["nombre"])
            print("Lote de vacuna:", paciente["lote"])
            print("Fecha de vacunación:", paciente["fecha"])
            print("Vacunatorio:", paciente["vacunatorio"])
            print("Vacuna administrada:", paciente["vacuna"])
            return
    
    print("Paciente no encontrado.")

def imprimir():
    rut = int(input("Ingrese el RUT del paciente(SIN PUNTOS NI DIGITO VERIFICADOR): "))
    
    for paciente in pacientes:
        if paciente["rut"] == rut:
            print("CERTIFICADO SANITARIO: Vacunación contra el COVID-19")
            print("RUT:", paciente["rut"],"-",paciente["dv"])
            print("Nombre Paciente:", paciente["nombre"])
            print("Fecha de vacunación:", paciente["fecha"])
            print("Vacunatorio:", paciente["vacunatorio"])
            print("Vacuna administrada:", paciente["vacuna"])
            return

def salir():
    print("Gracias por usar el programa de Felipe Trejo")
    print("Saliendo del programa...")
    
while sw == 1:
    menu()
    op = int(input("Eliga una opción: "))
    try:
        if op > 0 and op < 5:
            if op == 1:
                grabar()
            elif op == 2:
                buscar()
            elif op == 3:
                imprimir()
            elif op == 4:
                salir()
                sw = 0
    except:
        print("Selección Erronea")