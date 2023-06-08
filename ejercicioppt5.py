import os
piezas=['867961', '840369', '777876']
servidor=['Servidor Huaweii','Servidor Huaweii','Servidor HP' ]
nombre=['Next Generation 2','Generation One','Proliant Intel']
precio=['$80.000' , '$200.000', '$400.000']

def menu_general():
    os.system("cls")
    print("******* BIENVENIDO ******* ")
    print("1. Grabar")
    print("2. Buscar")
    print("3. Imprimir")
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


def menu_grabar():
    os.system("cls")
    print("*****Grabar*****")
    n_parte=input("Ingresa el numero de parte >  ")
    nom_producto=input ("Ingresa nombre del producto > ")
    precio_producto=input ("Ingresa precio del producto > ")
    piezas_grabadas.append(n_parte)
    nombre_grabado.append(nom_producto)
    precio_grabado.append(precio_producto)
    input("para volver al menu principal preciona cualquier tecla > ")


def menu_buscar():
    os.system("cls")
    print("**********BUSCAR**********")
    try:
        i=int(input("ingresa el codigo del producto > "))
        if i==867961:
            print(servidor[0], nombre [0] , precio [0])
        if i==840369:
            print(servidor[1], nombre [1] , precio [1])
        if i==777876:
            print(servidor[2], nombre [2] , precio [2])
        for i in [piezas_grabadas]:
            print (servidor[0], nombre_grabado [0] , precio_grabado [0])          
    except:
        os.system("cls")
        input("error en el menú general, presione una tecla para continuar > ")

    
def menu_imprimir():
    os.system("cls")
    print("1. 867961")
    print("2. 840369")
    print("3. 777876")
    try:
        opcion =int(input("Selecciona un modelo > "))
        if opcion==1:
            print("Pieza:         867961-B21")
            print("Servidor:      Huaweii")
            print("Nombre equipo: Next Generation 2")
            print("Valor:         $80.000 ")
        if opcion==2:
            print("Pieza:         840369-A21")
            print("Servidor:      Huaweii")
            print("Nombre equipo: Generation One")
            print("Valor:         $200.000")
        if opcion==3:
            print("Pieza:         777876-H55-H6")
            print("Servidor:      HP")
            print("Nombre equipo: Proliant Intel")
            print("Valor:         $400.000")
    except:
         os.system("cls")
         input("error en el menú general, presione una tecla para continuar > ")

def menu_salir():
    os.system("cls")
    print("*******SALISTE DEL SISTEMA******* ")
   
    input("presiona cualquier tecla para volver al menu principal > ")
    