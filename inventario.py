import random
import datetime
import time
ncliente = 0
nbonos = 0
ntarjetas = 0
ingresado = 0
entregado = 0
bsfbonos = 0
tarjetamasvendida = [0,0]
cantidadbilletes = [[2,0],[5,0],[10,0],[20,0],[50,0],[100,0]]
cantidaddenominacion = [[15,0],[25,0],[40,0],[60,0],[120,0]]


#*********************************INVENTARIO***********************************#

def cantidad_tarjetas(denominacion):
    print("\nDenominacion de tarjetas:")
    print("a.- 15")
    print("b.- 25")
    print("c.- 40")
    print("d.- 60")
    print("e.- 120")
    card=input("Escoja denominacion de tarjeta")
    if(card=="a"):
        print("Hay %d tarjetas de 15 Bsf" % denominacion[0][1])
        print("1.- Agregar")
        print("2.- Eliminar")
        print("3.- Actualizar")
        opc = input("Escoja una opcion")
        if(opc=="1"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantas tarjetas desea agregar?"))
            denominacion[0][1]=denominacion[0][1]+cantidad
        elif(opc=="2"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantas tarjetas desea eliminar?"))
            denominacion[0][1]=denominacion[0][1]-cantidad
        elif(opc=="3"):
            cantidad=int(input("Indique la cantidad de tarjetas"))
            denominacion[0][1]=cantidad
    elif(card=="b"):
        print("Hay %d tarjetas de 25 Bsf" % denominacion[1][1])
        print("1.- Agregar")
        print("2.- Eliminar")
        print("3.- Actualizar")
        opc = input("Escoja una opcion")
        if(opc=="1"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantas tarjetas desea agregar?"))
            denominacion[1][1]=denominacion[1][1]+cantidad
        elif(opc=="2"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantas tarjetas desea eliminar?"))
            denominacion[1][1]=denominacion[1][1]-cantidad
        elif(opc=="3"):
            cantidad=int(input("Indique la cantidad de tarjetas"))
            denominacion[1][1]=cantidad
    elif(card=="c"):
        print("Hay %d tarjetas de 40 Bsf" % denominacion[2][1])
        print("1.- Agregar")
        print("2.- Eliminar")
        print("3.- Actualizar")
        opc = input("Escoja una opcion")
        if(opc=="1"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantas tarjetas desea agregar?"))
            denominacion[2][1]=denominacion[2][1]+cantidad
        elif(opc=="2"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantas tarjetas desea eliminar?"))
            denominacion[2][1]=denominacion[2][1]-cantidad
        elif(opc=="3"):
            cantidad=int(input("Indique la cantidad de tarjetas"))
            denominacion[2][1]=cantidad
    elif(card=="d"):
        print("Hay %d tarjetas de 60 Bsf" % denominacion[3][1])
        print("1.- Agregar")
        print("2.- Eliminar")
        print("3.- Actualizar")
        opc = input("Escoja una opcion")
        if(opc=="1"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantas tarjetas desea agregar?"))
            denominacion[3][1]=denominacion[3][1]+cantidad
        elif(opc=="2"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantas tarjetas desea eliminar?"))
            denominacion[3][1]=denominacion[3][1]-cantidad
        elif(opc=="3"):
            cantidad=int(input("Indique la cantidad de tarjetas"))
            denominacion[3][1]=cantidad
    elif(card=="e"):
        print("Hay %d tarjetas de 120 Bsf" % denominacion[4][1])
        print("1.- Agregar")
        print("2.- Eliminar")
        print("3.- Actualizar")
        opc = input("Escoja una opcion")
        if(opc=="1"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantas tarjetas desea agregar?"))
            denominacion[4][1]=denominacion[4][1]+cantidad
        elif(opc=="2"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantas tarjetas desea eliminar?"))
            denominacion[4][1]=denominacion[4][1]-cantidad
        elif(opc=="3"):
            cantidad=int(input("Indique la cantidad de tarjetas"))
            denominacion[4][1]=cantidad
    else:
        print("Error, intente de nuevo")

def cantidad_billetes(billetes):
    print("\nDenominacion de billetes:")
    print("a.- 2")
    print("b.- 5")
    print("c.- 10")
    print("d.- 20")
    print("e.- 50")
    print("f.- 100")
    money=input("Escoja denominacion de billete")
    if(money=="a"):
        print("Hay %d billetes de 2 Bsf" % billetes[0][1])
        print("1.- Agregar")
        print("2.- Eliminar")
        print("3.- Actualizar")
        opc = input("Escoja una opcion")
        if(opc=="1"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantos billetes desea agregar?"))
            billetes[0][1]=billetes[0][1]+cantidad
        elif(opc=="2"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantas billetes desea eliminar?"))
            billetes[0][1]=billetes[0][1]-cantidad
        elif(opc=="3"):
            cantidad=int(input("Indique la cantidad de billetes"))
            billetes[0][1]=cantidad
    elif(money=="b"):
        print("Hay %d billetes de 5 Bsf" % billetes[1][1])
        print("1.- Agregar")
        print("2.- Eliminar")
        print("3.- Actualizar")
        opc = input("Escoja una opcion")
        if(opc=="1"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantos billetes desea agregar?"))
            billetes[1][1]=billetes[1][1]+cantidad
        elif(opc=="2"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantas billetes desea eliminar?"))
            billetes[1][1]=billetes[1][1]-cantidad
        elif(opc=="3"):
            cantidad=int(input("Indique la cantidad de billetes"))
            billetes[1][1]=cantidad
    elif(money=="c"):
        print("Hay %d billetes de 10 Bsf" % billetes[2][1])
        print("1.- Agregar")
        print("2.- Eliminar")
        print("3.- Actualizar")
        opc = input("Escoja una opcion")
        if(opc=="1"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantos billetes desea agregar?"))
            billetes[2][1]=billetes[2][1]+cantidad
        elif(opc=="2"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantas billetes desea eliminar?"))
            billetes[2][1]=billetes[2][1]-cantidad
        elif(opc=="3"):
            cantidad=int(input("Indique la cantidad de billetes"))
            billetes[2][1]=cantidad
    elif(money=="d"):
        print("Hay %d billetes de 20 Bsf" % billetes[3][1])
        print("1.- Agregar")
        print("2.- Eliminar")
        print("3.- Actualizar")
        opc = input("Escoja una opcion")
        if(opc=="1"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantos billetes desea agregar?"))
            billetes[3][1]=billetes[3][1]+cantidad
        elif(opc=="2"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantas billetes desea eliminar?"))
            billetes[3][1]=billetes[3][1]-cantidad
        elif(opc=="3"):
            cantidad=int(input("Indique la cantidad de billetes"))
            billetes[3][1]=cantidad
    elif(money=="e"):
        print("Hay %d billetes de 50 Bsf" % billetes[4][1])
        print("1.- Agregar")
        print("2.- Eliminar")
        print("3.- Actualizar")
        opc = input("Escoja una opcion")
        if(opc=="1"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantos billetes desea agregar?"))
            billetes[4][1]=billetes[4][1]+cantidad
        elif(opc=="2"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantas billetes desea eliminar?"))
            billetes[4][1]=billetes[4][1]-cantidad
        elif(opc=="3"):
            cantidad=int(input("Indique la cantidad de billetes"))
            billetes[4][1]=cantidad
    elif(money=="f"):
        print("Hay %d billetes de 100 Bsf" % billetes[5][1])
        print("1.- Agregar")
        print("2.- Eliminar")
        print("3.- Actualizar")
        opc = input("Escoja una opcion")
        if(opc=="1"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantos billetes desea agregar?"))
            billetes[5][1]=billetes[5][1]+cantidad
        elif(opc=="2"):
            cantidad=int(input("ÃƒÆ’Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¿Cuantas billetes desea eliminar?"))
            billetes[5][1]=billetes[5][1]-cantidad
        elif(opc=="3"):
            cantidad=int(input("Indique la cantidad de billetes"))
            billetes[5][1]=cantidad
    else:
        print("Error, intente de nuevo")

def menu_inventario(billetes,denominacion):
    operacion=True
    contador=3
    while ((contador<=3)and(contador>0)and(operacion==True)):
        clave = input("Introduzca contrasena")
        if clave =="sergio":
            salir = False
            operacion = False
            while(salir==False):
                print("\n   Menu Actualizar")
                print("***************************")
                print("1.- Cantidad de tarjetas")
                print("2.- Cantidad de billetes")
                print("3.- Volver al menu anterior")
                pregunta = int(input("Escoja una opcion"))
                if(pregunta==1):
                    cantidad_tarjetas(denominacion)
                elif(pregunta==2):
                    cantidad_billetes(billetes)
                else:
                    salir=True
            i=0
            j=0
            file = open("inventario.out","w")
            while (i<5):
                file.write(str(denominacion[i][0])+" "+str(denominacion[i][1])+"\n")
                i=i+1
            while(j<6):
                file.write(str(billetes[j][0])+" "+str(billetes[j][1])+"\n")
                j=j+1
        else:
            contador=contador-1;
            if(contador>0):
                print("Tiene %d intentos" % contador)
                print("Intente de nuevo")
            else:
                print("Contrasena invalida")

#***********************************COMPRA*************************************#

def guardarestadistica():
    global ntarjetas
    global ingresado
    global entregado
    global bsfbonos
    global nbonos
    file = open("estadis.out","w")
    file.write("Cantidad de tarjetas vendidas: "+str(ntarjetas)+"\n")
    file.write("Monto total ingresado: "+str(ingresado)+"\n")
    file.write("Monto total entregado por concepto de vuelto: "+str(entregado)+"\n")
    file.write("Cantidad de billetes utilizados (ingreso+vuelto): \n")
    for i in range(6):
        file.write("Bsf."+str(cantidadbilletes[i][0])+"..........................................."+str(cantidadbilletes[i][1])+"\n")
    file.write("Tarjeta mas vendida: \n")
    file.write("Bsf."+str(tarjetamasvendida[0])+"..........................................."+str(tarjetamasvendida[1])+"\n")
    file.write("Cantidad clientes con bono: "+str(nbonos)+"\n")
    file.write("Monto total bonos (Bsf.): "+str(bsfbonos))
    file.close()

def estadisticas(recibido,vuelto,pago,clientebono,costo):
    global ntarjetas
    global ingresado
    global entregado
    global bsfbonos
    ntarjetas = ntarjetas + 1
    ingresado = ingresado + pago
    for i in range(6):
        cantidadbilletes[i][1]=cantidadbilletes[i][1]+recibido[i][1]+vuelto[i][1]
        if(vuelto[i][1]>0):
            entregado = entregado+(vuelto[i][0]*vuelto[i][1])
    for j in range(5):
        if(costo==cantidaddenominacion[j][0]):
            cantidaddenominacion[j][1]=cantidaddenominacion[j][1]+1
    for k in range(5):
        if(cantidaddenominacion[k][1]>tarjetamasvendida[1]):
            tarjetamasvendida[0] = cantidaddenominacion[k][0]
            tarjetamasvendida[1] = cantidaddenominacion[k][1]
    bsfbonos = bsfbonos + int(clientebono[2])


def elbono(clientebono,costo):
    global ncliente
    global nbonos
    n=random.randint(1,100)
    if((n<=25)and(nbonos<10)):
        nbonos=nbonos+1
        codigo=random.randint(1,9)
        for digitos in range(7):
            codigo=random.randint(0,9)+(codigo*10)
        clientebono[0]=str(ncliente)
        clientebono[1]=str(costo)
        clientebono[2]=str(int(costo*0.20))
        clientebono[3]=str(codigo)
        try:
            file=open("bonos.out","a")
            file.write(clientebono[0]+" "+clientebono[1]+" "+clientebono[2]+" "+clientebono[3]+"\n")
            file.close()
        except:
            print("No se pudo abrir bonos.out")
    else:
        clientebono=[0,0,0,0]

def recibo(costo,vuelto,pago,clientebono,total):
    global ncliente
    print("\nPor favor introduzca los siguientes datos para emitir la factura: ")
    nombre=input("nombre: ")
    cedula=input("Cedula: ")
    fecha = datetime.date.today()
    hora = time.strftime("%H:%M:%S")
    hoy = fecha.strftime("%d/%m/%Y")
    file = open("recibos.out","a")
    file.write("\nSeniat\n")
    file.write("RIF No J-00012005-8\n")
    file.write("TarIntel: TARJETAS INTELIGENTES, C.A.\n")
    file.write("Av. Universidad c/c Paseo Venezuela\n")
    file.write("CC La Granja, Urb. La Granja, Naguanagua\n")
    file.write("Edo Carabobo      0241-8675537\n")
    file.write("Recibo No "+str(ncliente)+"\n")
    file.write("Fecha: "+hoy+"   Hora: "+hora+"\n")
    file.write("Cliente: "+nombre+"\n")
    file.write("CI: "+cedula+"\n")
    file.write("---------------------------------------\n")
    file.write("Tarjeta................................Bsf. "+str(costo)+"\n")
    file.write("Efectivo...............................Bsf. "+str(pago)+"\n")
    file.write("---------------------------------------\n")
    file.write("Vuelto\n")
    for i in range(6):
        if(vuelto[i][1]>0):
            file.write("Bsf."+str(vuelto[i][0])+"..........................................."+str(vuelto[i][1])+"\n")
    file.write("Total..................................Bsf. "+str(total)+"\n")
    file.write("---------------------------------------\n")
    if(clientebono[0]==str(ncliente)):
        file.write("********** FELICIDADES **********\n")
        file.write("GANASTE UN BONO DE Bsf. "+clientebono[2]+"\n")
        file.write("CODIGO: "+clientebono[3]+"\n")
    file.write("\n///////////////////////////////\n")
    file.close()

def elvuelto(pago,costo,vuelto):
    resto=pago-costo
    sobra=resto
    while(resto>0):
        if(resto>=100):
            vuelto[5][1]=vuelto[5][1]+1
            resto=resto-100
        else:
            if(resto>=50):
                vuelto[4][1]=vuelto[4][1]+1
                resto=resto-50
            else:
                if(resto>=20):
                    vuelto[3][1]=vuelto[3][1]+1
                    resto=resto-20
                else:
                    if(resto>=10):
                        vuelto[2][1]=vuelto[2][1]+1
                        resto=resto-10
                    else:
                        if(resto>=5):
                            vuelto[1][1]=vuelto[1][1]+1
                            resto=resto-5
                        else:
                            if(resto>=2):
                                vuelto[0][1]=vuelto[0][1]+1
                                resto=resto-2
    return sobra

def ingreso_dinero(recibido):
    suma=0
    adicion=True
    print("\nDenominacion de billetes")
    print("-------------------------------")
    print("a.- 2")
    print("b.- 5")
    print("c.- 10")
    print("d.- 20")
    print("e.- 50")
    print("f.-100")
    print("g.- Listo")
    while(adicion==True):
        print("Saldo: %d Bsf" % suma)
        opcion=input("Ingrese un billete")
        if(opcion=="a"):
            suma=suma+recibido[0][0]
            recibido[0][1]=recibido[0][1]+1
        elif(opcion=="b"):
            suma=suma+recibido[1][0]
            recibido[1][1]=recibido[1][1]+1
        elif(opcion=="c"):
            suma=suma+recibido[2][0]
            recibido[2][1]=recibido[2][1]+1
        elif(opcion=="d"):
            suma=suma+recibido[3][0]
            recibido[3][1]=recibido[3][1]+1
        elif(opcion=="e"):
            suma=suma+recibido[4][0]
            recibido[4][1]=recibido[4][1]+1
        elif(opcion=="f"):
            suma=suma+recibido[5][0]
            recibido[5][1]=recibido[5][1]+1
        elif(opcion=="g"):
            adicion=False
            return suma
        else:
            break
            return 0

def transaccion(costo,billetes,denominacion):
    global ncliente
    recibido = [[2,0],[5,0],[10,0],[20,0],[50,0],[100,0]]
    vuelto=[[2,0],[5,0],[10,0],[20,0],[50,0],[100,0]]
    pago = ingreso_dinero(recibido)
    if(pago<costo):
        print("Insuficiente dinero")
        print("Tome su vuelto")
    else:
        clientebono=[0,0,0,0]       # Num cliente, denominacion tarjeta, Bsf premio, codigo
        ncliente=ncliente+1
        total=elvuelto(pago,costo,vuelto)
        elbono(clientebono,costo)
        for i in range(6):
            billetes[i][1]=billetes[i][1]+recibido[i][1]-vuelto[i][1]
        for filas in range(5):
            if(costo==denominacion[filas][0]):
                denominacion[filas][1]=denominacion[filas][1]-1
        recibo(costo,vuelto,pago,clientebono,total)
        estadisticas(recibido,vuelto,pago,clientebono,costo)

def comprar(billetes,denominacion):
    salir = False
    while(salir==False):
        print("\n       TarIntel")
        print("***************************")
        print("a.- 15")
        print("b.- 25")
        print("c.- 40")
        print("d.- 60")
        print("e.- 120")
        print("f.- Cancelar")
        tarjeta = input("Por favor escoja la tarjeta de su preferencia")
        if (tarjeta=="a"):
            if(denominacion[0][1]>0):
                salir = True
                transaccion(15,billetes,denominacion)
            else:
                print("\nLa tarjeta de Bsf. 15 esta agotada")
        elif(tarjeta=="b"):
            if(denominacion[1][1]>0):
                salir = True
                transaccion(25,billetes,denominacion)
            else:
                print("\nLa tarjeta de Bsf. 25 esta agotada")
        elif(tarjeta=="c"):
            if(denominacion[2][1]>0):
                salir = True
                transaccion(40,billetes,denominacion)
            else:
                print("\nLa tarjeta de Bsf. 40 esta agotada")
        elif(tarjeta=="d"):
            if(denominacion[3][1]>0):
                salir = True
                transaccion(60,billetes,denominacion)
            else:
                print("\nLa tarjeta de Bsf. 60 esta agotada")
        elif(tarjeta=="e"):
            if(denominacion[4][1]>0):
                salir = True
                transaccion(120,billetes,denominacion)
            else:
                print("\nLa tarjeta de Bsf. 120 esta agotada")
        elif(tarjeta=="f"):
            salir = True
        else:
            print("Incorrecto, vuelva a intentar")

#*****************************CARGA DE ARCHIVOS********************************#

def denom(denominacion):
    try:
        i=0
        j=0
        file = open("denomina.dat","r")
        dem = file.readline()
        while dem:
            denominacion[i][j]=int(dem[:len(dem)-1])
            if(i==4):
                i=-1
                j=1
            i=i+1
            dem = file.readline()
        file.close()
    except:
        print("No se pudo abrir denominaciones.dat")

def bille(billetes):
    try:
        i=0
        j=0
        file = open("billetes.dat","r")
        bill = file.readline()
        while bill:
            billetes[i][j]=int(bill[:len(bill)-1])
            if(i==5):
                i=-1
                j=1
            i=i+1
            bill = file.readline()
        file.close()
    except:
        print("No se pudo abrir billetes.dat")

#*****************************IMPRIMIR INVENTARIO******************************#

def mostrar(billetes,denominacion):
    print("[Billetes,Cantidad]")
    print(billetes)
    print("[Tarjetas,Cantidad]")
    print(denominacion)

#*******************************MENU PRINCIPAL*********************************#

def menu(billetes,denominacion):
    salir = False
    while(salir==False):
        print("\n           Menu")
        print("***************************")
        print("1.- Actualizar inventario")
        print("2.- Mostrar inventario")
        print("3.- Comprar tarjeta")
        print("4.- Salir")
        opcion = input("Seleccione una opcion")
        if(opcion=="1"):
            menu_inventario(billetes,denominacion)
        elif(opcion=="2"):
            mostrar(billetes,denominacion)
        elif(opcion=="3"):
            comprar(billetes,denominacion)
        else:
            salir = True

#*******************************FUNCION MAIN***********************************#

def main():
    denominacion = [[0,0],[0,0],[0,0],[0,0],[0,0]]      # declaracion de arreglo denominacion
    billetes = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]    # declaracion de arreglo billetes
    denom(denominacion)                                 # carga las denominaciones de denomina.dat
    bille(billetes)                                     # carga los billetes de billetes.dat
    menu(billetes,denominacion)
    guardarestadistica()
    pass
if __name__ == '__main__':
    main()