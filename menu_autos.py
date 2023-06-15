import os

def menu_general():
    print("*****AUTO SEGURO*****")
    print("1- Grabar")
    print("2- Buscar")
    print("3- Imprimir")
    print("4- Salir")
    opcion=validar_opcion(5)
    return opcion


def validar_opcion(fin):
    try:
        opcion=int(input("Ingrese una de las opciones indicadas"))
        if opcion>0 and opcion<fin:
            return opcion
        else:
            input("opcion no valida presiona cualquier tecla para continuar")
    except:
        input("opcion no valida presiona cualquier tecla para continuar")

def guardar_vehiculo():
    os.system("cls")
    print("Favor ingrese los datos acontinuacion")
    tipo= input("tipo vehiculo > ")
    patente=validar_patente()
    marca=validar_marca()
    precio=validar_precio()
    multas=input("Multas > ")
    fecha_registro=input("Fecha de registro   > ")
    nombre_dueno=input("Nombre dueño   >")
    vehiculos_registrados.append[tipo,patente,marca,precio,multas,fecha_registro,nombre_dueno]
    
vehiculos_registrados=[]
def registrar_multas():
    validar=True
    multas=[]
    while validar:
        try:
            opcion=int(input("Tiene multas ? 1> SI     2>NO"))
            if opcion==1:
                cantidad=int(input("Cuantas multas tienes?"))
                for i in range (cantidad):
                    monto_multa=int(input(f"Monto multa : {i+1}"))
                    fecha_multa=input(f"Fecha de la multa : {i+1}")
                    multas.append([monto_multa, fecha_multa])
                validar=False
            elif opcion==2:
                 validar=False
        except:
            input("Error en valor ingresado")
    return multas


def validar_patente():
    validar=True
    while validar:
        patente=input("Patente > ")
        if len(patente)==6:
         validar=False
    else:
        input("Patente no valida ingresa nuevamente ")
    return patente


def validar_marca():
    validar=True
    while validar:
        marca=input("Marca  > ")
        if len(marca)>1 and len(marca)<16:
            validar=False
        else:
            input("La marca no corresponde ")
    return marca

def validar_precio():
    validar=True
    while validar:
        try:
            precio=int(input("precio > "))
            if precio >5000000:
                    validar=False
            else:
                    input("El precio no corresponde ")
        except:
            input("Valor no valido")
    return precio






menu_g= True
while menu_g:
    opcion_g= menu_general()
    if opcion_g==1:
        guardar_vehiculo()
    elif opcion_g==2:
        input("opcion 2")
    elif opcion_g==3:
        input("opcion 3")
    elif opcion_g==4:
        input("opcion 4")
