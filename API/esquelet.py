### Imports ################################################## 
import os   #per neteja la pantalla
import json #per desar i llegir dades en format JSON

#Variables ###################################################

#Nom del fitxer on desar/carregar dades
nom_fitxer = "alumnes.json"

alumnes = []


### menu() ###################################################
#   Aquesta funció mostra el menú d'opcions per pantalla. 
#   
#   Retorna (str): l'opció escollida per l'usuari
##############################################################
def menu():
    #Netejem la pantalla
    os.system('cls')            
    
    #Mostrem les diferents opcions
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

    #i retornem l'opció escollida per l'usuari
    return input()



### Programa ################################################

#Fins a l'infinit (i més enllà)
while True:
    
    #Executem una opció funció del que hagi escollit l'usuari
    match menu():

        # Mostrar alumnes ##################################
        case "1":
            os.system('cls')
            print("Mostrar alumnes")
            print("-------------------------------")
            

            #Introduiu el vostre codi per mostrar alumnes aquí
            if not alumnes:
                print("No hi ha alumnes carregats.")
            else:
                for alumne in alumnes:
                    print(f"ID: {alumne['id']} | Nom: {alumne['nom']} {alumne['cognom']}")
            input("\nPrem Enter per continuar...")
    
        # Afegir alumne ##################################
        case "2":
            os.system('cls')
            print("Afegir alumne")
            print("-------------------------------")
            
            #Introduiu el vostre codi per afegir un alumne aquí
                
            input()
    
        # Veure alumne ##################################
        case "3":
            os.system('cls')
            print("Veure alumne")
            print("-------------------------------")
            
            #Introduiu el vostre codi per veure un alumne aquí

            input()

        # Esborrar alumne ##################################
        case "4":
            os.system('cls')
            print("Esborrar alumne")
            print("-------------------------------")
          
            #Introduiu el vostre codi per esborrar un alumne aquí
  
            input()

        # Desar a fitxer ##################################
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


        # Llegir fitxer ##################################
        case "6":    
            os.system('cls')
            print("Llegir fitxer")
            print("-------------------------------")

            try:
                with open(nom_fitxer, "r", encoding="utf-8") as f:
                    alumnes = json.load(f)
                print(f"S'han carregat {len(alumnes)} alumnes des de {nom_fitxer}.")
                print("Dades carregades:")
                print(alumnes)
                
            except FileNotFoundError:
                print("El fitxer no existeix.")
            except json.JSONDecodeError:
                print("Error: el fitxer no té format JSON vàlid.")
            except Exception as e:
                print(f"Error en llegir el fitxer: {e}")
            
            input("\nPrem Enter per continuar...")

      

        # Sortir ##################################
        case "0":
            os.system('cls')
            print("Adeu!")

            #Trenquem el bucle infinit
            break

        #Qualsevol altra cosa #####################   
        case _:
            print("\nOpció incorrecta\a")            
            input()
