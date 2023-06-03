import os
persona =['1-7', 'Alan', 'Patricio','Brito' , 'Delgado']
grupo= [
    ['2-8', 'Maria', 'Antonia','Brito' , 'Delgado'],
    ['1-7', 'Alan', 'Patricio','Brito' , 'Delgado'],
    ['3-9', 'jose', 'francisco','Brito' , 'Martinez']]


for i in range (len(persona)):
    if i==1:
        print(persona[i])



def buscar_por_rut(rut_persona):
    for i in range (len(grupo)):
     for j in range (len(grupo[i])):
        if grupo[i][j] == rut_persona:
           return grupo[i]
print (buscar_por_rut('2-8'))

def imprimir_persona(array_persona):
   print(f"Rut: {array_persona[0]}")
   print(f"Primer nombre: {array_persona[1]}")
   print(f"Apellido paterno  {array_persona[2]}")
   print(f"Apellido materno {array_persona[3]}")
   input("")

imprimir_persona(buscar_por_rut('3-9'))

def agregar_persona():
   os.system("cls")
   print("*** agregar persona ***")
   rut= input("indique su rut > ")
   primer_nombre=input("indique su primer nombre > ")
   segundo_nombre=input("indique su segundo nombre > ")
   apellido_paterno=input("indique su primer apellido > ")
   apellido_materno=input("indique su segundo apellido > ")

   grupo.append([rut,primer_nombre,segundo_nombre,apellido_paterno,apellido_materno])

agregar_persona()
print (grupo)