## APP TICKET ##
import random, sys, os,json


if os.path.exists("tickets.json"):
    with open('tickets.json','r',encoding="utf-8") as archivo:
        info_ticket = json.load(archivo)
else:
    info_ticket = {
        "Ticket": [],
        "Nombre": [],
        "Sector" : [],
        "Asunto" : [],
        "Problema" : []
                }  
    
def menu_continua():
    while True:             
         menu_lector_salida = input("""
                ================================================================
                    1. Leer otro ticket.
                    2. Volver al menú principal
                ================================================================
                    Seleccione una opción:  """)
         
         if menu_lector_salida == "1":
            return "continua"
         elif menu_lector_salida == "2":
            return "sale"
         else:
            print("¡El valor ingresado no es válido!")
    

while True:
    os.system("cls")
    menu = input(f"""
               ==============================================================
                            ¡Bienvenido/a al sistema de Tickets!
               ==============================================================
                    1. Generar un nuevo ticket
                    2. Leer un ticket 
                    0. Salir
               ==============================================================
                    Tickets cargados en el sistema: {len(info_ticket["Ticket"])}
               
                    Seleccione una opción: """)
    match menu:
        case "0":
            os.system("cls")
            salida=""
            while salida.lower() != "n":
                salida = input("¿Seguro que quiere salir del programa? (s/n): ")
                if salida.lower()=="s":
                    print("¡Gracias por utilizar el sistema de tickets!")
                    sys.exit()
                
                else:
                    print("¡El valor ingresado no es válido!")

        case "1":
            nuevo_ticket="s"
            
            while nuevo_ticket.lower() == "s":
                os.system("cls")
                print("Por favor, ingrese los datos para Generar un nuevo Ticket: ")
                ticket = random.randint(1000,9999)
                #print(ticket) #Solo para chequear este paso
                
                info_ticket["Ticket"].append(ticket)
                info_ticket["Nombre"].append(input("Ingrese su Nombre: "))
                info_ticket["Sector"].append(input("Ingrese su Sector: "))
                info_ticket["Asunto"].append(input("Ingrese el Asunto: "))
                info_ticket["Problema"].append(input("Describa brevemente el problema: "))
                
                #print(info_ticket) #Solo para chequear este paso
                
                with open('tickets.json','w',encoding="utf-8") as archivo:
                    json.dump(info_ticket,archivo, indent=4, ensure_ascii=False)
                
                os.system("cls")
                print(f"""
                ===============================================================
                      Se generó el siguiente Ticket Nº {info_ticket["Ticket"][-1]}
                ===============================================================
                 . Nombre: {info_ticket["Nombre"][-1]}
                 . Sector: {info_ticket["Sector"][-1]}
                 . Asunto: {info_ticket["Asunto"][-1]}

                 . Mensaje: {info_ticket["Problema"][-1]}


                            ¡ATENCION! Recordar el número de su ticket
                ===============================================================
                      """)
                
                while True:
                    nuevo_ticket = input("¿Desea generar un nuevo Ticket? (s/n): ")
                    if nuevo_ticket.lower() == "n" or nuevo_ticket.lower() == "s":
                        break
                    else:
                        print("El valor ingresado no es válido. Ingrese 's' o 'n'." )
                                 
        case "2":
            menu_lector = "1"
            
            while menu_lector == "1":
                os.system("cls")
                lector_ticket = input("Por favor, ingrese el Nº del ticket que quiere ver: ")
                
                if lector_ticket.isdigit():
                    num_ticket = int(lector_ticket)
                    
                    if num_ticket in info_ticket["Ticket"]:
                        i = info_ticket["Ticket"].index(num_ticket)
                        print(f"""
                ===============================================================
                                 Nº de Ticket: {info_ticket["Ticket"][i]}
                ===============================================================
                
                    . Nombre: {info_ticket["Nombre"][i]}
                    . Sector: {info_ticket["Sector"][i]}
                    . Asunto: {info_ticket["Asunto"][i]}
                    . Mensaje: {info_ticket["Problema"][i]}                           
                """)
                    
                        resultado = menu_continua()
                        if resultado=="sale":
                            menu_lector="2" 

                    else:
                        print("Lo sentimos, pero el número de ticket no existe o es incorrecto.")
                        resultado = menu_continua()
                        if resultado=="sale":
                            menu_lector="2" 
                else:
                    print("¡Error! El valor ingresado no es un número entero")
                    resultado = menu_continua()
                    if resultado=="sale":
                        menu_lector="2" 