# Se importa la librería que permite pausar la ejecución por determinado tiempo
# Inteligencia Artificial
# Anthony Mauricio Goyes Díaz

import time
# Agente de dispensador de jabon

# Se define las localización: 
# Escenario propuesto: Una casa.
#Localizaciones (deben ser 3): baño, cocina, sala de estar, 
# donde baño estará identifcado como casa_banio, cocina por
# casa_cocina y la sala de estar por casa_salaEstar.

# Estados posibles:
# Si es igual a 1 está sucio. Por otro lado, si es igual a 0 está limpio.

def dispensadorJabon():
    #Se renombra las variables de localizaciones para facilidad de manejo.
    # Donde "L" represanta a la localización y el número a la posición de la localización.
    # L1 = 'casa_banio'
    # L2 = 'casa_cocina'
    # L3 = 'casa_salaEstar'

    # El estado objetivo es el que se espera llegar. Todas las habitaciones
    # deben dispensar el jabon si su mano está sucia. Si eso se cumple
    # se consigue el estado objetivo. Es decir, ninguna localización tiene 
    # manos sucias a las cuales dispensar jabón. 
    estado_objetivo = {'L1':'0','L2':'0','L3':'0'}

    # Se inicializa la variable "esfuerzo" que hará referencia al esfuerzo requerido
    # para realizar una acción
    esfuerzo = 0

    respuesta_localizacion = ''

    # Se genera un menú que se repetirá hasta que ingrese una de las opciones propuestas o
    # por el contrario, finalice el programa con la cuarta opción
    # Se le instruirá al usuario a que corresponde cada opción
    # Do while que ejecutará su bloque de código simepre que sea difirente de "Salir"
    while(respuesta_localizacion != 'Salir' ):
        print('---Agente Dispensador de jabón---')
        print('---------------Menú--------------')
        print('(Se debe ingresar la cadena de texto entre comillas, ejemplo: Salir)')
        print('1: "L1" = baño')
        print('2: "L2" = cocina')
        print('3: "L3" = sala de estar')
        print('4: "Salir"')
        # Se captura la información del usuario con respecto a la localización
        respuesta_localizacion = input('Ingrese la localización actual: ')
        # Se genera un switch en python mediante if anidados
        # Se evalúa a que localización corresponde la opción ingresada
        # Si la localización ingresada es igual "L1" <=> baño, entonces
        if(respuesta_localizacion == 'L1'):
            # Se genera un do while
            while(True):
                # Se captura la información del usuario con respecto al estado de la localización
                estado_valor = input('¿La persona en la habitación '+respuesta_localizacion+' tiene las manos sucias?  (1:Si; 0:No) ')
                # Se evalúa el estado si genera esfuerzo se cambia el estado objetivo de sucio a limpio
                # Si el estado es igual a "1" <=> sucio, entonces
                if(estado_valor == '1'):
                    # Se imprime un mensaje de una acción para limpiar las  manos
                    print('Manos sucias. Dispensando jabón...')
                    # Aumenta el esfuerzo en una unidad por el esfuerzo requerido 
                    esfuerzo +=1
                    # Se actualiza el estado de la localización uno (L1) de "1" (sucio) a 0 (limpio)
                    estado_objetivo['L1'] = 0
                    # Imprime el esfuerzo o el costo requerido hasta el momento
                    print('Esfuerzo actual: '+str(esfuerzo))
                    # Rompe el ciclo para seguir a la seguiente etapa
                    break
                elif(estado_valor == '0'):
                    # No requiere esfuerzo por lo tanto la variable "esfuerzo" se mantiene y se imprime
                    print('Sus manos están limpias')
                    print('Esfuerzo no requerido')
                    # Imprime el esfuerzo o el costo requerido hasta el momento
                    print('Esfuerzo actual: '+str(esfuerzo))
                    break
                else:
                    # Se presenta un mensaje indicando cuál fue el error
                    print('Opción no válida. Ingrese 1 o 0.')
            # While do que ejecutará su bloque de código simepre que sea difirente de "Salir"
            while(respuesta_localizacion != 'Salir' ):
                print('---Agente Dispensador de jabón---')
                print('---------------Menú--------------')
                print('(Se debe ingresar la cadena de texto entre comillas, ejemplo: Salir)')
                print('2: "L2" = cocina')
                print('3: "L3" = sala de estar')
                print('4: "Salir"')
                # Almacena la segunda localización del dispensador de jabón
                respuesta_localizacion = input('Ingrese la segunda localización: ')
                # Si la localización es igual a "L2" <=> cocina, entonces
                if(respuesta_localizacion == 'L2'):
                    # Do while
                    while(True):
                        # Almacena el estado de la localización 2 (L2)
                        estado_valor = input('¿La persona en la habitación '+respuesta_localizacion+' tiene las manos sucias?  (1:Si; 0:No) ')
                        # Si el estado de la localización 2 (L2) es igual a "1" <=> sucio, entonces
                        if(estado_valor == '1'):
                            # Imprime un mensaje de que se efectuó una acción
                            print('Manos sucias. Dispensando jabón...')
                            # Aumenta en una unidad el esfuerzo generado
                            esfuerzo +=1
                            # Se actualiza el estado de la localización dos (L2) de sucio (1) a limpio (0)
                            estado_objetivo['L2'] = 0
                            # Imprime el esfuerzo o costo actual
                            print('Esfuerzo actual: '+str(esfuerzo))
                            # Conociendo las dos localizaciones iniciales se puede mostrar un mensaje de manera directa
                            # de la localización restante.
                            estado_valor_restante = input('¿La persona en la habitación L3 (sala de estar) tiene las manos sucias?  (1:Si; 0:No) ')
                            # Si el estado de la localización 3 (L3) es igual a "1" <=> sucio, entonces
                            if(estado_valor_restante == '1'):
                                # Imprime un mensaje de que se efectuó una acción
                                print('Manos sucias. Dispensando jabón...')
                                # Aumenta el esfuerzo requerido en una unidad
                                esfuerzo +=1
                                # Se actualiza el estado de la localización tres (L3) de sucio (1) a limpio (0)
                                estado_objetivo['L3'] = 0
                                # Se imprime el estado objetivo 
                                print('Estado objetivo: '+str(estado_objetivo))
                                # Se imprime el esfuerzo requerido hasta esta etapa
                                print('Esfuerzo total: '+str(esfuerzo))
                                print('Finalizando programa de agente dispensador de jabón...')
                                # Se interrumpe la ejución con un tiempo de espera de 3 segundos
                                # Parametro: el tiempo en segundos
                                # Resultado: pausa la ejecución por tres segundos 
                                time.sleep(3)
                                # Se finaliza el programa                                
                                quit()
                            # Si el estado de la localización 3 (L3) es igual a "0" <=> limpio, entonces
                            elif(estado_valor_restante == '0'):
                                # Imprime mensaje al usuario de que no requiere acción adicional
                                print('Sus manos están limpias')
                                print('Esfuerzo no requerido')
                                # Se imprime el estado objetivo 
                                print('Estado objetivo: '+str(estado_objetivo))
                                # Se imprime el esfuerzo requerido hasta esta etapa
                                print('Esfuerzo total: '+str(esfuerzo))
                                print('Finalizando programa de agente dispensador de jabón...')
                                # Se interrumpe la ejución con un tiempo de espera de 3 segundos
                                # Parametro: el tiempo en segundos
                                # Resultado: pausa la ejecución por tres segundos 
                                time.sleep(3)
                                # Se finaliza el programa   
                                quit()
                            else:
                                 # Se imprime un mensaje de error 
                                print('Opción no válida. Ingrese 1 o 0.')
                        # Si el estado de la localización 2 (L2) es igual a "0" <=> limpio, entonces
                        elif(estado_valor == '0'):
                            # Imprime mensaje al usuario de que no requiere acción adicional
                            print('Sus manos están limpias')
                            print('Esfuerzo no requerido')
                            # Se imprime el esfuerzo requerido hasta esta etapa
                            print('Esfuerzo actual: '+str(esfuerzo))
                            # Almacena el estado de la localización 3 (L3) 
                            estado_valor_restante = input('¿La persona en la habitación L3 (sala de estar) tiene las manos sucias?  (1:Si; 0:No) ')
                            # Si el estado de la localización 3 (L3) es igual a "1" <=> sucio, entonces
                            if(estado_valor_restante == '   1'):
                                # Imprime un mensaje de que se efectuó una acción
                                print('Manos sucias. Dispensando jabón...')
                                # Aumenta el esfuerzo requerido en una unidad
                                esfuerzo +=1
                                # Se actualiza el estado de la localización dos (L3) de sucio (1) a limpio (0)
                                estado_objetivo['L3'] = 0
                                # Se imprime el estado objetivo
                                print('Estado objetivo: '+str(estado_objetivo))
                                # Se imprime el esfuerzo requerido hasta esta etapa
                                print('Esfuerzo total: '+str(esfuerzo))
                                print('Finalizando programa de agente dispensador de jabón...')
                                # Se interrumpe la ejución con un tiempo de espera de 3 segundos
                                # Parametro: el tiempo en segundos
                                # Resultado: pausa la ejecución por tres segundos 
                                time.sleep(3)
                                # Se finaliza el programa   
                                quit()
                            # Si el estado de la localización 3 (L3) es igual a "0" <=> limpio, entonces
                            elif(estado_valor_restante == '0'):
                                # Imprime mensaje al usuario de que no requiere acción adicional
                                print('Sus manos están limpias')
                                print('Esfuerzo no requerido')
                                # Se imprime el estado objetivo y el esfuerzo requerido hasta esta etapa
                                print('Estado objetivo: '+str(estado_objetivo))
                                print('Esfuerzo total: '+str(esfuerzo))
                                print('Finalizando programa de agente dispensador de jabón...')
                                # Se interrumpe la ejución con un tiempo de espera de 3 segundos
                                # Parametro: el tiempo en segundos
                                # Resultado: pausa la ejecución por tres segundos 
                                time.sleep(3)
                                # Se finaliza el programa
                                quit()
                            else:
                                # Se imprime un mensaje de error
                                print('Opción no válida. Ingrese 1 o 0.')
                            break
                        else:
                            # Se imprime un mensaje de error 
                            print('Opción no válida. Ingrese 1 o 0.')
                # Si la localización 3 ingresado es "L3" <=> sala de estar, entonces
                elif respuesta_localizacion == 'L3':
                    # Ciclo do while
                    while(True):
                        # Se almacena el estado de la localización "L3"
                        estado_valor = input('¿La persona en la habitación '+respuesta_localizacion+' tiene las manos sucias?  (1:Si; 0:No) ')
                        # Si el estado de la localización 3 (L3) es iguala "1"  (sucio), entonces 
                        if(estado_valor == '1'):
                            # Imprime un mensaje de que se efectuó una acción
                            print('Manos sucias. Dispensando jabón...')
                            # Aumenta el esfuerzo requerido en una unidad
                            esfuerzo +=1
                            # Se actualiza el estado de la localización tres (L3) de sucio (1) a limpio (0)
                            estado_objetivo['L3'] = 0
                            # Se imprime el esfuerzo requerido hasta esta etapa
                            print('Esfuerzo actual: '+str(esfuerzo))
                            # Almacena el estado de la localización 2 (L2)
                            estado_valor_restante = input('¿La persona en la habitación L2 (cocina) tiene las manos sucias?  (1:Si; 0:No) ')
                            # Si el estado de L2 es igual a 1 (sucio), entonces
                            if(estado_valor_restante == '1'):
                                # Las manos de L2 están sucias
                                print('Manos sucias. Dispensando jabón...')
                                # Aumenta el esfuerzo requerido en una unidad
                                esfuerzo +=1
                                # Se actualiza el estado de la localización dos (L2) de sucio (1) a limpio (0)
                                estado_objetivo['L2'] = 0
                                # Se imprime el estado objetivo y el esfuerzo requerido hasta esta etapa
                                print('Estado objetivo: '+str(estado_objetivo))
                                print('Esfuerzo total: '+str(esfuerzo))
                                print('Finalizando programa de agente dispensador de jabón...')
                                # Se interrumpe la ejución con un tiempo de espera de 3 segundos
                                time.sleep(3)
                                # Se finaliza el programa   
                                quit()
                            # Si el estado de L2 es igual a 0 (limpio), entonces
                            elif(estado_valor_restante == '0'):
                                #Las manos de L2 están limpias
                                print('Sus manos están limpias')
                                print('Esfuerzo no requerido')
                                # Se imprime el estado objetivo y el esfuerzo requerido hasta esta etapa
                                print('Estado objetivo: '+str(estado_objetivo))
                                print('Esfuerzo total: '+str(esfuerzo))
                                print('Finalizando programa de agente dispensador de jabón...')
                                # Se interrumpe la ejución con un tiempo de espera de 3 segundos
                                time.sleep(3)
                                # Se finaliza el programa   
                                quit()
                            else:
                                print('Opción no válida. Ingrese 1 o 0.')
                        # Si el estado de L3 es igual a 0 (limpio), entonces
                        elif(estado_valor == '0'):
                            #Las manos de L2 están limpias
                            print('Sus manos están limpias')
                            print('Esfuerzo no requerido')
                            # Se imprime el esfuerzo requerido hasta esta etapa
                            print('Esfuerzo actual: '+str(esfuerzo))
                            # Almacena el estado de la localización L2
                            estado_valor_restante = input('¿La persona en la habitación L2 (cocina) tiene las manos sucias?  (1:Si; 0:No) ')
                            # Si el estado de L2 es igual a "1" (sucio), entonces
                            if(estado_valor_restante == '1'):
                                # Las manos de L2 están sucias
                                print('Manos sucias. Dispensando jabón...')
                                # Aumenta el esfuerzo requerido en una unidad
                                esfuerzo +=1
                                # Se actualiza el estado de la localización dos (L2) de sucio (1) a limpio (0)
                                estado_objetivo['L2'] = 0
                                # Se imprime el estado objetivo y el esfuerzo requerido hasta esta etapa
                                print('Estado objetivo: '+str(estado_objetivo))
                                print('Esfuerzo total: '+str(esfuerzo))
                                print('Finalizando programa de agente dispensador de jabón...')
                                # Se interrumpe la ejución con un tiempo de espera de 3 segundos
                                time.sleep(3)
                                # Se finaliza el programa   
                                quit()
                            # Si el estado de L2 es igual a "0" (limpio), entonecs
                            elif(estado_valor == '0'):
                                # Las manos de L2 están limpias
                                print('Sus manos están limpias')
                                print('Esfuerzo no requerido')
                                # Se imprime el estado objetivo y el esfuerzo requerido hasta esta etapa
                                print('Estado objetivo: '+str(estado_objetivo))
                                print('Esfuerzo total: '+str(esfuerzo))
                                print('Finalizando programa de agente dispensador de jabón...')
                                # Se interrumpe la ejución con un tiempo de espera de 3 segundos
                                time.sleep(3)
                                # Se finaliza el programa   
                                quit()
                            else:
                                print('Opción no válida. Ingrese 1 o 0.')
                            break
                        else:
                            print('Opción no válida. Ingrese 1 o 0.')
                # Permite al usuario salir del bloque de comandos si la cadena de texto ingresada es igual a 
                # "Salir" mediante uso del comando "break"
                elif(respuesta_localizacion == 'Salir'):
                    break
                else:
                    print('No es una opción válida.')
        # Si la localización es igual a "L2", entonces
        elif respuesta_localizacion == 'L2':
            while(True):
                # Almacena el estado de L2
                estado_valor = input('¿La persona en la habitación '+respuesta_localizacion+' tiene las manos sucias?  (1:Si; 0:No) ')
                # Si el estado de L2 es igual a "1" (sucio), entonces
                if(estado_valor == '1'):
                    # Las manos de L2 están sucias
                    print('Manos sucias. Dispensando jabón...')
                    # Aumenta el esfuerzo requerido en una unidad
                    esfuerzo +=1
                    # Se actualiza el estado de la localización dos (L2) de sucio (1) a limpio (0)
                    estado_objetivo['L2'] = 0
                    # Imprime el esfuerzo requerido hasta esta etapa
                    print('Esfuerzo actual: '+str(esfuerzo))
                    break
                # Si el estado de L2 es igual a "0" (limpio), entonces
                elif(estado_valor == '0'):
                    #Las manos de L2 están limpias. No requiere acción
                    print('Sus manos están limpias')
                    print('Esfuerzo no requerido')
                    # Imprime el esfuerzo requerido hasta esta etapa
                    print('Esfuerzo actual: '+str(esfuerzo))
                    break
                else:
                    print('Opción no válida. Ingrese 1 o 0.')
            # While do para las localizaciones restantes. Sale si es igual a "Salir"
            while(respuesta_localizacion != 'Salir' ):
                print('---Agente Dispensador de jabón---')
                print('---------------Menú--------------')
                print('(Se debe ingresar la cadena de texto entre comillas, ejemplo: Salir)')
                print('2: "L1" = baño')
                print('3: "L3" = sala de estar')
                print('4: "Salir"')
                # Almacena la segunda localización
                respuesta_localizacion = input('Ingrese la segunda localización: ')
                # Si la localización almacenada es igual a "L1", entonces
                if(respuesta_localizacion == 'L1'):
                    # Do while
                    while(True):
                        # Almacena el estado de L1
                        estado_valor = input('¿La persona en la habitación '+respuesta_localizacion+' tiene las manos sucias?  (1:Si; 0:No) ')
                        # Si el estado de L1 es igual a "1" (sucio), entonces
                        if(estado_valor == '1'):
                            # Las manos de L1 están sucias
                            print('Manos sucias. Dispensando jabón...')
                            # Aumenta el esfuerzo requerido en una unidad
                            esfuerzo +=1
                            # Se actualiza el estado de la localización uno (L1) de sucio (1) a limpio (0)
                            estado_objetivo['L1'] = 0
                            # Imprime el esfuerzo requerido hasta esta etapa
                            print('Esfuerzo actual: '+str(esfuerzo))
                            # Almacena el estado de la localizacion restante (L3)
                            estado_valor_restante = input('¿La persona en la habitación L3 (sala de estar) tiene las manos sucias?  (1:Si; 0:No) ')
                            # Si el estado de L3 es igual a "1" (sucia), entonces
                            if(estado_valor_restante == '1'):
                                # Las manos de L3 están sucias
                                print('Manos sucias. Dispensando jabón...')
                                # Aumenta el esfuerzo requerido en una unidad
                                esfuerzo +=1
                                # Se actualiza el estado de la localización tres (L3) de sucio (1) a limpio (0)
                                estado_objetivo['L3'] = 0
                                # Se imprime el estado objetivo y el esfuerzo requerido hasta esta etapa
                                print('Estado objetivo: '+str(estado_objetivo))
                                print('Esfuerzo total: '+str(esfuerzo))
                                print('Finalizando programa de agente dispensador de jabón...')
                                # Se interrumpe la ejución con un tiempo de espera de 3 segundos
                                time.sleep(3)
                                # Se finaliza el programa   
                                quit()
                            # Si el estado de L3 es igual a "0" (limpia), entonces
                            elif(estado_valor == '0'):
                                # Las manos de L3 están limpias. Sin esfuerzo requerido
                                print('Sus manos están limpias')
                                print('Esfuerzo no requerido')
                                # Se imprime el estado objetivo y el esfuerzo requerido hasta esta etapa
                                print('Estado objetivo: '+str(estado_objetivo))
                                print('Esfuerzo total: '+str(esfuerzo))
                                print('Finalizando programa de agente dispensador de jabón...')
                                # Se interrumpe la ejución con un tiempo de espera de 3 segundos
                                time.sleep(3)
                                # Se finaliza el programa   
                                quit()
                            else:
                                print('Opción no válida. Ingrese 1 o 0.')
                        # Si el estado de L1 es igual a "0" (limpio), entonces
                        elif(estado_valor == '0'):
                            # Las manos de L1 están limpias. Sin esfuerzo requerido
                            print('Sus manos están limpias')
                            print('Esfuerzo no requerido')
                            # Imprime el esfuerzo requerido hasta esta etapa
                            print('Esfuerzo actual: '+str(esfuerzo))
                            # Almacena el estado de la localización restante (L3)
                            estado_valor_restante = input('¿La persona en la habitación L3 (sala de estar) tiene las manos sucias?  (1:Si; 0:No) ')
                            # Si el estado de L3 es igual a "1" (sucio), entonces
                            if(estado_valor_restante == '1'):
                                # Las manos de L3 están sucias.
                                print('Manos sucias. Dispensando jabón...')
                                # Aumenta el esfuerzo requerido en una unidad
                                esfuerzo +=1
                                # Se actualiza el estado de la localización tres (L3) de sucio (1) a limpio (0)
                                estado_objetivo['L3'] = 0
                                # Se imprime el estado objetivo y el esfuerzo requerido hasta esta etapa
                                print('Estado objetivo: '+str(estado_objetivo))
                                print('Esfuerzo total: '+str(esfuerzo))
                                print('Finalizando programa de agente dispensador de jabón...')
                                # Se interrumpe la ejución con un tiempo de espera de 3 segundos
                                time.sleep(3)
                                # Se finaliza el programa   
                                quit()
                            # Si el estado de L3 es igual a "0", entonces
                            elif(estado_valor_restante == '0'):
                                # Las manos de L3 están limpias. Sin esfuerzo requerido
                                print('Sus manos están limpias')
                                print('Esfuerzo no requerido')
                                # Se imprime el estado objetivo y el esfuerzo requerido hasta esta etapa
                                print('Estado objetivo: '+str(estado_objetivo))
                                print('Esfuerzo total: '+str(esfuerzo))
                                print('Finalizando programa de agente dispensador de jabón...')
                                # Se interrumpe la ejución con un tiempo de espera de 3 segundos
                                time.sleep(3)
                                # Se finaliza el programa   
                                quit()
                            else:
                                print('Opción no válida. Ingrese 1 o 0.')
                            break
                        else:
                            print('Opción no válida. Ingrese 1 o 0.')
                # Si la localización es igual a "L3", entonces
                elif respuesta_localizacion == 'L3':
                    # Do while
                    while(True):
                        # Almacena el estado de L3
                        estado_valor = input('¿La persona en la habitación '+respuesta_localizacion+' tiene las manos sucias?  (1:Si; 0:No) ')
                        # Si el estado de L3 es igual a "1", entonces
                        if(estado_valor == '1'):
                            # Las manos de L3 están sucias
                            print('Manos sucias. Dispensando jabón...')
                            # Aumenta el esfuerzo requerido en una unidad
                            esfuerzo +=1
                            # Se actualiza el estado de la localización tres (L3) de sucio (1) a limpio (0)
                            estado_objetivo['L3'] = 0
                            # Se imprime el esfuerzo hasta la etapa actual
                            print('Esfuerzo actual: '+str(esfuerzo))
                            # Almacena el estado de la localización restante (l1)
                            estado_valor_restante = input('¿La persona en la habitación L1 (baño) tiene las manos sucias?  (1:Si; 0:No) ')
                            # Si el estado de L1 es igual a "1", entonces
                            if(estado_valor_restante == '1'):
                                # Las manos de L1 están sucias
                                print('Manos sucias. Dispensando jabón...')
                                # Aumenta el esfuerzo requerido en una unidad
                                esfuerzo +=1
                                # Se actualiza el estado de la localización uno (L1) de sucio (1) a limpio (0)
                                estado_objetivo['L1'] = 0
                                # Se imprime el estado objetivo y el esfuerzo requerido hasta esta etapa
                                print('Estado objetivo: '+str(estado_objetivo))
                                print('Esfuerzo total: '+str(esfuerzo))
                                print('Finalizando programa de agente dispensador de jabón...')
                                # Se interrumpe la ejución con un tiempo de espera de 3 segundos
                                time.sleep(3)
                                # Se finaliza el programa   
                                quit()
                            # Si el estado de L1 es igual a "0", entonces
                            elif(estado_valor_restante == '0'):
                                # Las manos de L1 están sucias
                                print('Sus manos están limpias')
                                print('Esfuerzo no requerido')
                                # Se imprime el estado objetivo y el esfuerzo requerido hasta esta etapa
                                print('Estado objetivo: '+str(estado_objetivo))
                                print('Esfuerzo total: '+str(esfuerzo))
                                print('Finalizando programa de agente dispensador de jabón...')
                                # Se interrumpe la ejución con un tiempo de espera de 3 segundos
                                time.sleep(3)
                                # Se finaliza el programa   
                                quit()
                            else:
                                print('Opción no válida. Ingrese 1 o 0.')
                        # Si el estado de L3 es igual a "0", entonces
                        elif(estado_valor == '0'):
                            # Las manos de L3 están limpias
                            print('Sus manos están limpias')
                            print('Esfuerzo no requerido')
                            # Imprime el esfuerzo actual
                            print('Esfuerzo actual: '+str(esfuerzo))
                            # Almacena el estado de la localización restante (L1)
                            estado_valor_restante = input('¿La persona en la habitación L1 (baño) tiene las manos sucias?  (1:Si; 0:No) ')
                            # Si el estado de L1 es igual a "1", entonces
                            if(estado_valor_restante == '1'):
                                # Las manos de L1 están sucias
                                print('Manos sucias. Dispensando jabón...')
                                esfuerzo +=1
                                # Se actualiza el estado de la localización uno (L1) de sucio (1) a limpio (0)
                                estado_objetivo['L1'] = 0
                                # Se imprime el estado objetivo y el esfuerzo requerido hasta esta etapa
                                print('Estado objetivo: '+str(estado_objetivo))
                                print('Esfuerzo total: '+str(esfuerzo))
                                print('Finalizando programa de agente dispensador de jabón...')
                                # Se interrumpe la ejución con un tiempo de espera de 3 segundos
                                time.sleep(3)
                                # Se finaliza el programa   
                                quit()
                            # Si el estado de L1 es igual a "0", entonces
                            elif(estado_valor == '0'):
                                # Las manos de L1 están limpias. Sin esfuerzo requerido
                                print('Sus manos están limpias')
                                print('Esfuerzo no requerido')
                                # Se imprime el estado objetivo y el esfuerzo requerido hasta esta etapa
                                print('Estado objetivo: '+str(estado_objetivo))
                                print('Esfuerzo total: '+str(esfuerzo))
                                print('Finalizando programa de agente dispensador de jabón...')
                                # Se interrumpe la ejución con un tiempo de espera de 3 segundos
                                time.sleep(3)
                                # Se finaliza el programa   
                                quit()
                            else:
                                print('Opción no válida. Ingrese 1 o 0.')
                            break
                        else:
                            print('Opción no válida. Ingrese 1 o 0.')
                # Si la respuesta es "Salir" rompe el bucle repetitivo
                elif(respuesta_localizacion == 'Salir'):
                    break
                else:
                    print('No es una opción válida.')
        # Si la localización ingresada es "L3", entonces
        elif respuesta_localizacion == 'L3':
            ...
        elif(respuesta_localizacion == 'Salir'):
            break
        else:
            print('No es una opción válida.')  

# Se hace el llamado a la función generada
# Parametros de entrada: Ninguno
# Resultado: Ejecución completa del agente dispesador de jabón
dispensadorJabon()