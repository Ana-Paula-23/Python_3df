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
    |         Bienvenido/a al generador de contraseñas             |
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
                    print("Salió del programa")
                    sys.exit()
                else:
                    print("El valor ingresado no es válido. Ingrese 's' o 'n'." )
    
    elif menu in ["1","2","3","4"]:
        match menu:
            case "1":
                tipo = diccionario['letras']
            case "2":
                tipo = diccionario['numeros']
            case "3":
                tipo = diccionario['letras'] + diccionario['numeros']
            case "4":
                tipo = diccionario['letras'] + diccionario['numeros'] + diccionario['caracteres']

        while True:
            os.system("cls")
            longitud = input("Por favor, ingrese la longitud de la contraseña: ") 
            
            if longitud.isdigit() and int(longitud) > 0:
                longitud=int(longitud)
                break
            else:
                print("El valor ingresado no es válido. El valor debe ser un número entero.")

        contraseña = ""
        for i in range(longitud):
            contraseña += secrets.choice(tipo)
        
        os.system("cls")
        print(f"La contraseña generada es: {contraseña}, que contiene {longitud} caracteres")
        
        while True:    
            nueva_contraseña = input("¿Quiere generar otra contraseña? (s/n): ")

            if nueva_contraseña.lower() == "n":
                print("Salió del programa")
                sys.exit()
            elif nueva_contraseña.lower() == "s":
                break
            else:
                print("El valor ingresado no es válido. Ingrese 's' o 'n'." )
                        
    else:
        print("¡El valor ingresado es incorrecto!")