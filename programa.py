import utilidades
from utilidades import addcontrato, modifycontrato
import parametros
contratos=[]
seguir=True


menu=["elija una opcion",
    "1. ingresar contratos",
    "2. ver contratos",
    "3. salir"]
while seguir:
    try:
        print(menu)
        seleccion=int(input("seleccione uno: "))
        if seleccion==1:
            contratos.append(addcontrato(contratos))
            
        if seleccion==2:
            print(contratos)
        
            
            
    except:
        print("no selecciono ninguna opcion valida")