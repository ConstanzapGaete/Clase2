
import os

def menu_general():
    os.system("cls")
    print("******* MENU ******* ")
    print("1. Platos")
    print("2. Bebidas")
    print("3. Imprimir boleta")
    print("4. Salir")
    try:
        opcion = int(input("Ingrese una de las opciones > "))
        if opcion > 0 and opcion < 5:
            return opcion
        else:
            os.system("cls")
            input("opción no válida, presione una tecla para continuar > ")
    except:
        os.system("cls")
        input("error en el menú general, presione una tecla para continuar > ")


def menu_platos():
    os.system("cls")
    print("****** MENU PLATOS ******")
    print("1. Curanto \t\t $20.000")
    print("2. Centolla \t\t $15.000")
    print("3. Mariscal \t\t $10.000")
    print("4. Empanadas \t\t $ 2.000")
    print("5. Volver al menú anterior")
    try:
        opcion = int(input("Ingrese una de las opciones > "))
        if opcion > 0 and opcion < 6:
            return opcion
        else:
            os.system("cls")
            input("opción no válida, presione una tecla para continuar > ")
    except:
        os.system("cls")
        input("error en el menú platos, presione una tecla para continuar > ")

def menu_bebidas():
    os.system("cls")
    print("****** MENU BEBIDAS ******")
    print("1. Bebida en lata \t\t $1.500")
    print("2. Limonada     \t\t $2.500")
    print("3. Jugo Natural  \t\t $3.000")
    print("4. Volver al menú anterior")
    try:
        opcion =int(input("Ingresa una opcion  > "))
        if opcion > 0 and opcion < 5:
            return opcion
        else:
            os.system("cls")
            input("opcion no valida , presiona una tecla para continuar")
    except:
        os.system("cls")
        input("Error en menu bebidas , presiona una tecla para continuar")
    


def imprimir_boleta():
    os.system("cls")
    print("****** BOLETA ******")
    if curanto > 0:
        print(f"{curanto} Curanto \t\t ${curanto*20000}")
    if centolla > 0:
        print(f"{centolla} Centolla \t\t ${centolla*15000}")
    if mariscal > 0:   
        print(f"{mariscal} Mariscal \t\t ${mariscal*10000}")
    if empanadas > 0:
        print(f"{empanadas} Empanadas \t\t ${empanadas*2000}")
    if bebida>0:
        print(f"{bebida} Bebida \t\t ${bebida*1500}")
    if limonada>0:
        print(f"{limonada} Limonada \t\t ${limonada*2500}")
    if jugo>0:
        print(f"{jugo} Jugo Natural \t\t ${jugo*3000}")
    print(f"----------")
    input("\n presione una tecla para continuar > ")


# acumuladores
curanto = 0
centolla = 0
mariscal = 0
empanadas = 0
bebida=0
limonada=0
jugo=0



menu = True
while menu:
    opcion_general = menu_general()
    if opcion_general == 1:
        menup = True
        while menup:
            opcion_platos = menu_platos()
            if opcion_platos == 1:
                curanto += int(input("Ingrese la cantidad que desea comprar > "))
            if opcion_platos == 2:
                centolla += int(input("Ingrese la cantidad que desea comprar > "))
            if opcion_platos == 3:
                mariscal += int(input("Ingrese la cantidad que desea comprar > "))
            if opcion_platos == 4:
                empanadas += int(input("Ingrese la cantidad que desea comprar > "))
            if opcion_platos == 5:
                menup = False
    if opcion_general == 2:
        menub=True
        while menub:
            opcion_bebidas=menu_bebidas()
            if opcion_bebidas==1:
                bebida +=int(input("Ingrese la cantidad que desea comprar > "))
            if opcion_bebidas==2:
                limonada +=int(input("Ingrese la cantidad que desea comprar > ")) 
            if opcion_bebidas==3:
                jugo += int(input("Ingrese la cantidad que desea comprar > "))
            if opcion_bebidas==4:
                menub=False    
    if opcion_general == 3:
        imprimir_boleta()