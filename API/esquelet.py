### Imports ################################################## 
import os   # Para limpiar la pantalla
import json # Para guardar y leer datos JSON

#Variables ###################################################

# Nombre del fichero donde guardar/cargar datos
nom_fitxer = "alumnes.json"

# Lista de alumnos
alumnes = []

# Variable para controlar el siguiente ID disponible
# (se incrementa cada vez que se añade un nuevo alumno)
id_seguent = 1


### menu() ###################################################
#   Esta función muestra el menú de opciones por pantalla.  
#   Devuelve (str): la opción elegida por el usuario.
##############################################################
def menu():

    #Limpiamos la pantalla
    os.system('cls')            
    
    #Mostramos las diferentes opciones disponibles
    print("Gestió alumnes")
    print("-------------------------------")
    print("1. Mostrar alumnes")
    print("2. Afegir alumne")
    print("3. Veure alumne")
    print("4. Esborrar alumne")

    print("\n5. Desar a fitxer")
    print("6. Llegir fitxer")

    print("\n0. Sortir\n\n\n")
    print(">", end=" ")

    #y devolvemos la opción elegida por el usuario
    return input()



### Programa principal ################################################

#Fins a l'infinit (i més enllà)
while True:
    
    #Ejecutamos una opción función de lo que haya escogido el usuario
    match menu():

        # 1. Mostrar alumnos ##################################
        case "1":
            os.system('cls')
            print("Mostrar alumnes")
            print("-------------------------------")
            

            if not alumnes:
                print("No hi ha alumnes carregats.")
            else:
                for alumne in alumnes:
                    print(f"ID: {alumne['id']} | Nom: {alumne['nom']} {alumne['cognom']}")
            input("\nPrem Enter per continuar...")
    
        # 2. Añadir alumno ##################################
        case "2":
            os.system('cls')
            print("Afegir alumne")
            print("-------------------------------")
            
            nom = input("Nom:")    
            cognom = input("Cognom:")

            dia = int(input("Dia de naixement:"))
            mes = int(input("Mes de naixement:"))
            any = int(input("Any de naixement:"))

            treballa = input("Treballa? (si/no):").lower() == "si"
            curs = input("curs (DAW1, DAW2, DAM1, DAM2, ASIX1, ASIX2)")

            # Generar email según el curso (1º -> 2024, 2º -> 2023)
            any_email = "2024" if "1" in curs else "2023"
            email = f"{any_email}_{nom.lower()}.{cognom.lower()}@iticbcn.cat"

            alumne = {
                "id": id_seguent,
                "nom": nom,
                "cognom": cognom,
                "data": {
                    "dia": dia,
                    "mes": mes,
                    "any": any
                },
                "email": email,
                "feina": treballa,
                "curs": curs
            }

            alumnes.append(alumne)
            id_seguent += 1
            print(f"Alumne afegit: {alumne}")
            input("\nPrem Enter per continuar...")

        # 3. Ver alumno ##################################
        case "3":
            os.system('cls')
            print("Veure alumne")
            print("-------------------------------")
            
            id_buscat = int(input("Introduïu l'ID de l'alumne: "))
            alumne_trobat = False

            for alumne in alumnes:
                if alumne["id"] == id_buscat:
                    alumne_trobat = True
                    print(f"ID: {alumne['id']}")
                    print(f"Nom: {alumne['nom']} {alumne['cognom']}")
                    print(f"Data de naixement: {alumne['data']['dia']}/{alumne['data']['mes']}/{alumne['data']['any']}")
                    print(f"Email: {alumne['email']}")
                    print(f"Treballa: {'Sí' if alumne['feina'] else 'No'}")
                    print(f"Curs: {alumne['curs']}")
                    break
                
            if not alumne_trobat:
                print("No s'ha trobat cap alumne amb aquest ID.")

            input("\nPrem Enter per continuar...")

        # 4. Borrar alumno ##################################
        case "4":
            os.system('cls')
            print("Esborrar alumne")
            print("-------------------------------")
          
            id_borrar = int(input("Introduïu l'ID de l'alumne a esborrar: "))
            alumne_trobat = False

            for alumne in alumnes:
                if alumne["id"] == id_borrar:
                    alumnes.remove(alumne)
                    alumne_trobat = True
                    print(f"Alumne amb ID {id_borrar} esborrat.")
                    break

            if not alumne_trobat:
                print("No s'ha trobat cap alumne amb aquest ID.")

            input("\nPrem Enter per continuar...")

        # 5. Guardar en fichero ##################################
        case "5":
            os.system('cls')
            print("Desar a fitxer")
            print("-------------------------------")

            #Introduiu el vostre codi per desar a fitxer aquí
         
            try:
                with open(nom_fitxer, "w", encoding="utf-8") as f:
                    json.dump(alumnes, f, indent=4, ensure_ascii=False)
                print(f"S'han desat {len(alumnes)} alumnes al fitxer {nom_fitxer}.")
            except Exception as e:
                print(f"Error en desar el fitxer: {e}")

            input("\nPrem Enter per continuar...")


        # 6. Leer fichero ##################################
        case "6":    
            os.system('cls')
            print("Llegir fitxer")
            print("-------------------------------")

            
            try:
                with open(nom_fitxer, "r", encoding="utf-8") as f:
                    alumnes = json.load(f)
                
                print(f"S'han carregat {len(alumnes)} alumnes des de {nom_fitxer}.")

                # Buscar el ID más alto y preparar el siguiente
                if alumnes:
                    id_seguent = max(alumne["id"] for alumne in alumnes) + 1
                else:
                    id_seguent = 1

                print("Dades carregades correctament.")
                
            except FileNotFoundError:
                print("El fitxer no existeix.")
            except json.JSONDecodeError:
                print("Error: el fitxer no té format JSON vàlid.")
            except Exception as e:
                print(f"Error en llegir el fitxer: {e}")
            
            input("\nPrem Enter per continuar...")

      

        # 0. Salir ##################################
        case "0":
            os.system('cls')
            print("Adeu!")

            #Rompemos el bucle infinito
            break

        # Opción incorrecta #####################   
        case _:
            print("\nOpció incorrecta\a")            
            input()
