import datetime
def datoscliente(cliente):
    """"" la usaba dentro de addcontrato pero no funcionaba y
    si use el return cliente para mandar
    el diccionario del cliente"""
    pass

def addcontrato(contrato):
    contrato={}
    estado={}
    empleado=input("ingrese nombre del empleado \n")
    aseado=(input("ingrese el dato en metros de lo que aseo\n"))
    price=(input("ingrese el precio: \n"))
    cliente={}
    print("ingrese los datos del cliente que se piden")
    nombre=input("Nombre del cliente: \n")
    identidad=input("numero de identidad del cliente: \n")
    cliente["datos cliente"]=nombre,identidad
    contrato["empleado"]=empleado
    contrato["metros aseados"]=aseado
    contrato["precio cobrado"]=price
    contrato["datos del cliente"]=cliente

    print("cual es el estado del contrato, seleccione una opcion: ")
    print("1. En espera  2. En proceso  3.Finalizado")
    conestado=int(input("seleccione una opcion:\n"))
    try:
        if conestado== 1:
            estado["en espera"]=contrato
        elif conestado==2:
            estado["en proceso"]=contrato
        elif conestado==3:
            estado["finalizado"]=contrato
    except:
        print=("no selecciono una opcion valida")
    return estado

def modifycontrato(contrato, posicion):
    
    pass
