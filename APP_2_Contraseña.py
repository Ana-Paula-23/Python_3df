#################################################
#           GENERADOR DE CONTRASEÑAS            #
#################################################

import secrets, string, sys, os

diccionario = {
  'letras': string.ascii_letters,
  'numeros': string.digits,
  'caracteres': string.punctuation
}

while True:
    os.system("cls")
    menu = input("""
    +--------------------------------------------------------------+
    |           Bienvenido/a al generador de contraseñas           |
    +--------------------------------------------------------------+
    
    Seleccione una de las siguientes opciones:

        ✦ 1. Generar contraseña sólo de letras
        ✦ 2. Generar contraseña sólo de números
        ✦ 3. Generar contraseña con Letras y Números
        ✦ 4. Generar contraseña con Letras, Números y Caracteres
        ✦ 0. Salir
    
    >> Escriba la opción seleccionada:  """)
    
    if menu =="0":
            while True:
                salida = input("¿Está seguro que quiere salir? (s/n): ")
                if salida.lower() == "n":
                    break
                elif salida.lower() == "s":
                    print("Gracias por utilizar el programa. ¡Hasta la próxima!")
                    sys.exit()
                else:
                    os.system("cls")
                    print("El valor ingresado n͟o͟ es v͟á͟l͟i͟d͟o͟. Ingrese 's' o 'n'." )
                    
    
    elif menu in ["1","2","3","4"]:
        match menu:
            case "1":
                tipo = diccionario['letras']
                seleccion = "sólo de letras"
            case "2":
                tipo = diccionario['numeros']
                seleccion = "sólo de números"
            case "3":
                tipo = diccionario['letras'] + diccionario['numeros']
                seleccion = "con letras y números"
            case "4":
                tipo = diccionario['letras'] + diccionario['numeros'] + diccionario['caracteres']
                seleccion = "con letras, números y caracteres"

        while True:
            os.system("cls")
            longitud = input(f"""
    Usted ha seleccionado la opción para generar una contraseña {seleccion}.
     
    >> Por favor, ingrese la longitud de la contraseña: """) 
            
            if longitud.isdigit() and int(longitud) > 0:
                longitud=int(longitud)
                break
            else:
                input("""
    El valor ingresado n͟o͟ es v͟á͟l͟i͟d͟o͟. El valor debe ser un número entero.
    
    Presione ENTER para continuar...""")

        contraseña = ""
        for i in range(longitud):
            contraseña += secrets.choice(tipo)
        
        os.system("cls")
        print(f"La contraseña generada es: {contraseña}, cuya longitud es {longitud}.")
        
        while True:    
            nueva_contraseña = input("¿Quiere generar otra contraseña? (s/n): ")

            if nueva_contraseña.lower() == "n":
                print("Gracias por utilizar el programa. ¡Hasta la próxima!")
                sys.exit()
            elif nueva_contraseña.lower() == "s":
                break
            else:
                os.system("cls")
                print("El valor ingresado n͟o͟ es v͟á͟l͟i͟d͟o͟. Ingrese 's' o 'n'." )
                        
    else:
        input("""
    ¡El valor ingresado es incorrecto!
    
    Presione ENTER para continuar...""")