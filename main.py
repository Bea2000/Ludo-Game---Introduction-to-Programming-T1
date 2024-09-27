def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo, "r")
    contenido = archivo.read().splitlines()
    archivo.close()
    return contenido

def escribir_archivo(nombre_archivo, contenido):
    archivo = open(nombre_archivo, "w")
    archivo.write(contenido)
    archivo.close()

contenido_final = ""
datos = leer_archivo("datos.txt")
linea = 0
casilleros_blancos= int(datos[linea])
linea = linea + 1
zona_de_victoria=casilleros_blancos+1
meta=casilleros_blancos+6
fichas_liberadas_1=0
fichas_liberadas_2=0
posicion_ficha_11=-1
posicion_ficha_12=-1
posicion_ficha_21=-1
posicion_ficha_22=-1
ganador=False
zonav11= False
zonav12=False
zonav21=False
zonav22=False

while((posicion_ficha_11<meta or posicion_ficha_12<meta)  and ganador==False):
    Turno=True
    contenido_final += "Ha iniciado el turno de J1\n"
    Dado= int(datos[linea])
    linea = linea + 1
    contenido_final += f"Dado: {Dado} \n"
    Respuesta= datos[linea]
    linea = linea + 1
    if(Dado==6 or Dado==1):
        while(Turno==True and (Dado==6 or Dado==1) and (posicion_ficha_11<meta or posicion_ficha_12<meta) and ganador==False):
            while(Respuesta=="Avanzar" and fichas_liberadas_1==0 and posicion_ficha_11<meta and posicion_ficha_12<meta and (Dado==6 or Dado==1)):
                contenido_final += "No hay fichas que avanzar\n"
                Respuesta= datos[linea]
                linea = linea + 1
            while(Respuesta=="Avanzar" and fichas_liberadas_1==1 and ganador==False and (Dado==6 or Dado==1) and Turno==True):
                    Dado_para_avanzar= int(datos[linea])
                    linea = linea + 1
                    if(Dado_para_avanzar==1 and posicion_ficha_11<meta):
                        posicion_ficha_11=posicion_ficha_11+Dado
                        if(posicion_ficha_11>=meta):
                            posicion_ficha_11=meta-(posicion_ficha_11-meta)
                        contenido_final += "La ficha 1, quedo en la posicion", posicion_ficha_11,"\n"
                        if(posicion_ficha_11>=zona_de_victoria and zonav11==False):
                            contenido_final += "La ficha 1, llego a la zona de victoria" + "\n"
                            zonav11=True
                        if(posicion_ficha_11==meta):
                            contenido_final += "La ficha 1, llego al casillero final" + "\n"
                        if(posicion_ficha_11<meta or posicion_ficha_12<meta):
                            Dado=int(datos[linea])
                            linea = linea + 1
                            contenido_final += f"Dado: {Dado} \n"
                            Respuesta= datos[linea]
                            linea = linea + 1
                        if(posicion_ficha_11==meta and posicion_ficha_12==meta):
                            ganador=True
                    elif(Dado_para_avanzar==2):
                        contenido_final += "Ficha 2 no es valida" + "\n"
                        Respuesta= datos[linea]
                        linea = linea + 1
                    else:
                        contenido_final += "Ficha", Dado_para_avanzar, "no es valida" + "\n"
                        Respuesta= datos[linea]
                        linea = linea + 1
            while(Respuesta=="Avanzar" and fichas_liberadas_1==2 and (posicion_ficha_11<meta or posicion_ficha_12<meta) and ganador==False and (Dado==6 or Dado==1)):
                Dado_para_avanzar=int(datos[linea])
                linea = linea + 1
                if(Dado_para_avanzar==1 and posicion_ficha_11<meta):
                    posicion_ficha_11=posicion_ficha_11+Dado
                    if(posicion_ficha_11>=meta):
                        posicion_ficha_11=meta-(posicion_ficha_11-meta)
                    contenido_final += "La ficha 1, quedo en la posicion", posicion_ficha_11 + "\n"
                    if(posicion_ficha_11>=zona_de_victoria and zonav11==False):
                        contenido_final += "La ficha 1, llego a la zona de victoria" + "\n"
                        zonav11=True
                    if(posicion_ficha_11==meta):
                        contenido_final += "La ficha 1, llego al casillero final" + "\n"
                    if(posicion_ficha_11<meta or posicion_ficha_12<meta):
                        Dado=int(datos[linea])
                        linea = linea + 1
                        contenido_final += f"Dado: {Dado} \n"
                        Respuesta= str(datos[linea])
                        linea = linea + 1
                    if(posicion_ficha_11==meta and posicion_ficha_12==meta):
                        ganador=True
                elif(Dado_para_avanzar==2 and posicion_ficha_12<meta):
                    posicion_ficha_12=posicion_ficha_12+Dado
                    if(posicion_ficha_12>=meta):
                        posicion_ficha_12=meta-(posicion_ficha_12-meta)
                    contenido_final += f"La ficha 2, quedo en la posicion {posicion_ficha_12}" + "\n"
                    if(posicion_ficha_12>=zona_de_victoria and zonav12==False):
                        contenido_final += "La ficha 2, llego a la zona de victoria" + "\n"
                        zonav12=True
                    if(posicion_ficha_12==meta):
                        contenido_final += "La ficha 2, llego al casillero final" + "\n"
                    if(posicion_ficha_11<meta or posicion_ficha_12<meta):
                        Dado=int(datos[linea])
                        linea = linea + 1
                        contenido_final += f"Dado: {Dado} \n"
                        Respuesta= str(datos[linea])
                        linea = linea + 1
                    if(posicion_ficha_11==meta and posicion_ficha_12==meta):
                        ganador=True
                else:
                    contenido_final += f"Ficha {Dado_para_avanzar} no es valida" + "\n"
                    Respuesta= str(datos[linea])
                    linea = linea + 1
            while(Respuesta=="Liberar" and fichas_liberadas_1==0 and (posicion_ficha_11<meta or posicion_ficha_12<meta) and ganador==False and (Dado==6 or Dado==1)):
                contenido_final += "El Jugador ha liberado una ficha" + "\n"
                fichas_liberadas_1=1
                posicion_ficha_11=0
                Dado=int(datos[linea])
                linea = linea + 1
                contenido_final += f"Dado: {Dado} \n"
                Respuesta= str(datos[linea])
                linea = linea + 1
            while(Respuesta=="Liberar" and fichas_liberadas_1==1 and (posicion_ficha_11<meta or posicion_ficha_12<meta) and ganador==False and (Dado==6 or Dado==1)):
                contenido_final += "El Jugador ha liberado una ficha" + "\n"
                fichas_liberadas_1=2
                posicion_ficha_12=0
                Dado=int(datos[linea])
                linea = linea + 1
                contenido_final += f"Dado: {Dado} \n"
                Respuesta= str(datos[linea])
                linea = linea + 1
            while(Respuesta=="Liberar" and fichas_liberadas_1==2 and (posicion_ficha_11<meta or posicion_ficha_12<meta) and ganador==False and (Dado==6 or Dado==1)):
                contenido_final += "No quedan fichas por liberar" + "\n"
                Respuesta=str(datos[linea])
                linea = linea + 1
    while(Turno==True and (Dado!=6 and Dado!=1) and (posicion_ficha_11<meta or posicion_ficha_12<meta) and ganador==False):
        if(Respuesta=="Avanzar" and fichas_liberadas_1==0):
            Turno=False
        while(Respuesta=="Avanzar" and fichas_liberadas_1==1 and Turno==True and ganador==False):
            if(posicion_ficha_12==-1 and posicion_ficha_11==meta):
                Turno=False
            if(Turno==True):
                Dado_para_avanzar=int(datos[linea])
                linea = linea + 1
                if(Dado_para_avanzar==1 and posicion_ficha_11<meta):
                    posicion_ficha_11=posicion_ficha_11+Dado
                    if(posicion_ficha_11>=meta):
                        posicion_ficha_11=meta-(posicion_ficha_11-meta)
                    contenido_final += f"La ficha 1, quedo en la posicion {posicion_ficha_11}" + "\n"
                    if(posicion_ficha_11>=zona_de_victoria and zonav11==False):
                        contenido_final += "La ficha 1, llego a la zona de victoria" + "\n"
                        zonav11=True
                    if(posicion_ficha_11==meta):
                        contenido_final += "La ficha 1, llego al casillero final" + "\n"
                        Turno=False
                    if(posicion_ficha_11==meta and posicion_ficha_12==meta):
                        ganador=True
                    if(posicion_ficha_11<=meta):
                        Turno=False
                elif(Dado_para_avanzar==2):
                    contenido_final += "Ficha 2 no es valida" + "\n"
                    Turno=True
                else:
                    contenido_final += "Ficha" ,Dado_para_avanzar, "no es valida" + "\n"
                    Turno=True
                if(posicion_ficha_11==meta):
                    Turno=False
        while(Respuesta=="Avanzar" and fichas_liberadas_1==2 and Turno==True and ganador==False and (posicion_ficha_11<meta or posicion_ficha_12<meta)):
            Dado_para_avanzar=int(datos[linea])
            linea = linea + 1
            if(Dado_para_avanzar==1 and posicion_ficha_11<meta):
                posicion_ficha_11=posicion_ficha_11+Dado
                if(posicion_ficha_11>=meta):
                    posicion_ficha_11=meta-(posicion_ficha_11-meta)
                contenido_final += f"La ficha 1, quedo en la posicion {posicion_ficha_11}" + "\n"
                if(posicion_ficha_11>=zona_de_victoria and zonav11==False):
                    contenido_final += "La ficha 1, llego a la zona de victoria" + "\n"
                    zonav11=True
                if(posicion_ficha_11==meta):
                    contenido_final += "La ficha 1, llego al casillero final" + "\n"
                Turno=False
                if(posicion_ficha_11==meta and posicion_ficha_12==meta):
                    ganador=True
            elif(Dado_para_avanzar==2 and posicion_ficha_12<meta):
                posicion_ficha_12=posicion_ficha_12+Dado
                if(posicion_ficha_12>=meta):
                    posicion_ficha_12=meta-(posicion_ficha_12-meta)
                contenido_final += f"La ficha 2, quedo en la posicion {posicion_ficha_12}" + "\n"
                if(posicion_ficha_12>=zona_de_victoria and zonav12==False):
                    contenido_final += "La ficha 2, llego a la zona de victoria" + "\n"
                    zonav12=True
                if(posicion_ficha_12==meta):
                    contenido_final += "La ficha 2, llego al casillero final" + "\n"
                Turno=False
                if(posicion_ficha_11==meta and posicion_ficha_12==meta):
                    ganador=True
            else:
                contenido_final += f"Ficha {Dado_para_avanzar} no es valida" + "\n"
    if((posicion_ficha_21<meta or posicion_ficha_22<meta) and ganador==False):
        Turno=True
        contenido_final += "Ha iniciado el turno de J2" + "\n"
        Dado=int(datos[linea])
        linea = linea + 1
        contenido_final += f"Dado: {Dado} \n"
        Respuesta= str(datos[linea])
        linea = linea + 1
        if(Dado==6 or Dado==1):
            while(Turno==True and (Dado==6 or Dado==1) and (posicion_ficha_21<meta or posicion_ficha_22<meta and ganador==False)):
                while(Respuesta=="Avanzar" and fichas_liberadas_2==0 and (posicion_ficha_21<meta or posicion_ficha_22<meta) and ganador==False and (Dado==6 or Dado==1)):
                    contenido_final += "No hay fichas que avanzar" + "\n"
                    Respuesta= str(datos[linea])
                    linea = linea + 1
                while(Respuesta=="Avanzar" and fichas_liberadas_2==1 and ganador==False and (Dado==6 or Dado==1)):
                        Dado_para_avanzar=int(datos[linea])
                        linea = linea + 1
                        if(Dado_para_avanzar==1 and posicion_ficha_21<meta):
                            posicion_ficha_21=posicion_ficha_21+Dado
                            if(posicion_ficha_21>=meta):
                                posicion_ficha_21=meta-(posicion_ficha_21-meta)
                            contenido_final += "La ficha 1, quedo en la posicion", posicion_ficha_21 + "\n"
                            if(posicion_ficha_21>=zona_de_victoria and zonav21==False):
                                contenido_final += "La ficha 1, llego a la zona de victoria" + "\n"
                                zonav21=True
                            if(posicion_ficha_21==meta):
                                contenido_final += "La ficha 1, llego al casillero final" + "\n"
                            if(posicion_ficha_21<meta or posicion_ficha_22<meta):
                                Dado=int(datos[linea])
                                linea = linea + 1
                                contenido_final += f"Dado: {Dado} \n"
                                Respuesta= str(datos[linea])
                                linea = linea + 1
                            if(posicion_ficha_21==meta and posicion_ficha_22==meta):
                                ganador=True
                        elif(Dado_para_avanzar==2):
                            contenido_final += "Ficha 2 no es valida" + "\n"
                            Respuesta= str(datos[linea])
                            linea = linea + 1
                        else:
                            contenido_final += "Ficha", Dado_para_avanzar, "no es valida" + "\n"
                            Respuesta= str(datos[linea])
                            linea = linea + 1
                while(Respuesta=="Avanzar" and fichas_liberadas_2==2 and (Dado==6 or Dado==1) and (posicion_ficha_21<meta or posicion_ficha_22<meta and ganador==False)):
                    Dado_para_avanzar=int(datos[linea])
                    linea = linea + 1
                    if(Dado_para_avanzar==1 and posicion_ficha_21<meta):
                        posicion_ficha_21=posicion_ficha_21+Dado
                        if(posicion_ficha_21>=meta):
                            posicion_ficha_21=meta-(posicion_ficha_21-meta)
                        contenido_final += f"La ficha 1, quedo en la posicion {posicion_ficha_21}" + "\n"
                        if(posicion_ficha_21>=zona_de_victoria and zonav21==False):
                            contenido_final += "La ficha 1, llego a la zona de victoria" + "\n"
                            zonav21=True
                        if(posicion_ficha_21==meta):
                            contenido_final += "La ficha 1, llego al casillero final" + "\n"
                        if(posicion_ficha_21<meta or posicion_ficha_22<meta):
                            Dado=int(datos[linea])
                            linea = linea + 1
                            contenido_final += f"Dado: {Dado} \n"
                            Respuesta= str(datos[linea])
                            linea = linea + 1
                        if(posicion_ficha_21==meta and posicion_ficha_22==meta):
                            ganador=True
                    elif(Dado_para_avanzar==2 and posicion_ficha_22<meta):
                        posicion_ficha_22=posicion_ficha_22+Dado
                        if(posicion_ficha_22>=meta):
                            posicion_ficha_22=meta-(posicion_ficha_22-meta)
                        contenido_final += f"La ficha 2, quedo en la posicion {posicion_ficha_22}" + "\n"
                        if(posicion_ficha_22>=zona_de_victoria and zonav22==False):
                            contenido_final += "La ficha 2, llego a la zona de victoria" + "\n"
                            zonav22=True
                        if(posicion_ficha_22==meta):
                            contenido_final += "La ficha 2, llego al casillero final" + "\n"
                        if(posicion_ficha_21<meta or posicion_ficha_22<meta):
                            Dado=int(datos[linea])
                            linea = linea + 1
                            contenido_final += f"Dado: {Dado} \n"
                            Respuesta= str(datos[linea])
                            linea = linea + 1
                        if(posicion_ficha_21==meta and posicion_ficha_22==meta):
                            ganador=True
                    else:
                        contenido_final += f"Ficha {Dado_para_avanzar} no es valida" + "\n"
                        Respuesta= str(datos[linea])
                        linea = linea + 1
                while(Respuesta=="Liberar" and (Dado==6 or Dado==1) and fichas_liberadas_2==0 and (posicion_ficha_21<meta or posicion_ficha_22<meta) and ganador==False):
                    contenido_final += "El Jugador ha liberado una ficha" + "\n"
                    fichas_liberadas_2=1
                    posicion_ficha_21=0
                    Dado=int(datos[linea])
                    linea = linea + 1
                    contenido_final += f"Dado: {Dado} \n"
                    Respuesta= str(datos[linea])
                    linea = linea + 1
                while(Respuesta=="Liberar" and (Dado==6 or Dado==1) and fichas_liberadas_2==1 and (posicion_ficha_21<meta or posicion_ficha_22<meta) and ganador==False):
                    contenido_final += "El Jugador ha liberado una ficha" + "\n"
                    fichas_liberadas_2=2
                    posicion_ficha_22=0
                    Dado=int(datos[linea])
                    linea = linea + 1
                    contenido_final += f"Dado: {Dado} \n"
                    Respuesta= str(datos[linea])
                    linea = linea + 1
                while(Respuesta=="Liberar" and (Dado==6 or Dado==1) and fichas_liberadas_2==2 and (posicion_ficha_21<meta or posicion_ficha_22<meta) and ganador==False):
                    contenido_final += "No quedan fichas por liberar" + "\n"
                    Respuesta=str(datos[linea])
                    linea = linea + 1
        while(Turno==True and (Dado!=6 and Dado!=1) and (posicion_ficha_21<meta or posicion_ficha_22<meta) and ganador==False):
            if(Respuesta=="Avanzar" and fichas_liberadas_2==0):
                Turno=False
            while(Respuesta=="Avanzar" and fichas_liberadas_2==1 and Turno==True and ganador==False):
                if(posicion_ficha_22==-1 and posicion_ficha_21==meta):
                    Turno=False
                if(Turno==True):
                    Dado_para_avanzar=int(datos[linea])
                    linea = linea + 1
                    if(posicion_ficha_21<meta):
                        if(Dado_para_avanzar==1 and posicion_ficha_21<meta):
                            posicion_ficha_21=posicion_ficha_21+Dado
                            if(posicion_ficha_21>=meta):
                                posicion_ficha_21=meta-(posicion_ficha_21-meta)
                            contenido_final += f"La ficha 1, quedo en la posicion {posicion_ficha_21}" + "\n"
                            if(posicion_ficha_21>=zona_de_victoria and zonav21==False):
                                contenido_final += "La ficha 1, llego a la zona de victoria" + "\n"
                                zonav21=True
                            if(posicion_ficha_21==meta):
                                contenido_final += "La ficha 1, llego al casillero final" + "\n"
                                Turno=False
                            if(posicion_ficha_21==meta and posicion_ficha_22==meta):
                                ganador=True
                            if(posicion_ficha_21<=meta):
                                Turno=False
                        elif(Dado_para_avanzar==2):
                            contenido_final += "Ficha 2 no es valida" + "\n"
                            Turno=True
                        else:
                            contenido_final += "Ficha", Dado_para_avanzar, "no es valida" + "\n"
                            Turno=True
            while(Respuesta=="Avanzar" and fichas_liberadas_2==2 and Turno==True and ganador==False and (posicion_ficha_21<meta or posicion_ficha_22<meta)):
                Dado_para_avanzar=int(datos[linea])
                linea = linea + 1
                if(Dado_para_avanzar==1 and posicion_ficha_21<meta):
                    posicion_ficha_21=posicion_ficha_21+Dado
                    if(posicion_ficha_21>=meta):
                        posicion_ficha_21=meta-(posicion_ficha_21-meta)
                    contenido_final += f"La ficha 1, quedo en la posicion {posicion_ficha_21}" + "\n"
                    Turno=False
                    if(posicion_ficha_21>=zona_de_victoria and zonav21==False):
                        contenido_final += "La ficha 1, llego a la zona de victoria" + "\n"
                        zonav21=True
                        Turno=False
                    if(posicion_ficha_21==meta):
                        contenido_final += "La ficha 1, llego al casillero final" + "\n"
                        if(posicion_ficha_21==meta and posicion_ficha_22==meta):
                            ganador=True
                elif(Dado_para_avanzar==2 and posicion_ficha_22<meta):
                    posicion_ficha_22=posicion_ficha_22+Dado
                    if(posicion_ficha_22>=meta):
                        posicion_ficha_22=meta-(posicion_ficha_22-meta)
                    contenido_final += f"La ficha 2, quedo en la posicion {posicion_ficha_22}" + "\n"
                    Turno=False
                    if(posicion_ficha_22>=zona_de_victoria and zonav22==False):
                        contenido_final += "La ficha 2, llego a la zona de victoria" + "\n"
                        zonav22=True
                    if(posicion_ficha_22==meta):
                        contenido_final += "La ficha 2, llego al casillero final" + "\n"
                        Turno=False
                    if(posicion_ficha_21==meta and posicion_ficha_22==meta):
                        ganador=True
                else:
                    contenido_final += f"Ficha {Dado_para_avanzar} no es valida" + "\n"
if(posicion_ficha_11==meta and posicion_ficha_12==meta):
    ganador=True
    contenido_final += "Resumen Ludo" + "\n"
    contenido_final += "Ganador: J1" + "\n"
    contenido_final += f"Cantidad fichas liberadas J2: {fichas_liberadas_2}" + "\n"
    contenido_final += f"Posicion ficha 1: {posicion_ficha_21}" + "\n"
    contenido_final += f"Posicion ficha 2: {posicion_ficha_22}" + "\n"

if(posicion_ficha_21==meta and posicion_ficha_22==meta):
    ganador=True
    contenido_final += "Resumen Ludo" + "\n"
    contenido_final += "Ganador: J2" + "\n"
    contenido_final += f"Cantidad fichas liberadas J1: {fichas_liberadas_1}" + "\n"
    contenido_final += f"Posicion ficha 1: {posicion_ficha_11}" + "\n"
    contenido_final += f"Posicion ficha 2: {posicion_ficha_12}" + "\n"
    
escribir_archivo("output.txt", contenido_final)